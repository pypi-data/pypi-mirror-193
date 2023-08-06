from collections import defaultdict
import itertools
import typing
import uuid
from gloo.measure import measure_decorator, measure
from gloo.types import DocumentChunk, DocumentSearchResult, EmbeddingType
import pinecone
from enum import Enum


# TODO: Move away from string tags to int tags.
# The issue is typed dict doesn't support this well.
class GlooPineconeTag(str, Enum):
    APP_ID = "gloo-app-id"
    DOCUMENT_ID = "gloo-doc-id"
    DOCUMENT_SPAN_START = "gloo-doc-span-start"
    DOCUMENT_SPAN_END = "gloo-doc-span-end"
    USER_TAGS = "gloo-user-tags"


class GlooPineconeMetadata(typing.TypedDict):
    GlooPineconeTag.DOCUMENT_ID: str
    GlooPineconeTag.DOCUMENT_SPAN_START: int
    GlooPineconeTag.DOCUMENT_SPAN_END: int
    GlooPineconeTag.USER_TAGS: typing.Optional[typing.List[str]]


class PineconeSearchMatch(typing.TypedDict):
    id: str
    score: float
    metadata: GlooPineconeMetadata


class Span(typing.TypedDict):
    start: int
    end: int


class EmbeddingChunk(typing.TypedDict):
    dbId: str
    span: Span


last_embedding = None
PINECONE_KEY = "9733d995-4473-4d6d-9f3d-b448b484d271"
pinecone.init(api_key=PINECONE_KEY, environment="us-east1-gcp")


def _pinecone_init(embedding_type: EmbeddingType) -> str:
    global last_embedding

    if embedding_type == EmbeddingType.SbertMpnetBaseV2:
        PINECONE_INDEX = "test-hf"
        # PINECONE_KEY = "9733d995-4473-4d6d-9f3d-b448b484d271"
    elif embedding_type == EmbeddingType.Openai:
        PINECONE_INDEX = "test-openai"
        # PINECONE_KEY = "3f30296a-33a4-468b-a344-9709be651491"
        # raise Exception('Embedding not yet supported')
    return PINECONE_INDEX


def remove_from_pinecone(
    appId: str, documentId: str, embedding_type: EmbeddingType
):
    index_name = _pinecone_init(embedding_type)
    # Most documents don't really have more than 10 vectors. If we encounter
    # larger documents we can consider using a pool.
    index = pinecone.Index(index_name)
    index.delete(
        namespace=appId, filter={GlooPineconeTag.DOCUMENT_ID: documentId}
    )


def to_pinecone(
    embedding_type: EmbeddingType,
    chunks: typing.Iterable[DocumentChunk],
    *,
    appId: str,
    documentId: str,
    documentTags: typing.List[str],
):
    metadata = {
        GlooPineconeTag.DOCUMENT_ID: documentId,
        GlooPineconeTag.USER_TAGS: documentTags,
    }
    e_chunks: typing.List[EmbeddingChunk] = []
    vectors: typing.List[pinecone.Vector] = []
    for chunk in chunks:
        db_id = str(uuid.uuid4())
        e_chunks.append(
            EmbeddingChunk(
                dbId=db_id,
                span=Span(start=chunk["span"][0], end=chunk["span"][1]),
            )
        )
        vectors.append(
            pinecone.Vector(
                id=db_id,
                values=chunk["embeddings2"],
                metadata={
                    **metadata,
                    GlooPineconeTag.DOCUMENT_SPAN_START: chunk["span"][0],
                    GlooPineconeTag.DOCUMENT_SPAN_END: chunk["span"][1],
                },
            )
        )
    if vectors:
        index_name = _pinecone_init(embedding_type)
        # Most documents don't really have more than 10 vectors. If we encounter
        # larger documents we can consider using a pool.
        index = pinecone.Index(index_name)
        # Delete all data for that document first.
        index.delete(
            filter={GlooPineconeTag.DOCUMENT_ID: documentId},
            namespace=appId,
        )
        # Add new data.
        index.upsert(vectors, namespace=appId)
    return e_chunks


@measure_decorator
def query_pinecone(
    embedding_type: EmbeddingType,
    embedding: typing.List[float],
    *,
    appId: str,
    max_k: int,
    tag_filters: typing.Optional[typing.List[str]],
):
    index_name = _pinecone_init(embedding_type)
    # Most documents don't really have more than 10 vectors. If we encounter
    # larger documents we can consider using a pool.
    index = pinecone.Index(index_name)
    with measure("pc-query"):
        query_result = index.query(
            embedding,
            namespace=appId,
            include_metadata=True,
            include_values=False,
            top_k=max_k,
            filter=None
            if tag_filters is None
            else {GlooPineconeTag.USER_TAGS: {"$in": tag_filters}},
        )

    with measure("pc-post"):
        # First merge any relevant chunks returned with nearby chunks.
        search_result_map: typing.DefaultDict[
            str, DocumentSearchResult
        ] = defaultdict(lambda: DocumentSearchResult())
        for result in typing.cast(
            typing.List[PineconeSearchMatch], query_result["matches"]
        ):
            doc_id = result["metadata"][GlooPineconeTag.DOCUMENT_ID]
            if (
                GlooPineconeTag.DOCUMENT_SPAN_START not in result["metadata"]
                or GlooPineconeTag.DOCUMENT_SPAN_END not in result["metadata"]
            ):
                # Somehow bad data got stored.
                # We should log something here.
                continue
            span_start, span_end = (
                result["metadata"][GlooPineconeTag.DOCUMENT_SPAN_START],
                result["metadata"][GlooPineconeTag.DOCUMENT_SPAN_END],
            )
            search_result_map[doc_id].add_chunk(
                {
                    "score": result["score"],
                    "span": (span_start, span_end),
                }
            )

        chunks = list(
            itertools.chain(
                *map(
                    lambda result: map(
                        lambda c: (result[0], c), result[1].chunks
                    ),
                    search_result_map.items(),
                )
            )
        )
        # Return the relevant chunks in sorted order.
        chunks.sort(key=lambda c: c[1]["score"], reverse=True)
    return chunks

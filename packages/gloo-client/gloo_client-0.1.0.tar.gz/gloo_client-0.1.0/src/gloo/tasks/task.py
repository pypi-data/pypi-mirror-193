from collections import defaultdict
import itertools
import typing
from gloo.db.document import DocumentModelItem
from gloo.measure import measure_decorator, measure, enable_measure
from gloo.pinecone_integration import (
    Span,
    query_pinecone,
    remove_from_pinecone,
    to_pinecone,
)
from gloo.token_chunker import TokenChunker
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.embeddings.base import Embeddings
from unidecode import unidecode

from gloo.types import ChunkSearchResult, EmbeddingType, StageType


DEFAULT_CHUNK_SIZE = 512

HF_EMBEDDING_MODEL_NAME = "sentence-transformers/all-mpnet-base-v2"

T = typing.TypeVar("T")


def batches(
    iterable: typing.Iterable[T], batch_size: int = 100
) -> typing.Generator[typing.Tuple[T, ...], None, None]:
    """A helper function to break an iterable into chunks of size batch_size."""
    it = iter(iterable)
    chunk = tuple(itertools.islice(it, batch_size))
    while chunk:
        yield chunk
        chunk = tuple(itertools.islice(it, batch_size))


def memoize(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result

    return wrapper


@memoize
def get_embedder(
    embedding_type: EmbeddingType,
) -> Embeddings:
    embeddings = (
        HuggingFaceEmbeddings(model_name=HF_EMBEDDING_MODEL_NAME)
        if embedding_type == EmbeddingType.SbertMpnetBaseV2
        else OpenAIEmbeddings(
            openai_api_key="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",
        )
    )
    return embeddings


def remove_document(
    app_id: str, document_id: str, embedding_type: EmbeddingType
) -> None:
    doc = DocumentModelItem.load(appId=app_id, documentId=document_id)
    try:
        remove_from_pinecone(
            appId=app_id, documentId=document_id, embedding_type=embedding_type
        )
        doc.update_embedding_status(e_type=embedding_type, stage=None)
    except Exception as e:
        doc.update_embedding_status(
            e_type=embedding_type, stage=StageType.Error
        )
        # We are ok not reraising here.


def process_document(
    app_id: str,
    document_id: str,
    embedding_type: EmbeddingType,
    skip_if_ready: bool = False,
) -> None:
    # Load the document.
    doc = DocumentModelItem.load(appId=app_id, documentId=document_id)

    if skip_if_ready:
        for s in doc.status:
            if s["type"] == embedding_type and s["stage"] == StageType.Ready:
                return

    # Load the tokenizer
    tk = TokenChunker.forEmbedding(embedding_type)

    # Load document content
    content = doc.read()

    # Signal to db we're working on this data.
    doc.update_embedding_status(
        e_type=embedding_type, stage=StageType.Processing
    )

    try:
        # We should remove weird non-encodeable characters from
        # the model.
        cleaned_content = unidecode(content)
        chunks = tk.to_chunks(cleaned_content)
        e_chunks = to_pinecone(
            embedding_type,
            chunks,
            appId=app_id,
            documentId=doc.documentId,
            documentTags=doc.tags,
        )
        doc.update_embedding_status(
            e_type=embedding_type,
            stage=StageType.Ready,
            chunks=e_chunks,
        )
    except Exception as e:
        doc.update_embedding_status(
            e_type=embedding_type, stage=StageType.Error
        )
        raise e


class SearchResponseSpan(typing.TypedDict):
    span: Span
    score: float


class SearchResponse(typing.TypedDict):
    documentId: str
    spans: typing.List[SearchResponseSpan]


@measure_decorator
def search_impl(
    app_id: str,
    query: str,
    embedding_type: EmbeddingType,
    max_content_size: int,
    tag_filters: typing.Optional[typing.List[str]],
):
    embedder = get_embedder(embedding_type)
    with measure("embedding-query"):
        floatlist = embedder.embed_query(query)
    query_results = query_pinecone(
        embedding_type,
        floatlist,
        appId=app_id,
        tag_filters=tag_filters,
        max_k=min(max(max_content_size // 1000, 2), 10),
    )

    with measure("post-processing"):
        group_by_doc: typing.DefaultDict[
            str, typing.List[ChunkSearchResult]
        ] = defaultdict(lambda: [])
        content_size_left = max_content_size
        for doc_id, result in query_results:
            size = result["span"][1] - result["span"][0]
            if content_size_left >= size:
                group_by_doc[doc_id].append(result)
                content_size_left -= size
            elif content_size_left > 0:
                group_by_doc[doc_id].append(
                    {
                        "score": result["score"],
                        "span": (
                            result["span"][0],
                            result["span"][0] + content_size_left,
                        ),
                    }
                )
                content_size_left = 0
            else:
                break
        matches = list(
            map(
                lambda k: SearchResponse(
                    documentId=k[0],
                    spans=list(
                        map(
                            lambda j: SearchResponseSpan(
                                span=Span(
                                    start=j["span"][0], end=j["span"][1]
                                ),
                                score=j["score"],
                            ),
                            k[1],
                        )
                    ),
                ),
                group_by_doc.items(),
            )
        )
    return {
        "matches": matches,
        "contentSize": max_content_size - content_size_left,
    }

import typing
from enum import Enum


class EmbeddingType(str, Enum):
    Openai = "OPENAI"
    SbertMpnetBaseV2 = "SBERT_MPNET_BASE_V2"


class StageType(str, Enum):
    Queued = "QUEUED"
    Processing = "PROCESSING"
    Ready = "READY"
    Error = "ERROR"


class DocumentChunk(typing.TypedDict):
    # embedding: torch.Tensor
    embeddings2: typing.List[float]
    # These are indicies relative to input string.
    span: typing.Tuple[int, int] | None


class ChunkSearchResult(typing.TypedDict):
    span: typing.Tuple[int, int]
    score: float


class DocumentSearchResult:
    def __init__(self) -> None:
        self.chunks: typing.List[ChunkSearchResult] = []
        self.score = 0.0

    def add_chunk(self, result: ChunkSearchResult) -> None:
        """
        Adds new span (start, end) to the existing search result span to the existing list.
        If the new span overlaps any of the existing spans, merge them.
        Args:
            new_span (Tuple[int, int]): The new span to add/merge.
        """
        non_overlapping_chunks: typing.List[ChunkSearchResult] = []
        overlapping_chunks: typing.List[ChunkSearchResult] = []

        # TODO: (vbv) we can do a log n search here since self.chunks is sorted.
        for chunk in self.chunks:
            span = chunk["span"]
            if span[0] <= result["span"][1] and span[1] >= result["span"][0]:
                # spans overlap, add to list of overlapping spans
                overlapping_chunks.append(chunk)
            else:
                # no overlap, add the existing span to the non-overlapping list
                non_overlapping_chunks.append(chunk)

        if len(overlapping_chunks) == 0:
            # no overlaps found, add the new span to the non-overlapping list
            non_overlapping_chunks.append(result)
        else:
            # merge the new span with all overlapping spans
            overlapping_chunks.append(result)
            start = min(map(lambda x: x["span"][0], overlapping_chunks))
            end = max(map(lambda x: x["span"][1], overlapping_chunks))

            # TODO: If the scores are widely different, there may be value
            # in keeping the chunks separate.

            # The chunk is as relevant as the first element.
            score = max(map(lambda x: x["score"], overlapping_chunks))
            non_overlapping_chunks.append(
                ChunkSearchResult(span=(start, end), score=score)
            )

        # sort the non-overlapping list and return it
        non_overlapping_chunks.sort(key=lambda x: x["span"][0])

        self.score = max(self.score, result["score"])
        self.chunks = non_overlapping_chunks

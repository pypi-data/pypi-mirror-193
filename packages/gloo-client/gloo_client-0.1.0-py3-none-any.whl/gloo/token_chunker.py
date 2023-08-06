import typing
import torch
import numpy as np
from transformers.tokenization_utils import PreTrainedTokenizerBase
from gloo.types import DocumentChunk, EmbeddingType
from transformers import AutoTokenizer
import math
from langchain.embeddings import HuggingFaceEmbeddings
import torch.nn.functional as F
import re
from langchain.embeddings.base import Embeddings
from langchain.embeddings.openai import OpenAIEmbeddings
from gloo.measure import measure_decorator


def add_values_to_rows(
    tensor: torch.Tensor,
    start_values: typing.List[int],
    end_values: typing.List[int],
) -> torch.Tensor:
    """
    Given a PyTorch tensor of shape (n, m), add a set of values to the beginning of every row and a different set to the end.

    Args:
        tensor: A PyTorch tensor of shape (n, m).
        start_values: A list of values to add to the beginning of each row.
        end_values: A list of values to add to the end of each row.

    Returns:
        A new PyTorch tensor with the values added.

    Example:
        >>> tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        >>> start_values = [10, 20, 30]
        >>> end_values = [40, 50, 60]
        >>> add_values_to_rows(tensor, start_values, end_values)
        tensor([[10, 20, 30,  1,  2,  3, 40, 50, 60],
                [10, 20, 30,  4,  5,  6, 40, 50, 60],
                [10, 20, 30,  7,  8,  9, 40, 50, 60]])
    """
    if not start_values and not end_values:
        return tensor

    dtype = tensor.dtype
    device = tensor.device

    if start_values:
        start_values_tensor = torch.tensor(
            start_values, dtype=dtype, device=device
        )
        tensor = torch.cat(
            [
                start_values_tensor.unsqueeze(0).expand(tensor.size(0), -1),
                tensor,
            ],
            dim=1,
        )

    if end_values:
        end_values_tensor = torch.tensor(
            end_values, dtype=dtype, device=device
        )
        tensor = torch.cat(
            [
                tensor,
                end_values_tensor.unsqueeze(0).expand(tensor.size(0), -1),
            ],
            dim=1,
        )

    return tensor


def get_optimal_overlap(
    tensor: torch.Tensor, chunk_size: int, min_overlap: int = 0
) -> int:
    """
    Given a PyTorch tensor and a chunk size, calculate the optimal overlap size that minimizes the amount of padding needed.

    Args:
        tensor: A PyTorch tensor of shape (1, n).
        chunk_size: The maximum size of each chunk.
        min_overlap: The minimum overlap size to consider. Default is 0.

    Returns:
        The optimal overlap size.

    Example:
        >>> tensor = torch.tensor([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
        >>> get_optimal_overlap(tensor, chunk_size=4, min_overlap=1)
        1
    """
    # TODO: Be more smart here.
    return max(100, min_overlap)


def to_overlapping_chunks(
    arr: torch.Tensor, chunk_size: int, overlap: int
) -> torch.Tensor:
    """
    Divide a numpy array into chunks with some overlap.

    Args:
        arr: A numpy array of shape (1, n).
        chunk_size: The maximum size of each chunk.
        overlap: The number of elements to overlap between adjacent chunks.

    Returns:
        A numpy array of shape (num_chunks, chunk_size).
        Each chunk contains elements of the original array with some overlap.

    Example:
        >>> tensor = torch.tensor([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
        >>> to_overlapping_chunks(tensor, chunk_size=4, overlap=2)
        tensor([[ 1,  2,  3,  4],
                [ 3,  4,  5,  6],
                [ 5,  6,  7,  8],
                [ 7,  8,  9, 10]])
    """
    # Calculate the number of chunks with overlap
    num_chunks = int(math.ceil(arr.shape[1] / (chunk_size - overlap)))

    # Create an empty array to hold the chunked data
    chunked_arr = torch.zeros((num_chunks, chunk_size), dtype=arr.dtype)

    # Fill in the chunked data using array slicing
    for i in range(num_chunks):
        start = i * (chunk_size - overlap)
        end = start + chunk_size
        chunk = arr[:, start:end]
        chunked_arr[i, : chunk.shape[1]] = chunk

    padding = (
        (num_chunks * chunk_size)
        - (chunk_size - overlap) * (num_chunks - 1)
        - arr.shape[1] % (chunk_size - overlap)
    )

    return chunked_arr, padding


class ModelMetadata(typing.TypedDict):
    name: str
    prefix: typing.List[int]
    suffix: typing.List[int]
    max_size: int


EMBEDDING_TYPE_TO_MODEL: typing.Dict[EmbeddingType, ModelMetadata] = {
    EmbeddingType.Openai: {
        "name": "openai-gpt",
        "prefix": [],
        "suffix": [],
        "max_size": 512,
    },
    EmbeddingType.SbertMpnetBaseV2: {
        "name": "sentence-transformers/all-mpnet-base-v2",
        "prefix": [0],
        "suffix": [2],
        "max_size": 512,
    },
}


def cos_sim(a, b):
    return np.dot(a, b), np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def find_matching_span(
    root_str: str, match_strs: typing.Iterable[typing.Tuple[torch.Tensor, str]]
) -> typing.Generator[
    typing.Tuple[torch.Tensor, typing.Tuple[int, int], str], None, None
]:
    """
    Finds the matching span of `match_str` within `root_str`, ignoring whitespace and case.

    Args:
        root_str (str): The string to search within.
        match_str (str): The string to search for.
        offset (int, optional): An offset to start searching within `root_str`. Defaults to 0.

    Returns:
        A tuple of two integers representing the start and end indices of the matching span, respectively. If no match is
        found, the tuple (None, None) is returned.

    Example:
        >>> find_matching_span('The quick brown fox', 'QUICK  FOX ')
        (4, 15)

        >>> find_matching_span('The quick brown fox', 'QUICK  FOX ', offset=4)
        (4, 15)
    """
    # remove all whitespace and convert to lowercase
    root_str_no_space = re.sub(r"\s+", "", root_str).lower()
    # root_str_no_space = unidecode(root_str_no_space)

    # Find all indices of whitespace characters in root_str
    whitespace_indices = np.array(
        [match.start() for match in re.finditer(r"\s", root_str)], dtype=int
    )
    mapped_whitespace_indices = whitespace_indices - np.arange(
        len(whitespace_indices)
    )

    for i, (row, match_str) in enumerate(match_strs):
        # print("Matching: ", i)
        match_str_no_space = re.sub(r"\s+", "", match_str).lower()
        # escape any special characters in match_str_no_space
        # root_str_escaped = re.escape(root_str_no_space)
        match_str_escaped = re.escape(match_str_no_space)

        # find all matches of match_str_escaped in root_str_no_space
        matches = list(
            re.finditer(match_str_escaped, root_str_no_space, flags=re.ASCII)
        )
        if not matches:
            if match_str_escaped.startswith("\#"):
                match_str_escaped = match_str_escaped.lstrip("\#")
                matches = re.finditer(
                    match_str_escaped,
                    root_str_no_space,
                    flags=re.ASCII,
                )

        # compute the start and end indices of the first match in root_str
        for match in matches:
            # print("\tMatch: ", match.span())
            start_no_space = match.start()
            end_no_space = match.end()
            # print(match.span())
            # iterate over characters in root_str, counting removed whitespace characters
            start_matching_idx = np.count_nonzero(
                mapped_whitespace_indices < start_no_space
            )
            start = start_matching_idx + start_no_space

            end_matching_idx = np.count_nonzero(
                mapped_whitespace_indices <= end_no_space
            )
            end = end_matching_idx + end_no_space
            yield row, (start, end), match_str
            break
        else:
            # if no matches were found, return None
            print(match_str_escaped)
            raise Exception("Unable to chunk this content appropriately")


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
def get_models(
    embedding_type: EmbeddingType,
) -> typing.Tuple[PreTrainedTokenizerBase, Embeddings]:
    embedder = (
        HuggingFaceEmbeddings(
            model_name=EMBEDDING_TYPE_TO_MODEL[embedding_type]["name"]
        )
        if embedding_type == EmbeddingType.SbertMpnetBaseV2
        else OpenAIEmbeddings(
            openai_api_key="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",
        )
    )
    tokenizer: PreTrainedTokenizerBase = AutoTokenizer.from_pretrained(
        EMBEDDING_TYPE_TO_MODEL[embedding_type]["name"], do_lower_case=True
    )
    return tokenizer, embedder


class TokenChunker:
    def __init__(self, embedding_type: EmbeddingType) -> None:
        self._metadata = EMBEDDING_TYPE_TO_MODEL[embedding_type]
        self._tokenizer, self._model2 = get_models(embedding_type)
        # We don't need this warning as we expect this.
        self._tokenizer.deprecation_warnings[
            "sequence-length-is-longer-than-the-specified-maximum"
        ] = True
        self._overlap = 100

    @staticmethod
    @memoize
    def forEmbedding(embedding_type: EmbeddingType):
        return TokenChunker(embedding_type)

    @property
    def chunk_size(self):
        # The chunk size always needs to care about
        return (
            self._metadata["max_size"]
            - len(self._metadata["prefix"])
            - len(self._metadata["suffix"])
        )

    def to_chunks(self, text: str):
        # First tokenize text
        encoded_text = self._tokenizer(
            text,
            add_special_tokens=False,
            return_tensors="pt",
        )
        tokens = encoded_text["input_ids"]
        # print(encoded_text["attention_mask"].shape)
        # print(tokens.shape)

        # Desired overlap between chunks
        # TODO: (vbv) at some point we should consider a dynamic overlap.
        # Important parts of text deserve to be overlapping.
        # We should also prioritize preserving paragraphs
        overlap = get_optimal_overlap(
            tokens,
            chunk_size=self.chunk_size,
            # We always want some overlap between chunks
            # but for some documents, we may allow for larger overlap
            min_overlap=self._overlap,
        )

        tokenized_chunks, padding = to_overlapping_chunks(
            tokens,
            chunk_size=self.chunk_size,
            overlap=overlap,
        )

        padded_tokenized_chunks = add_values_to_rows(
            tokenized_chunks,
            start_values=self._metadata["prefix"],
            end_values=self._metadata["suffix"],
        )

        def process_row(row):
            return (
                row,
                self._tokenizer.decode(row, skip_special_tokens=True),
            )

        # Mean Pooling - Take attention mask into account for correct averaging
        def mean_pooling(model_output, attention_mask):
            token_embeddings = model_output[
                0
            ]  # First element of model_output contains all token embeddings
            input_mask_expanded = (
                attention_mask.unsqueeze(-1)
                .expand(token_embeddings.size())
                .float()
            )
            return torch.sum(
                token_embeddings * input_mask_expanded, 1
            ) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)

        attention_mask = torch.ones(padded_tokenized_chunks.shape)
        attention_mask[-1, -padding:] = 0

        # We can gain more efficiently by using the compute_embeddings function
        # below, but right now we dont have 1:1 match so we don't
        # use it.
        def compute_embeddigns(idx, row, raw_str):
            with torch.no_grad():
                encoded_input = self._tokenizer(
                    raw_str,
                    padding=False,
                    truncation=False,
                    return_tensors="pt",
                )
                last_idx = (
                    512 - padding
                    if idx == padded_tokenized_chunks.shape[0] - 1
                    else 512
                )

                my_mask = attention_mask[idx, :last_idx].view(1, last_idx)

                print(
                    my_mask.shape,
                    encoded_input["attention_mask"].shape,
                    padding,
                )
                print(encoded_input["attention_mask"])
                if not torch.all(my_mask.eq(encoded_input["attention_mask"])):
                    print(
                        "Fail match",
                        my_mask.shape,
                        encoded_input["attention_mask"].shape,
                    )

                model_output = self._model(
                    input_ids=row[:last_idx].view(1, last_idx),
                    attention_mask=my_mask,
                )
                # Perform pooling
                sentence_embeddings = mean_pooling(model_output, my_mask)
                # return sentence_embeddings
                # print(sentence_embeddings.shape)
                # # Normalize embeddings
                return F.normalize(sentence_embeddings, p=2, dim=1)

        decoded_strings = map(process_row, padded_tokenized_chunks)
        chunks = map(
            lambda x: DocumentChunk(
                embeddings2=self._model2.client.encode(x[1][2]).tolist(),
                # embedding=compute_embeddigns(x[0], x[1][0], x[1][2]),
                span=x[1][1],
            ),
            enumerate(find_matching_span(text, decoded_strings)),
        )

        return chunks


# def main():
#     tk = TokenChunker(EmbeddingType.SBERT_MPNET_V_2)
#     nid_em = np.array(
#         tk._model2.embed_query(
#             "Should i consider having kids? or should i wait?"
#         )
#     )
#     with open("../../../../playground/data/pg.json", "r") as f:
#         pg = json.load(f)
#         # print(sum(map(lambda x: len(x["content"]), pg)))
#         for i, x in enumerate(pg):
#             if i < 5:
#                 content = unidecode(x["content"])
#                 ck = tk.to_chunks(content)
#                 print(i, len(content), x["title"], "----")
#                 for i, chunks in enumerate(ck):
#                     if chunks["span"]:
#                         # em = np.array(chunks["embedding"].tolist()[0])
#                         em2 = np.array(chunks["embeddings2"])
#                         # sim = cos_sim(em, em2)
#                         # sim_em = cos_sim(em, nid_em)
#                         sim_em2 = cos_sim(em2, nid_em)
#                         print(i, "\tChunk:", chunks["span"], sim_em2)
#                         if sim_em2[0] > 0.15 and sim_em2[0] < 0.2:
#                             print(
#                                 content[chunks["span"][0] : chunks["span"][1]]
#                             )
#                     else:
#                         print(i, "\tNo chunks")


# if __name__ == "__main__":
#     main()

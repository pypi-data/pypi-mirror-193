import typing
import uvicorn

from fastapi import FastAPI

from gloo.tasks.task import (
    process_document,
    get_embedder,
    remove_document,
    search_impl,
)
from pydantic import BaseModel

from gloo.types import EmbeddingType


class ProcessDocRequest(BaseModel):
    appId: str
    documentId: str
    embeddingType: str
    remove: bool


class SearchRequestOptions(BaseModel):
    embeddingType: str
    excludedTags: typing.Optional[typing.List[str]]
    includedTags: typing.Optional[typing.List[str]]
    maxCharacters: int


class SearchRequest(BaseModel):
    appId: str
    query: str
    options: SearchRequestOptions


app = FastAPI()


# register(
#     app,
#     app=AppService(),
#     document=DocumentService(),
#     document_group=DocumentGroupService(),
#     root=RootService(),
#     internal=InternalService(),
# )


@app.get("/")
def healthcheck():
    print("----healthcheck----")
    return {"status": "200 OK"}


@app.post("/process_document")
def process_doc(req: ProcessDocRequest):
    print(f"----process_document---- {req}")
    if req.remove:
        remove_document(
            app_id=req.appId,
            document_id=req.documentId,
            embedding_type=EmbeddingType(req.embeddingType),
        )
    else:
        process_document(
            app_id=req.appId,
            document_id=req.documentId,
            embedding_type=EmbeddingType(req.embeddingType),
        )
    return {"hello": "world"}


@app.post("/search")
def search(req: SearchRequest):
    print(f"----search---- {req}")
    return search_impl(
        app_id=req.appId,
        query=req.query,
        embedding_type=EmbeddingType(req.options.embeddingType),
        max_content_size=req.options.maxCharacters,
        tag_filters=req.options.includedTags,
    )


def start() -> None:
    """Launched with `poetry run start` at root level"""
    print("Initializing embedders")
    # get_embedder()
    get_embedder(EmbeddingType.SbertMpnetBaseV2)
    print("finish initializing embedders")
    print("----start----")
    uvicorn.run(
        "gloo.main:app",
        host="0.0.0.0",
        port=8080,
        reload=True,
    )


if __name__ == "__main__":
    start()

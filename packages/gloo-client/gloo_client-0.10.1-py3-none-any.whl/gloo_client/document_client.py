import typing
from urllib.parse import urljoin
import requests
from gloo_client.model import (
    DocumentResponse,
    UpdateDocumentRequest,
    CreateDocumentRequest,
    EmbeddingType,
    DocumentContent,
    DocumentAnnotation,
)
from gloo_client.base_client import GlooBaseClient


class DocumentClient(GlooBaseClient):
    def __init__(self, *, base: GlooBaseClient, app_id: str):
        super().__init__(
            origin=urljoin(base.origin, f"app/{app_id}/document"),
            app_secret=base.app_secret,
        )

    def create(
        self,
        *,
        name: str,
        source: str,
        content: typing.Union[str, typing.List[str]],
        annotations: typing.Optional[typing.List[DocumentAnnotation]],
        tags: typing.Optional[typing.List[str]] = None,
    ) -> DocumentResponse:
        c = (
            DocumentContent.factory.text(content)
            if isinstance(content, str)
            else DocumentContent.factory.chunks(content)
            if isinstance(content, list)
            else None
        )

        return DocumentResponse.parse_raw(
            self._post(
                "",
                data=CreateDocumentRequest(
                    tags=tags or [],
                    name=name,
                    source=source,
                    content=c,
                    annotations=annotations,
                ),
            ).text
        )

    def update(
        self,
        document_id: str,
        *,
        name: typing.Optional[str],
        source: typing.Optional[str],
        tags: typing.Optional[typing.List[str]],
        annotations: typing.Optional[typing.List[DocumentAnnotation]],
        content: typing.Optional[typing.Union[str, typing.List[str]]] = None,
    ) -> DocumentResponse:
        c = (
            DocumentContent.factory.text(content)
            if isinstance(content, str)
            else DocumentContent.factory.chunks(content)
            if isinstance(content, list)
            else None
        )

        return DocumentResponse.parse_raw(
            self._post(
                document_id,
                data=UpdateDocumentRequest(
                    name=name,
                    content=c,
                    source=source,
                    tags=tags,
                    annotations=annotations,
                ),
            ).text
        )

    def get(self, document_id: str) -> DocumentResponse:
        return DocumentResponse.parse_raw(self._get(document_id).text)

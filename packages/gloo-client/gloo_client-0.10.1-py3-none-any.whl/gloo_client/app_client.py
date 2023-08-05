import typing
from urllib.parse import urljoin
from gloo_client.model import (
    CreateAppRequest,
    EmbeddingType,
    AppResponse,
    UpdateAppRequest,
)
from gloo_client.base_client import GlooBaseClient


class AppClient(GlooBaseClient):
    def __init__(self, *, base: GlooBaseClient):
        super().__init__(
            origin=urljoin(base.origin, f"app"), app_secret=base.app_secret
        )

    def update(
        self,
        app_id: str,
        name: typing.Optional[str] = None,
        embeddings: typing.Optional[typing.List[EmbeddingType]] = None,
    ) -> AppResponse:
        return AppResponse.parse_raw(
            self._post(
                f"{app_id}", data=UpdateAppRequest(name=name, embeddings=embeddings)
            ).text
        )

    def get(self, app_id: str) -> AppResponse:
        return AppResponse.parse_raw(self._get(f"{app_id}").text)

    def create(self, name: str, embeddings: typing.List[EmbeddingType]) -> AppResponse:
        return AppResponse.parse_raw(
            self._post(
                "create", data=CreateAppRequest(name=name, embeddings=embeddings)
            ).text
        )

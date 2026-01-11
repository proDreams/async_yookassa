"""Base service class for all YooKassa services."""

import uuid
from abc import ABC
from typing import TYPE_CHECKING, Any

from pydantic import BaseModel

if TYPE_CHECKING:
    from async_yookassa._http import HttpClient


class BaseService(ABC):
    """Базовый класс для всех сервисов YooKassa API."""

    BASE_PATH: str = ""
    CMS_NAME: str = "async_yookassa_python"

    def __init__(self, http_client: HttpClient) -> None:
        self._http = http_client

    async def _get(
        self,
        path: str,
        query_params: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        """GET запрос."""
        return await self._http.request(
            method="GET",
            path=path,
            query_params=query_params,
        )

    async def _post(
        self,
        path: str,
        body: dict[str, Any] | None = None,
        idempotency_key: uuid.UUID | None = None,
    ) -> dict[str, Any]:
        """POST запрос с idempotency key."""
        headers = self._get_idempotency_headers(idempotency_key)
        return await self._http.request(
            method="POST",
            path=path,
            body=body,
            headers=headers,
        )

    @staticmethod
    def _get_idempotency_headers(
        idempotency_key: uuid.UUID | None,
    ) -> dict[str, str] | None:
        """Формирует заголовок Idempotence-Key."""
        if idempotency_key is None:
            idempotency_key = uuid.uuid4()
        return {"Idempotence-Key": str(idempotency_key)}

    @staticmethod
    def _serialize_request(request: BaseModel) -> dict[str, Any]:
        """Сериализует Pydantic модель в dict."""
        return request.model_dump(exclude_none=True)

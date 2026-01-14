"""Base service class for all YooKassa services."""

import uuid
from abc import ABC
from typing import TYPE_CHECKING, Any

from pydantic import BaseModel

if TYPE_CHECKING:
    from async_yookassa._http import HttpClient


class BaseService(ABC):
    """
    Базовый класс для всех сервисов YooKassa API.

    Обеспечивает базовую функциональность для выполнения HTTP запросов,
    работы с ключами идемпотентности и сериализации данных.
    """

    BASE_PATH: str = ""
    CMS_NAME: str = "async_yookassa_python"

    def __init__(self, http_client: HttpClient) -> None:
        self._http = http_client

    async def _get(
        self,
        path: str,
        query_params: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        """
        Выполнение GET запроса.

        :param path: Путь запроса
        :param query_params: Query параметры
        :return: JSON ответ
        """
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
        """
        Выполнение POST запроса с поддержкой идемпотентности.

        :param path: Путь запроса
        :param body: Тело запроса
        :param idempotency_key: Ключ идемпотентности (если не передан, генерируется новый)
        :return: JSON ответ
        """
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
        """
        Формирует заголовок Idempotence-Key.

        Если ключ не передан, генерирует новый UUIDv4.
        """
        if idempotency_key is None:
            idempotency_key = uuid.uuid4()
        return {"Idempotence-Key": str(idempotency_key)}

    @staticmethod
    def _serialize_request(request: BaseModel) -> dict[str, Any]:
        """
        Сериализует Pydantic модель запроса в словарь.

        Исключает поля со значением None.
        """
        return request.model_dump(exclude_none=True)

"""Receipt service for YooKassa API."""

import uuid
from typing import Any

from async_yookassa.models.receipt import ReceiptListOptions, ReceiptListResponse, ReceiptRequest, ReceiptResponse
from async_yookassa.services.base import BaseService


class ReceiptService(BaseService):
    """
    Сервис для работы с чеками.

    Использование:
    ```python
    async with YooKassaClient(...) as client:
        # Создание чека
        receipt = await client.receipt.create(ReceiptRequest(...))

        # Получение чека
        receipt = await client.receipt.find_one("receipt_id")

        # Список чеков
        receipts = await client.receipt.list()
    ```
    """

    BASE_PATH = "/receipts"

    async def find_one(self, receipt_id: str) -> ReceiptResponse:
        """
        Получение информации о чеке.

        :param receipt_id: Уникальный идентификатор чека
        :return: Объект ответа ReceiptResponse
        """
        if not isinstance(receipt_id, str):
            raise ValueError("Invalid receipt_id value")

        response = await self._get(f"{self.BASE_PATH}/{receipt_id}")
        return ReceiptResponse(**response)

    async def create(
        self, params: dict[str, Any] | ReceiptRequest, idempotency_key: uuid.UUID | None = None
    ) -> ReceiptResponse:
        """
        Создание чека.

        :param params: Параметры создания чека (словарь или объект ReceiptRequest)
        :param idempotency_key: Ключ идемпотентности (опционально)
        :return: Объект ответа ReceiptResponse
        """
        if isinstance(params, dict):
            body = params
        elif isinstance(params, ReceiptRequest):
            body = self._serialize_request(params)
        else:
            raise TypeError("Invalid params value type")

        response = await self._post(
            self.BASE_PATH,
            body=body,
            idempotency_key=idempotency_key,
        )
        return ReceiptResponse(**response)

    async def list(self, params: dict[str, Any] | ReceiptListOptions | None = None) -> ReceiptListResponse:
        """
        Получение списка чеков с фильтрацией.

        :param params: Параметры фильтрации (словарь или объект ReceiptListOptions)
        :return: Объект ответа ReceiptListResponse
        """

        if isinstance(params, ReceiptListOptions):
            params = params.model_dump(mode="json", by_alias=True, exclude_none=True)

        response = await self._get(self.BASE_PATH, query_params=params)
        return ReceiptListResponse(**response)

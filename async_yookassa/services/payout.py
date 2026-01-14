"""Payout service for YooKassa API."""

import uuid
from typing import Any

from async_yookassa.models.payout import (
    PayoutListOptions,
    PayoutListResponse,
    PayoutRequest,
    PayoutResponse,
    PayoutSearchOptions,
)
from async_yookassa.services.base import BaseService


class PayoutService(BaseService):
    """
    Сервис для работы с выплатами.

    Использование:
    ```python
    async with YooKassaClient(...) as client:
        # Создание выплаты
        payout = await client.payout.create(PayoutRequest(...))

        # Получение выплаты
        payout = await client.payout.find_one("payout_id")
    ```
    """

    BASE_PATH = "/payouts"

    async def find_one(self, payout_id: str) -> PayoutResponse:
        """
        Получение информации о выплате.

        :param payout_id: Уникальный идентификатор выплаты
        :return: Объект ответа PayoutResponse
        """

        if not isinstance(payout_id, str):
            raise ValueError("Invalid payout_id value")

        response = await self._get(f"{self.BASE_PATH}/{payout_id}")
        return PayoutResponse(**response)

    async def find(self, params: dict[str, Any] | PayoutSearchOptions | None = None) -> PayoutListResponse:
        """
        Поиск выплат по реквизитам.

        :param params: Параметры поиска (словарь или объект PayoutSearchOptions)
        :return: Объект ответа PayoutListResponse
        """

        if isinstance(params, PayoutSearchOptions):
            params = params.model_dump(mode="json", by_alias=True, exclude_none=True)

        response = await self._get(f"{self.BASE_PATH}/search", query_params=params)
        return PayoutListResponse(**response)

    async def create(
        self,
        params: dict[str, Any] | PayoutRequest,
        idempotency_key: uuid.UUID | None = None,
    ) -> PayoutResponse:
        """
        Создание выплаты.

        :param params: Параметры создания выплаты (словарь или объект PayoutRequest)
        :param idempotency_key: Ключ идемпотентности (опционально)
        :return: Объект ответа PayoutResponse
        """

        if isinstance(params, dict):
            body = params
        elif isinstance(params, PayoutRequest):
            body = self._serialize_request(params)
        else:
            raise TypeError("Invalid params value type")

        response = await self._post(
            self.BASE_PATH,
            body=body,
            idempotency_key=idempotency_key,
        )
        return PayoutResponse(**response)

    async def list(self, params: dict[str, Any] | PayoutListOptions | None = None) -> PayoutListResponse:
        """
        Получение списка выплат с фильтрацией.

        :param params: Параметры фильтрации (словарь или объект PayoutListOptions)
        :return: Объект ответа PayoutListResponse
        """

        if isinstance(params, PayoutListOptions):
            params = params.model_dump(mode="json", by_alias=True, exclude_none=True)

        response = await self._get(self.BASE_PATH, query_params=params)
        return PayoutListResponse(**response)

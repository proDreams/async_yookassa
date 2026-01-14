"""Deal service for YooKassa API."""

import uuid
from typing import Any

from async_yookassa.models.deal import DealListOptions, DealListResponse, DealRequest, DealResponse
from async_yookassa.services import BaseService


class DealService(BaseService):
    """
    Сервис для работы со сделками.

    Использование:
    ```python
    async with YooKassaClient(...) as client:
        # Создание сделки
        deal = await client.deal.create(DealRequest(...))

        # Получение сделки
        deal = await client.deal.find_one("deal_id")

        # Список сделок
        deals = await client.deal.list()
    ```
    """

    BASE_PATH = "/deals"

    async def find_one(self, deal_id: str) -> DealResponse:
        """
        Получение информации о сделке.

        :param deal_id: Уникальный идентификатор сделки
        :return: Объект ответа DealResponse
        """
        if not isinstance(deal_id, str):
            raise ValueError("Invalid deal_id value")

        response = await self._get(f"{self.BASE_PATH}/{deal_id}")
        return DealResponse(**response)

    async def create(
        self,
        params: dict[str, Any] | DealRequest,
        idempotency_key: uuid.UUID | None = None,
    ) -> DealResponse:
        """
        Создание сделки.

        :param params: Параметры создания сделки (словарь или объект DealRequest)
        :param idempotency_key: Ключ идемпотентности (опционально)
        :return: Объект ответа DealResponse
        """
        if isinstance(params, dict):
            request = DealRequest(**params)
        elif isinstance(params, DealRequest):
            request = params
        else:
            raise TypeError("Invalid params value type")

        body = self._serialize_request(request)

        response = await self._post(
            self.BASE_PATH,
            body=body,
            idempotency_key=idempotency_key,
        )
        return DealResponse(**response)

    async def list(
        self,
        params: dict[str, str] | DealListOptions | None = None,
    ) -> DealListResponse:
        """
        Получение списка сделок с фильтрацией.

        :param params: Параметры фильтрации (словарь или объект DealListOptions)
        :return: Объект ответа DealListResponse со списком сделок
        """

        if isinstance(params, DealListOptions):
            params = params.model_dump(mode="json", by_alias=True, exclude_none=True)

        response = await self._get(self.BASE_PATH, query_params=params)
        return DealListResponse(**response)

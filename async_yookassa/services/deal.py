"""Deal service for YooKassa API."""

import uuid
from typing import Any

from async_yookassa.models.deal_request import DealRequest
from async_yookassa.models.deal_response import DealListResponse, DealResponse
from async_yookassa.services.base import BaseService


class DealService(BaseService):
    """Сервис для работы со сделками."""

    BASE_PATH = "/deals"

    async def find_one(self, deal_id: str) -> DealResponse:
        """
        Возвращает информацию о сделке.

        :param deal_id: Уникальный идентификатор сделки
        :return: DealResponse
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

        :param params: Данные сделки
        :param idempotency_key: Ключ идемпотентности
        :return: DealResponse
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
        params: dict[str, str] | None = None,
    ) -> DealListResponse:
        """
        Возвращает список сделок.

        :param params: Параметры фильтрации
        :return: DealListResponse
        """
        response = await self._get(self.BASE_PATH, query_params=params)
        return DealListResponse(**response)

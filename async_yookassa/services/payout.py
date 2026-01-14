"""Payout service for YooKassa API."""

import uuid
from typing import Any

from async_yookassa.models.payout.request import (
    PayoutListOptions,
    PayoutListResponse,
    PayoutRequest,
    PayoutSearchOptions,
)
from async_yookassa.models.payout.response import PayoutResponse
from async_yookassa.services.base import BaseService


class PayoutService(BaseService):
    """Сервис для работы с выплатами."""

    BASE_PATH = "/payouts"

    async def find_one(self, payout_id: str) -> PayoutResponse:
        """
        Возвращает информацию о выплате.

        :param payout_id: Уникальный идентификатор выплаты
        :return: PayoutResponse
        """

        if not isinstance(payout_id, str):
            raise ValueError("Invalid payout_id value")

        response = await self._get(f"{self.BASE_PATH}/{payout_id}")
        return PayoutResponse(**response)

    async def find(self, params: dict[str, Any] | PayoutSearchOptions | None = None) -> PayoutListResponse:
        """
        placeholder
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

        :param params: Данные выплаты
        :param idempotency_key: Ключ идемпотентности
        :return: PayoutResponse
        """

        if isinstance(params, dict):
            request = PayoutRequest(**params)
        elif isinstance(params, PayoutRequest):
            request = params
        else:
            raise TypeError("Invalid params value type")

        body = self._serialize_request(request)

        response = await self._post(
            self.BASE_PATH,
            body=body,
            idempotency_key=idempotency_key,
        )
        return PayoutResponse(**response)

    async def list(self, params: dict[str, Any] | PayoutListOptions | None = None) -> PayoutListResponse:
        """
        placeholder
        """

        if isinstance(params, PayoutListOptions):
            params = params.model_dump(mode="json", by_alias=True, exclude_none=True)

        response = await self._get(self.BASE_PATH, query_params=params)
        return PayoutListResponse(**response)

"""Refund service for YooKassa API."""

import uuid
from typing import Any

from async_yookassa.models.refund_request import RefundRequest
from async_yookassa.models.refund_response import RefundListResponse, RefundResponse
from async_yookassa.services.base import BaseService


class RefundService(BaseService):
    """Сервис для работы с возвратами."""

    BASE_PATH = "/refunds"

    async def find_one(self, refund_id: str) -> RefundResponse:
        """
        Возвращает информацию о возврате.

        :param refund_id: Уникальный идентификатор возврата
        :return: RefundResponse
        """
        if not isinstance(refund_id, str):
            raise ValueError("Invalid refund_id value")

        response = await self._get(f"{self.BASE_PATH}/{refund_id}")
        return RefundResponse(**response)

    async def create(
        self,
        params: dict[str, Any] | RefundRequest,
        idempotency_key: uuid.UUID | None = None,
    ) -> RefundResponse:
        """
        Создание возврата.

        :param params: Данные возврата
        :param idempotency_key: Ключ идемпотентности
        :return: RefundResponse
        """
        if isinstance(params, dict):
            request = RefundRequest(**params)
        elif isinstance(params, RefundRequest):
            request = params
        else:
            raise TypeError("Invalid params value type")

        body = self._serialize_request(request)

        response = await self._post(
            self.BASE_PATH,
            body=body,
            idempotency_key=idempotency_key,
        )
        return RefundResponse(**response)

    async def list(
        self,
        params: dict[str, str] | None = None,
    ) -> RefundListResponse:
        """
        Возвращает список возвратов.

        :param params: Параметры фильтрации
        :return: RefundListResponse
        """
        response = await self._get(self.BASE_PATH, query_params=params)
        return RefundListResponse(**response)

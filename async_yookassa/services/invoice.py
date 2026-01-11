"""Invoice service for YooKassa API."""

import uuid
from typing import Any

from async_yookassa.models.invoice_request import InvoiceRequest
from async_yookassa.models.invoice_response import InvoiceListResponse, InvoiceResponse
from async_yookassa.services.base import BaseService


class InvoiceService(BaseService):
    """Сервис для работы со счетами."""

    BASE_PATH = "/invoices"

    async def find_one(self, invoice_id: str) -> InvoiceResponse:
        """
        Возвращает информацию о счёте.

        :param invoice_id: Уникальный идентификатор счёта
        :return: InvoiceResponse
        """
        if not isinstance(invoice_id, str):
            raise ValueError("Invalid invoice_id value")

        response = await self._get(f"{self.BASE_PATH}/{invoice_id}")
        return InvoiceResponse(**response)

    async def create(
        self,
        params: dict[str, Any] | InvoiceRequest,
        idempotency_key: uuid.UUID | None = None,
    ) -> InvoiceResponse:
        """
        Создание счёта.

        :param params: Данные счёта
        :param idempotency_key: Ключ идемпотентности
        :return: InvoiceResponse
        """
        if isinstance(params, dict):
            request = InvoiceRequest(**params)
        elif isinstance(params, InvoiceRequest):
            request = params
        else:
            raise TypeError("Invalid params value type")

        body = self._serialize_request(request)

        response = await self._post(
            self.BASE_PATH,
            body=body,
            idempotency_key=idempotency_key,
        )
        return InvoiceResponse(**response)

    async def cancel(
        self,
        invoice_id: str,
        idempotency_key: uuid.UUID | None = None,
    ) -> InvoiceResponse:
        """
        Отмена неоплаченного счёта.

        :param invoice_id: Уникальный идентификатор счёта
        :param idempotency_key: Ключ идемпотентности
        :return: InvoiceResponse
        """
        if not isinstance(invoice_id, str):
            raise ValueError("Invalid invoice_id value")

        response = await self._post(
            f"{self.BASE_PATH}/{invoice_id}/cancel",
            idempotency_key=idempotency_key,
        )
        return InvoiceResponse(**response)

    async def list(
        self,
        params: dict[str, str] | None = None,
    ) -> InvoiceListResponse:
        """
        Возвращает список счетов.

        :param params: Параметры фильтрации
        :return: InvoiceListResponse
        """
        response = await self._get(self.BASE_PATH, query_params=params)
        return InvoiceListResponse(**response)

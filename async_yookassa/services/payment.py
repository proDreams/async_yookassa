"""Payment service for YooKassa API."""

import uuid
from typing import Any

from async_yookassa.models.payment import (
    CapturePaymentRequest,
    PaymentListOptions,
    PaymentListResponse,
    PaymentRequest,
    PaymentResponse,
)
from async_yookassa.services.base import BaseService


class PaymentService(BaseService):
    """
    Сервис для работы с платежами.

    Использование:
    ```python
    async with YooKassaClient(...) as client:
        # Создание платежа
        payment = await client.payment.create(PaymentRequest(...))

        # Получение платежа
        payment = await client.payment.find_one("payment_id")

        # Подтверждение платежа
        payment = await client.payment.capture("payment_id")

        # Отмена платежа
        payment = await client.payment.cancel("payment_id")

        # Список платежей
        payments = await client.payment.list()
    ```
    """

    BASE_PATH = "/payments"

    async def find_one(self, payment_id: str) -> PaymentResponse:
        """
        Получение информации о платеже.

        :param payment_id: Уникальный идентификатор платежа
        :return: Объект ответа PaymentResponse
        """
        if not isinstance(payment_id, str):
            raise ValueError("Invalid payment_id value")

        response = await self._get(f"{self.BASE_PATH}/{payment_id}")
        return PaymentResponse(**response)

    async def create(
        self,
        params: dict[str, Any] | PaymentRequest,
        idempotency_key: uuid.UUID | None = None,
    ) -> PaymentResponse:
        """
        Создание платежа.

        :param params: Параметры создания платежа (словарь или объект PaymentRequest)
        :param idempotency_key: Ключ идемпотентности (опционально)
        :return: Объект ответа PaymentResponse
        """
        if isinstance(params, dict):
            request = PaymentRequest(**params)
        elif isinstance(params, PaymentRequest):
            request = params
        else:
            raise TypeError("Invalid params value type")

        request = self._add_cms_metadata(request)
        body = self._serialize_request(request)

        response = await self._post(
            self.BASE_PATH,
            body=body,
            idempotency_key=idempotency_key,
        )
        return PaymentResponse(**response)

    async def capture(
        self,
        payment_id: str,
        params: dict[str, Any] | CapturePaymentRequest | None = None,
        idempotency_key: uuid.UUID | None = None,
    ) -> PaymentResponse:
        """
        Подтверждение платежа.

        :param payment_id: Уникальный идентификатор платежа
        :param params: Параметры подтверждения (словарь или объект CapturePaymentRequest)
        :param idempotency_key: Ключ идемпотентности (опционально)
        :return: Объект ответа PaymentResponse
        """
        if not isinstance(payment_id, str):
            raise ValueError("Invalid payment_id value")

        body = None
        if params is not None:
            if isinstance(params, dict):
                request = CapturePaymentRequest(**params)
            elif isinstance(params, CapturePaymentRequest):
                request = params
            else:
                raise TypeError("Invalid params value type")
            body = self._serialize_request(request)

        response = await self._post(
            f"{self.BASE_PATH}/{payment_id}/capture",
            body=body,
            idempotency_key=idempotency_key,
        )
        return PaymentResponse(**response)

    async def cancel(
        self,
        payment_id: str,
        idempotency_key: uuid.UUID | None = None,
    ) -> PaymentResponse:
        """
        Отмена платежа.

        :param payment_id: Уникальный идентификатор платежа
        :param idempotency_key: Ключ идемпотентности (опционально)
        :return: Объект ответа PaymentResponse
        """
        if not isinstance(payment_id, str):
            raise ValueError("Invalid payment_id value")

        response = await self._post(
            f"{self.BASE_PATH}/{payment_id}/cancel",
            idempotency_key=idempotency_key,
        )
        return PaymentResponse(**response)

    async def list(
        self,
        params: dict[str, Any] | PaymentListOptions | None = None,
    ) -> PaymentListResponse:
        """
        Получение списка платежей с фильтрацией.

        :param params: Параметры фильтрации (словарь или объект PaymentListOptions)
        :return: Объект ответа PaymentListResponse со списком платежей
        """
        if isinstance(params, PaymentListOptions):
            params = params.model_dump(mode="json", by_alias=True, exclude_none=True)

        response = await self._get(self.BASE_PATH, query_params=params)
        return PaymentListResponse(**response)

    def _add_cms_metadata(self, request: PaymentRequest) -> PaymentRequest:
        """Добавляет информацию о CMS в метаданные платежа."""
        if request.metadata is None:
            request.metadata = {"cms_name": self.CMS_NAME}
        elif "cms_name" not in request.metadata:
            request.metadata["cms_name"] = self.CMS_NAME
        return request

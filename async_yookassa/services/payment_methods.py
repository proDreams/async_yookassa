"""Payment Methods service for YooKassa API."""

import uuid
from typing import Any

from async_yookassa.models.payment_method import PaymentMethodRequest, PaymentMethodResponse
from async_yookassa.services.base import BaseService


class PaymentMethodsService(BaseService):
    """
    Сервис для работы со способами оплаты.

    Использование:
    ```python
    async with YooKassaClient(...) as client:
        # Список способов оплаты
        methods = await client.payment_methods.list()

        # Получение конкретного способа
        method = await client.payment_methods.find_one("method_id")
    ```
    """

    BASE_PATH = "/payment_methods"

    async def find_one(self, payment_method_id: str) -> PaymentMethodResponse:
        """
        Получение информации о сохраненном способе оплаты.

        :param payment_method_id: Уникальный идентификатор способа оплаты
        :return: Объект ответа PaymentMethodResponse
        """
        if not isinstance(payment_method_id, str):
            raise ValueError("Invalid payment_method_id value")

        response = await self._get(f"{self.BASE_PATH}/{payment_method_id}")
        return PaymentMethodResponse(**response)

    async def create(
        self,
        params: dict[str, Any] | PaymentMethodRequest,
        idempotency_key: uuid.UUID | None = None,
    ) -> PaymentMethodResponse:
        """
        Создание (сохранение) способа оплаты.

        :param params: Параметры создания способа оплаты
        :param idempotency_key: Ключ идемпотентности
        :return: Объект ответа PaymentMethodResponse
        """
        if isinstance(params, dict):
            body = params
        elif isinstance(params, PaymentMethodRequest):
            body = self._serialize_request(request=params)
        else:
            raise TypeError("Invalid params value type")

        response = await self._post(
            self.BASE_PATH,
            body=body,
            idempotency_key=idempotency_key,
        )
        return PaymentMethodResponse(**response)

"""Payment Methods service for YooKassa API."""

import uuid
from typing import Any

from async_yookassa.models.payment_method import PaymentMethodRequest, PaymentMethodResponse
from async_yookassa.services.base import BaseService


class PaymentMethodsService(BaseService):
    """
    placeholder

    """

    BASE_PATH = "/payment_methods"

    async def find_one(self, payment_method_id: str) -> PaymentMethodResponse:
        """
        placeholder
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
        placeholder
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

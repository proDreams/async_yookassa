from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field

from async_yookassa.models.invoice_submodels.cart_model import Cart
from async_yookassa.models.invoice_submodels.delivery_method_model import DeliveryMethod
from async_yookassa.models.payment_request_model import PaymentData


class InvoiceRequest(BaseModel):
    payment_data: PaymentData
    cart: Cart
    delivery_method_data: DeliveryMethod
    expires_at: datetime
    locale: str | None = None
    description: str | None = Field(max_length=128, default=None)
    metadata: dict[str, Any] | None = None

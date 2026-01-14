from datetime import datetime
from typing import Any

from pydantic import Field

from async_yookassa.enums.payment import PaymentStatus
from async_yookassa.models.base import ModelConfigBase
from async_yookassa.models.invoice.cart import Cart
from async_yookassa.models.invoice.delivery_method import DeliveryMethodResponseUnion
from async_yookassa.models.invoice.invoice_cancellation_details import InvoiceCancellationDetails
from async_yookassa.models.invoice.payment_details import PaymentDetails


class InvoiceResponse(ModelConfigBase):
    id: str = Field(min_length=39, max_length=39)
    status: PaymentStatus
    cart: list[Cart]
    delivery_method: DeliveryMethodResponseUnion | None = None
    payment_details: PaymentDetails | None = None
    created_at: datetime
    expires_at: datetime | None = None
    description: str | None = Field(max_length=128, default=None)
    cancellation_details: InvoiceCancellationDetails | None = None
    metadata: dict[str, Any] | None = None

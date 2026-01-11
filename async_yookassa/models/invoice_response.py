from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict, Field

from async_yookassa.enums.payment import PaymentStatus
from async_yookassa.models.invoice_submodels.cart import Cart
from async_yookassa.models.invoice_submodels.delivery_method import DeliveryMethod
from async_yookassa.models.invoice_submodels.invoice_cancellation_details import (
    InvoiceCancellationDetails,
)
from async_yookassa.models.invoice_submodels.payment_details import PaymentDetails


class InvoiceResponse(BaseModel):
    id: str = Field(min_length=39, max_length=39)
    status: PaymentStatus
    cart: list[Cart]
    delivery_method: DeliveryMethod | None = None
    payment_details: PaymentDetails | None = None
    created_at: datetime
    expires_at: datetime | None = None
    description: str | None = Field(max_length=128, default=None)
    cancellation_details: InvoiceCancellationDetails | None = None
    metadata: dict[str, Any] | None = None

    model_config = ConfigDict(use_enum_values=True)


class InvoiceListResponse(BaseModel):
    type: str
    items: list[InvoiceResponse]
    next_cursor: str | None = None

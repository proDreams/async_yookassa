from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict, Field

from async_yookassa.enums.payment_response_enums import PaymentResponseStatusEnum
from async_yookassa.models.invoice_submodels.cart_model import Cart
from async_yookassa.models.invoice_submodels.delivery_method_model import DeliveryMethod
from async_yookassa.models.invoice_submodels.invoice_cancellation_details import (
    InvoiceCancellationDetails,
)
from async_yookassa.models.invoice_submodels.payment_details_model import PaymentDetails


class InvoiceResponse(BaseModel):
    id: str = Field(min_length=39, max_length=39)
    status: PaymentResponseStatusEnum
    cart: list[Cart]
    delivery_method: DeliveryMethod | None = None
    payment_details: PaymentDetails | None = None
    created_at: datetime
    expires_at: datetime | None = None
    description: str | None = Field(max_length=128, default=None)
    cancellation_details: InvoiceCancellationDetails | None = None
    metadata: dict[str, Any] | None = None

    model_config = ConfigDict(use_enum_values=True)

from datetime import datetime
from typing import Any, Literal

from pydantic import BaseModel, Field

from async_yookassa.enums.payment import PaymentStatus
from async_yookassa.models.base import ModelConfigBase
from async_yookassa.models.list_options_base import ListOptionsBase
from async_yookassa.models.payment.amount import Amount
from async_yookassa.models.payment.authorization_details import (
    AuthorizationDetails,
)
from async_yookassa.models.payment.cancellation_details import (
    CancellationDetails,
)
from async_yookassa.models.payment.confirmation import ConfirmationUnion
from async_yookassa.models.payment.deal import Deal
from async_yookassa.models.payment.invoice_details import InvoiceDetails
from async_yookassa.models.payment.methods.base import PaymentMethodUnion
from async_yookassa.models.payment.recipient import RecipientResponse
from async_yookassa.models.payment.transfers import TransferResponse


class PaymentResponse(ModelConfigBase):
    id: str = Field(min_length=36, max_length=36)
    status: PaymentStatus
    amount: Amount
    income_amount: Amount | None = None
    description: str | None = Field(max_length=128, default=None)
    recipient: RecipientResponse
    payment_method: PaymentMethodUnion | None = None
    captured_at: datetime | None = None
    created_at: datetime
    expires_at: datetime | None = None
    confirmation: ConfirmationUnion | None = None
    test: bool
    refunded_amount: Amount | None = None
    paid: bool
    refundable: bool
    receipt_registration: PaymentStatus | None = None
    metadata: dict[str, Any] | None = None
    cancellation_details: CancellationDetails | None = None
    authorization_details: AuthorizationDetails | None = None
    transfers: list[TransferResponse] | None = None
    deal: Deal | None = None
    merchant_customer_id: str | None = Field(max_length=200, default=None)
    invoice_details: InvoiceDetails | None = None


class PaymentListOptions(ListOptionsBase):
    captured_at_gte: datetime | None = Field(default=None, serialization_alias="captured_at.gte")
    captured_at_gt: datetime | None = Field(default=None, serialization_alias="captured_at.gt")
    captured_at_lte: datetime | None = Field(default=None, serialization_alias="captured_at.lte")
    captured_at_lt: datetime | None = Field(default=None, serialization_alias="captured_at.lt")
    payment_method: str | None = None
    status: Literal["pending", "waiting_for_capture", "succeeded", "canceled"] | None = None


class PaymentListResponse(BaseModel):
    type: str
    items: list[PaymentResponse]
    next_cursor: str | None = None

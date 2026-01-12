from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from async_yookassa.enums.payment import PaymentStatus
from async_yookassa.models.payment.amount import Amount
from async_yookassa.models.payment.cancellation_details import RefundDetails
from async_yookassa.models.payment.deal import DealRefund
from async_yookassa.models.payment.methods.base import PaymentMethodRefund
from async_yookassa.models.payment.transfers import TransferBase


class RefundResponse(BaseModel):
    id: str = Field(min_length=36, max_length=36)
    payment_id: str = Field(min_length=36, max_length=36)
    status: PaymentStatus
    cancellation_details: RefundDetails | None = None
    receipt_registration: PaymentStatus | None = None
    created_at: datetime
    amount: Amount
    description: str | None = Field(max_length=250, default=None)
    sources: list[TransferBase] | None = None
    deal: DealRefund | None = None
    refund_method: PaymentMethodRefund | None = None

    model_config = ConfigDict(use_enum_values=True)


class RefundListResponse(BaseModel):
    type: str
    items: list[RefundResponse]
    next_cursor: str | None = None

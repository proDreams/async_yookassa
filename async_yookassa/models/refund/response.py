from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field

from async_yookassa.enums.payment import PaymentStatus
from async_yookassa.models.base import ModelConfigBase
from async_yookassa.models.payment.amount import Amount
from async_yookassa.models.payment.cancellation_details import CancellationDetails
from async_yookassa.models.payment.deal import DealRefund
from async_yookassa.models.payment.methods.base import PaymentMethodRefundUnion
from async_yookassa.models.payment.transfers import TransferBase


class RefundAuthorizationDetails(ModelConfigBase):
    rrn: str | None = None


class RefundResponse(ModelConfigBase):
    id: str = Field(min_length=36, max_length=36)
    payment_id: str = Field(min_length=36, max_length=36)
    status: PaymentStatus
    cancellation_details: CancellationDetails | None = None
    receipt_registration: PaymentStatus | None = None
    created_at: datetime
    amount: Amount
    description: str | None = Field(max_length=250, default=None)
    sources: list[TransferBase] | None = None
    deal: DealRefund | None = None
    refund_method: PaymentMethodRefundUnion | None = None
    refund_authorization_details: RefundAuthorizationDetails | None = None
    metadata: dict[str, Any] | None = None


class RefundListResponse(BaseModel):
    type: str
    items: list[RefundResponse]
    next_cursor: str | None = None

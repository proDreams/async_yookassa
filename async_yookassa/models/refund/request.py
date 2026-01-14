from typing import Any, Literal

from pydantic import BaseModel, Field

from async_yookassa.models.list_options_base import ListOptionsBase
from async_yookassa.models.payment.amount import Amount
from async_yookassa.models.payment.deal import DealRefund
from async_yookassa.models.payment.methods.base import ElectronicCertificatePaymentMethodRefund
from async_yookassa.models.payment.receipts.base import Receipt
from async_yookassa.models.payment.transfers import TransferBase


class RefundRequest(BaseModel):
    payment_id: str = Field(min_length=36, max_length=36)
    amount: Amount
    description: str | None = Field(max_length=250, default=None)
    receipt: Receipt | None = None
    sources: list[TransferBase] | None = None
    deal: DealRefund | None = None
    refund_method_data: ElectronicCertificatePaymentMethodRefund | None = None
    metadata: dict[str, Any] | None = None


class RefundListOptions(ListOptionsBase):
    payment_id: str | None = None
    status: Literal["pending", "succeeded", "canceled"] | None = None

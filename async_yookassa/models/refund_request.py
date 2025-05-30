from pydantic import BaseModel, Field

from async_yookassa.models.payment_submodels.amount import Amount
from async_yookassa.models.payment_submodels.deal import DealRefund
from async_yookassa.models.payment_submodels.payment_method import PaymentMethodRefund
from async_yookassa.models.payment_submodels.receipt import Receipt
from async_yookassa.models.payment_submodels.transfers import TransferBase


class RefundRequest(BaseModel):
    payment_id: str = Field(min_length=36, max_length=36)
    amount: Amount
    description: str | None = Field(max_length=250, default=None)
    receipt: Receipt | None = None
    sources: list[TransferBase] | None = None
    deal: DealRefund | None = None
    refund_method_data: PaymentMethodRefund | None = None

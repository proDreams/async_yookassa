from typing import Any

from pydantic import BaseModel, Field

from async_yookassa.models.payment_submodels.amount import Amount
from async_yookassa.models.payment_submodels.deal import DealBase
from async_yookassa.models.payout_submodels.payout_destination_data import (
    PayoutDestination,
)
from async_yookassa.models.payout_submodels.receipt_data import ReceiptData


class PayoutRequest(BaseModel):
    amount: Amount
    payout_destination_data: PayoutDestination | None = None
    payout_token: str | None = None
    payment_method_id: str | None = None
    description: str | None = Field(max_length=128, default=None)
    deal: DealBase | None = None
    self_employed: DealBase | None = None
    receipt_data: ReceiptData | None = None
    personal_data: list[DealBase] | None = None
    metadata: dict[str, Any] | None = None

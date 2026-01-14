from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field

from async_yookassa.enums.payment import PaymentStatus
from async_yookassa.models.payment.amount import Amount
from async_yookassa.models.payment.cancellation_details import CancellationDetails
from async_yookassa.models.payment.deal import DealBase
from async_yookassa.models.payout.payout_destination import PayoutDestinationUnion
from async_yookassa.models.payout.receipt_data import ReceiptDataResponse


class PayoutResponse(BaseModel):
    id: str = Field(min_length=36, max_length=50)
    amount: Amount
    status: PaymentStatus
    payout_destination: PayoutDestinationUnion
    description: str | None = Field(max_length=128, default=None)
    created_at: datetime
    succeeded_at: datetime | None = None
    deal: DealBase | None = None
    self_employed: DealBase | None = None
    receipt: ReceiptDataResponse | None = None
    cancellation_details: CancellationDetails | None = None
    metadata: dict[str, Any] | None = None
    test: bool

from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field

from async_yookassa.enums.payment_response import ReceiptRegistrationEnum
from async_yookassa.models.payment_submodels.amount import Amount
from async_yookassa.models.payment_submodels.cancellation_details import PayoutDetails
from async_yookassa.models.payment_submodels.deal import DealBase
from async_yookassa.models.payout_submodels.payout_destination_data import (
    PayoutDestinationResponse,
)
from async_yookassa.models.payout_submodels.receipt_data import ReceiptDataResponse


class PayoutResponse(BaseModel):
    id: str = Field(min_length=36, max_length=50)
    amount: Amount
    status: ReceiptRegistrationEnum
    payout_destination: PayoutDestinationResponse
    description: str | None = Field(max_length=128, default=None)
    created_at: datetime
    deal: DealBase | None = None
    self_employed: DealBase | None = None
    receipt: ReceiptDataResponse | None = None
    cancellation_details: PayoutDetails | None = None
    metadata: dict[str, Any] | None = None
    test: bool

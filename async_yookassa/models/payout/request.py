from typing import Any

from pydantic import BaseModel, Field

from async_yookassa.models.list_options_base import ListOptionsBase
from async_yookassa.models.payment.amount import Amount
from async_yookassa.models.payment.deal import DealBase
from async_yookassa.models.payout.payout_destination import PayoutDestinationRequestUnion
from async_yookassa.models.payout.response import PayoutResponse


class PayoutRequest(BaseModel):
    amount: Amount
    payout_destination_data: PayoutDestinationRequestUnion | None = None
    payout_token: str | None = None
    payment_method_id: str | None = None
    description: str | None = Field(max_length=128, default=None)
    deal: DealBase | None = None
    personal_data: list[DealBase] | None = None
    metadata: dict[str, Any] | None = None


class PayoutListOptions(ListOptionsBase):
    payout_destination_type: str | None = Field(default=None, serialization_alias="payout_destination.type")


class PayoutSearchOptions(ListOptionsBase):
    metadata: dict[str, Any] | None = None


class PayoutListResponse(BaseModel):
    type: str
    items: list[PayoutResponse]
    next_cursor: str | None = None

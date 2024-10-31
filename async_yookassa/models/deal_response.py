from datetime import datetime

from pydantic import BaseModel, ConfigDict

from async_yookassa.enums.deal_enums import DealStatusEnum
from async_yookassa.models.deal_request import DealRequest
from async_yookassa.models.payment_submodels.amount import Amount


class DealResponse(DealRequest):
    id: str
    balance: Amount
    payout_balance: Amount
    status: DealStatusEnum
    created_at: datetime
    expires_at: datetime
    test: bool

    model_config = ConfigDict(use_enum_values=True)


class DealListResponse(BaseModel):
    type: str
    items: list[DealResponse]
    next_cursor: str | None = None

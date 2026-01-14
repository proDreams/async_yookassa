from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field

from async_yookassa.enums.deal_enums import DealFeeMomentEnum, DealStatusEnum, DealTypeEnum
from async_yookassa.models.base import ModelConfigBase
from async_yookassa.models.payment.amount import Amount


class DealResponse(ModelConfigBase):
    type: DealTypeEnum
    id: str
    fee_moment: DealFeeMomentEnum
    description: str | None = Field(max_length=128, default=None)
    balance: Amount
    payout_balance: Amount
    status: DealStatusEnum
    created_at: datetime
    expires_at: datetime
    metadata: dict[str, Any] | None = None
    test: bool


class DealListResponse(BaseModel):
    type: str
    items: list[DealResponse]
    next_cursor: str | None = None

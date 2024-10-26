from typing import Any

from pydantic import BaseModel, Field

from async_yoomoney.models.payment_submodels.amount_model import Amount


class Transfers(BaseModel):
    account_id: str
    amount: Amount
    platform_fee_amount: Amount
    description: str | None = Field(max_length=128)
    metadata: dict[str, Any] | None = None

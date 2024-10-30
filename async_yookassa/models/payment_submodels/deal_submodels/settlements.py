from pydantic import BaseModel, Field

from async_yookassa.models.payment_submodels.amount import Amount


class Settlement(BaseModel):
    type: str = Field(default="payout")
    amount: Amount

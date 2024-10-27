from pydantic import BaseModel, Field

from async_yookassa.models.payment_submodels.amount_model import Amount


class Settlement(BaseModel):
    type: str = Field(default="payout")
    amount: Amount

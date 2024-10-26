from pydantic import BaseModel

from async_yoomoney.models.payment_submodels.amount_model import Amount


class Settlement(BaseModel):
    type: str = "payout"
    amount: Amount

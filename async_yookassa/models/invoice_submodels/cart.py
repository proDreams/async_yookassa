from pydantic import BaseModel, Field

from async_yookassa.models.payment_submodels.amount import Amount


class Cart(BaseModel):
    description: str = Field(min_length=1, max_length=128)
    price: Amount
    discount_price: Amount | None = None
    quantity: int | float

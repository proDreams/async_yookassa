from typing import Any

from pydantic import BaseModel, Field

from async_yookassa.models.payment_submodels.amount_model import Amount


class Articles(BaseModel):
    article_number: int = Field(le=999)
    tru_code: str = Field(min_length=30, max_length=30)
    article_code: str | None = Field(max_length=128)
    article_name: str = Field(max_length=128)
    quantity: int
    price: Amount
    metadata: dict[str, Any]

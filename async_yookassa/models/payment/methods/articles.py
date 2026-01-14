from pydantic import BaseModel, Field

from async_yookassa.models.payment.methods.electronic_certificate import (
    Certificate,
)


class ArticleBase(BaseModel):
    article_number: int = Field(ge=1, le=999)
    tru_code: str = Field(min_length=30, max_length=30)
    article_code: str | None = Field(max_length=128, default=None)


class ArticleResponse(ArticleBase):
    certificates: list[Certificate]


class ArticleRefund(ArticleBase):
    payment_article_number: int = Field(ge=1, le=999)
    quantity: int = Field(ge=1)

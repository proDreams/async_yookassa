import re

from pydantic import BaseModel, ConfigDict, Field, field_validator

from async_yookassa.enums.card import CardTypeEnum, SourceEnum
from async_yookassa.models.payment_submodels.payment_method_submodels.card_product import (
    CardProduct,
)


class CardBase(BaseModel):
    number: str


class CardRequest(CardBase):
    expiry_year: str
    expiry_month: str
    cardholder: str | None = None
    csc: str | None = None


class CardResponse(BaseModel):
    first6: str | None = None
    last4: str
    expiry_year: str
    expiry_month: str
    card_type: CardTypeEnum
    card_product: CardProduct | None = None
    issuer_country: str | None = Field(min_length=2, max_length=2, default=None)
    issuer_name: str | None = None
    source: SourceEnum | None = None

    model_config = ConfigDict(use_enum_values=True)

    @field_validator("first6", mode="before")
    def validate_first6(cls, value: str) -> str:
        if not re.match("^[0-9]{6}$", value):
            raise ValueError("Invalid first6 value")

        return value

    @field_validator("last4", mode="before")
    def validate_last4(cls, value: str) -> str:
        if not re.match(r"^\d{4}$", value):
            raise ValueError("Invalid last4 value")

        return value

    @field_validator("expiry_year", mode="before")
    def validate_expiry_year(cls, value: str) -> str:
        if not re.match(r"^\d\d\d\d$", value) and 2000 < int(value) < 2200:
            raise ValueError("Invalid card expiry year value")

        return value

    @field_validator("expiry_month", mode="before")
    def validate_expiry_month(cls, value: str) -> str:
        if not re.match(r"^\d\d$", value) and 0 < int(value) <= 12:
            raise ValueError("Invalid card expiry month value")

        return value

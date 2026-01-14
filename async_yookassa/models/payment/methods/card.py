import re

from pydantic import BaseModel, Field, field_validator

from async_yookassa.enums.payment import CardSource, CardType
from async_yookassa.models.base import ModelConfigBase
from async_yookassa.models.payment.methods.card_product import (
    CardProduct,
)


class CardBase(BaseModel):
    number: str

    @field_validator("number", mode="before")
    def validate_number(cls, value: str) -> str:
        if not re.match("^[0-9]{14,19}$", value):
            raise ValueError("Invalid card number value")

        return value


class CardRequest(CardBase):
    expiry_year: str
    expiry_month: str
    cardholder: str | None = None
    csc: str | None = None

    @field_validator("expiry_year", mode="before")
    def validate_expiry_year(cls, value: str) -> str:
        if not re.match("^[0-9]{4}$", value):
            raise ValueError("Invalid expiry year value")

        return value

    @field_validator("expiry_month", mode="before")
    def validate_expiry_month(cls, value: str) -> str:
        if not re.match("^[0-9]{2}$", value):
            raise ValueError("Invalid expiry month value")

        return value

    @field_validator("cardholder", mode="before")
    def validate_cardholder(cls, value: str | None) -> str | None:
        if value is None:
            return None

        if not re.match("^[a-zA-Z '-]{0,26}$", value):
            raise ValueError("Invalid cardholder value")

        return value

    @field_validator("csc", mode="before")
    def validate_csc(cls, value: str | None) -> str | None:
        if value is None:
            return None

        if not re.match("^[0-9]{3,4}$", value):
            raise ValueError("Invalid csc value")

        return value


class CardResponseBase(ModelConfigBase):
    first6: str | None = None
    last4: str
    card_type: CardType
    issuer_country: str | None = Field(min_length=2, max_length=2, default=None)
    issuer_name: str | None = None

    @field_validator("first6", mode="before")
    def validate_first6(cls, value: str | None) -> str | None:
        if value is None:
            return None

        if not re.match("^[0-9]{6}$", value):
            raise ValueError("Invalid first6 value")

        return value

    @field_validator("last4", mode="before")
    def validate_last4(cls, value: str) -> str:
        if not re.match(r"^\d{4}$", value):
            raise ValueError("Invalid last4 value")

        return value


class CardResponse(CardResponseBase):
    expiry_year: str
    expiry_month: str
    card_product: CardProduct | None = None
    source: CardSource | None = None

    @field_validator("expiry_year", mode="before")
    def validate_expiry_year(cls, value: str) -> str:
        if not re.match(r"^\d{4}$", value) and 2000 < int(value) < 2200:
            raise ValueError("Invalid card expiry year value")

        return value

    @field_validator("expiry_month", mode="before")
    def validate_expiry_month(cls, value: str) -> str:
        if not re.match(r"^\d{2}$", value) and 0 < int(value) <= 12:
            raise ValueError("Invalid card expiry month value")

        return value

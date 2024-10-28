from decimal import ROUND_HALF_UP, Decimal
from typing import Any

from pydantic import BaseModel, field_validator


class Amount(BaseModel):
    value: str
    currency: str

    @field_validator("value", mode="before")
    def validate_value(cls, value: Any) -> str:
        """
        Устанавливает value модели Amount.

        :param value: value модели Amount.
        :type value: Decimal
        """
        return str(Decimal(str(float(value))).quantize(Decimal("1.11"), rounding=ROUND_HALF_UP))

    @field_validator("currency", mode="before")
    def validate_currency(cls, value: str) -> str:
        """
        Устанавливает currency модели Amount.

        :param value: currency модели Amount.
        :type value: str
        """
        if not isinstance(value, str):
            raise ValueError("currency must be a string")

        if len(value) != 3:
            raise ValueError("currency must be 3 characters long")

        return value.upper()

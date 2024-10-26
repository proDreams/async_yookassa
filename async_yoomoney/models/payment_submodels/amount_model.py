from decimal import ROUND_HALF_UP, Decimal
from typing import Any

from pydantic import BaseModel, field_validator


class Amount(BaseModel):
    value: Decimal
    currency: str

    @field_validator("value", mode="before")
    def validate_value(cls, value: Any) -> Decimal:
        """
        Устанавливает value модели Amount.

        :param value: value модели Amount.
        :type value: Decimal
        """
        return Decimal(str(float(value))).quantize(Decimal("1.11"), rounding=ROUND_HALF_UP)

    @field_validator("currency", mode="before")
    def validate_currency(cls, value: Any) -> str:
        """
        Устанавливает currency модели Amount.

        :param value: currency модели Amount.
        :type value: str
        """
        value = str(value).upper()

        if len(value) != 3:
            raise ValueError("currency must be 3 characters long")

        return value

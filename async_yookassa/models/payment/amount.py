from decimal import ROUND_HALF_UP, Decimal
from typing import Any

from pydantic import BaseModel, field_validator, model_validator


class Amount(BaseModel):
    value: str
    currency: str

    @field_validator("currency", mode="before")
    def validate_currency(cls, value: Any) -> str:
        if not isinstance(value, str):
            raise ValueError("currency must be a string")
        if len(value) != 3:
            raise ValueError("currency must be 3 characters long")
        return value.upper()

    @field_validator("value", mode="before")
    def pre_validate_value(cls, value: Any) -> str:
        """
        Предварительная очистка value.
        Преобразуем все в строку сразу, избегая float.
        """
        return str(value)

    @model_validator(mode="after")
    def format_value_based_on_currency(self):
        """
        Форматирует value в зависимости от currency.
        """
        zero_precision = {"JPY", "KRW", "CLP", "HUF", "VND"}
        three_precision = {"BHD", "KWD", "OMR", "JOD", "TND"}

        scale = 2

        if self.currency in zero_precision:
            scale = 0
        elif self.currency in three_precision:
            scale = 3

        exp_template = Decimal("1").scaleb(-scale)

        try:
            d_val = Decimal(self.value)
            quantized_val = d_val.quantize(exp_template, rounding=ROUND_HALF_UP)

            self.value = str(quantized_val)

        except Exception:
            raise ValueError(f"Invalid decimal value: {self.value}")

        return self

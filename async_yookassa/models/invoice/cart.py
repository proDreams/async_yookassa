from decimal import Decimal, InvalidOperation
from typing import Any

from pydantic import BaseModel, ConfigDict, Field, field_validator

from async_yookassa.models.payment.amount import Amount


class Cart(BaseModel):
    description: str = Field(min_length=1, max_length=128)
    price: Amount
    discount_price: Amount | None = None
    quantity: int

    model_config = ConfigDict(json_encoders={Decimal: float})

    @field_validator("quantity", mode="before")
    def validate_quantity(cls, value: Any) -> Decimal:
        """
        Валидация количества.
        Возвращает Decimal, который в JSON станет number (числом).
        """
        try:
            d_val = Decimal(str(value))
        except (InvalidOperation, ValueError, TypeError):
            raise ValueError("Quantity must be a valid number")

        if not d_val.is_finite():
            raise ValueError("Quantity must be a finite number")

        if d_val <= 0:
            raise ValueError("Quantity must be greater than 0")

        normalized = d_val.normalize()
        exponent = normalized.as_tuple().exponent

        if isinstance(exponent, int):
            if exponent < -3:
                raise ValueError("Quantity allows max 3 decimal places")

        return normalized

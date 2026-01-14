import re
from decimal import ROUND_HALF_UP, Decimal, InvalidOperation
from typing import Any

from pydantic import ConfigDict, Field, field_validator

from async_yookassa.enums.agent_type import AgentTypeEnum
from async_yookassa.enums.item_measure import ItemMeasureEnum
from async_yookassa.enums.payment_subject import PaymentModeEnum, PaymentSubjectEnum
from async_yookassa.models.base import ModelConfigBase
from async_yookassa.models.payment.amount import Amount
from async_yookassa.models.payment.receipts.mark_code_info import (
    MarkCodeInfo,
)
from async_yookassa.models.payment.receipts.mark_quantity import (
    MarkQuantity,
)
from async_yookassa.models.payment.receipts.payment_subject_industry_details import (
    PaymentSubjectIndustryDetails,
)
from async_yookassa.models.receipt.supplier import Supplier


class ReceiptItemBase(ModelConfigBase):
    description: str = Field(max_length=128)
    amount: Amount
    vat_code: int = Field(ge=1, le=12)
    quantity: str
    measure: ItemMeasureEnum | None = None
    mark_quantity: MarkQuantity | None = None
    payment_subject: PaymentSubjectEnum | None = None
    payment_mode: PaymentModeEnum | None = None
    country_of_origin_code: str | None = Field(min_length=2, max_length=2, default=None)
    customs_declaration_number: str | None = Field(max_length=32, default=None)
    excise: str | None = None
    product_code: str | None = None
    planned_status: int | None = Field(ge=1, le=6, default=None)
    mark_code_info: MarkCodeInfo | None = None
    mark_mode: str | None = None
    payment_subject_industry_details: PaymentSubjectIndustryDetails | None = None

    @field_validator("quantity", mode="before")
    def validate_quantity(cls, value: Any) -> str:
        """
        Валидация количества.
        Лимиты: макс 99999.999, до 3 знаков после точки.
        """
        try:
            d_val = Decimal(str(value))
        except (InvalidOperation, ValueError, TypeError):
            raise ValueError("Quantity must be a valid number")

        if d_val <= 0:
            raise ValueError("Quantity must be greater than 0")

        if d_val > Decimal("99999.999"):
            raise ValueError("Quantity exceeds maximum limit of 99999.999")

        normalized = d_val.normalize()
        exponent = normalized.as_tuple().exponent

        if isinstance(exponent, int):
            if exponent < -3:
                raise ValueError("Quantity allows max 3 decimal places")

        return f"{normalized:f}"

    @field_validator("excise", mode="before")
    def validate_excise(cls, value: Any) -> str | None:
        """
        Устанавливает excise (Тег 1229).
        Десятичное число с точностью до 2 знаков после точки.
        """
        if value is None:
            return None

        try:
            d_val = Decimal(str(value))
        except (InvalidOperation, ValueError, TypeError):
            raise ValueError("Excise must be a valid number")

        if d_val < 0:
            raise ValueError("Excise cannot be negative")

        quantized = d_val.quantize(Decimal("1.00"), rounding=ROUND_HALF_UP)

        return str(quantized)

    @field_validator("mark_mode", mode="before")
    def mark_mode_validator(cls, value: str) -> str:
        """
        Устанавливает mark_mode модели ReceiptItem.

        :param value: mark_mode модели ReceiptItem.
        :type value: str
        """
        if not re.search(r"^0$", value):
            raise ValueError(r"Invalid value for `mark_mode`, must be a follow pattern or equal to `/^0$/`")

        return value


class ReceiptItem(ReceiptItemBase):
    supplier: Supplier | None = None
    agent_type: AgentTypeEnum | None = None

    model_config = ConfigDict(use_enum_values=True)

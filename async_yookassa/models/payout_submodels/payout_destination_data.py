from typing import Any

from pydantic import BaseModel, ConfigDict, Field, model_validator

from async_yookassa.enums.payout import PayoutTypeEnum
from async_yookassa.models.payment_submodels.payment_method_submodels.card import (
    CardBase,
)


class PayoutDestinationBase(BaseModel):
    type: PayoutTypeEnum
    card: CardBase | None = None
    bank_id: str | None = Field(max_length=12, default=None)
    phone: str | None = None
    account_number: str | None = Field(min_length=11, max_length=33, default=None)

    model_config = ConfigDict(use_enum_values=True)


class PayoutDestination(PayoutDestinationBase):

    @model_validator(mode="before")
    def validate_required_fields(cls, values: dict[str, Any]) -> dict[str, Any]:
        type_value = values.get("type")

        if type_value == PayoutTypeEnum.bank_card:
            if not values.get("card"):
                raise ValueError("Field 'card' is required for type 'bank_card'")

        elif type_value == PayoutTypeEnum.sbp:
            if not values.get("bank_id"):
                raise ValueError("Field 'bank_id' are required for type 'sbp'")
            if not values.get("phone"):
                raise ValueError("Field 'phone' are required for type 'sbp'")

        elif type_value == PayoutTypeEnum.yoo_money:
            if not values.get("account_number"):
                raise ValueError("Field 'account_number' is required for type 'yoo_money'")

        return values


class PayoutDestinationResponse(PayoutDestinationBase):
    recipient_checked: bool | None = None

    @model_validator(mode="before")
    def validate_required_fields(cls, values: dict[str, Any]) -> dict[str, Any]:
        type_value = values.get("type")

        if type_value == PayoutTypeEnum.sbp:
            if not values.get("bank_id"):
                raise ValueError("Field 'bank_id' are required for type 'sbp'")
            if not values.get("phone"):
                raise ValueError("Field 'phone' are required for type 'sbp'")
            if not values.get("recipient_checked"):
                raise ValueError("Field 'recipient_checked' are required for type 'sbp'")

        elif type_value == PayoutTypeEnum.yoo_money:
            if not values.get("account_number"):
                raise ValueError("Field 'account_number' is required for type 'yoo_money'")

        return values

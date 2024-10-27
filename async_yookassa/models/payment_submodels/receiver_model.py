from enum import Enum

from pydantic import BaseModel, Field, model_validator


class TypeEnum(str, Enum):
    bank_account = "bank_account"
    mobile_balance = "mobile_balance"
    digital_wallet = "digital_wallet"


class Receiver(BaseModel):
    type: TypeEnum
    account_number: str | None = Field(min_length=20, max_length=20, default=None)
    bic: str | None = Field(min_length=9, max_length=9, default=None)
    phone: str | None = Field(min_length=11, max_length=15, default=None)

    @model_validator(mode="before")
    def validate_required_fields(cls, values):
        type_value = values.get("type")

        if type_value == TypeEnum.bank_account:
            if not values.get("account_number"):
                raise ValueError("Field 'account_number' is required for type 'bank_account'")
            if not values.get("bic"):
                raise ValueError("Field 'bic' is required for type 'bank_account'")

        elif type_value == TypeEnum.mobile_balance:
            if not values.get("phone"):
                raise ValueError("Field 'phone' are required for type 'mobile_balance'")

        elif type_value == TypeEnum.digital_wallet:
            if not values.get("account_number"):
                raise ValueError("Field 'account_number' are required for type 'digital_wallet'")

        return values

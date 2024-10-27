from enum import Enum

from pydantic import BaseModel, model_validator

from async_yookassa.models.payment_submodels.amount_model import Amount


class TypeEnum(str, Enum):
    untaxed = "untaxed"
    calculated = "calculated"
    mixed = "mixed"


class VatData(BaseModel):
    type: TypeEnum
    amount: Amount | None = None
    rate: str | None = None

    @model_validator(mode="before")
    def validate_required_fields(cls, values):
        type_value = values.get("type")

        if type_value == TypeEnum.calculated:
            if not values.get("amount"):
                raise ValueError("Field 'payment_purpose' are required for type 'calculated'")
            if not values.get("rate"):
                raise ValueError("Field 'vat_data' are required for type 'calculated'")
        elif type_value == TypeEnum.mixed:
            if not values.get("amount"):
                raise ValueError("Field 'payment_purpose' are required for type 'mixed'")

        return values

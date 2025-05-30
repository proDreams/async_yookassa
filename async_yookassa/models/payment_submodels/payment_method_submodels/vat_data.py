from pydantic import BaseModel, ConfigDict, model_validator

from async_yookassa.enums.vat_data import RateEnum, VatDataTypeEnum
from async_yookassa.models.payment_submodels.amount import Amount


class VatData(BaseModel):
    type: VatDataTypeEnum
    amount: Amount | None = None
    rate: RateEnum | None = None

    model_config = ConfigDict(use_enum_values=True)

    @model_validator(mode="before")
    def validate_required_fields(cls, values):
        type_value = values.get("type")

        if type_value == VatDataTypeEnum.calculated:
            if not values.get("amount"):
                raise ValueError("Field 'payment_purpose' are required for type 'calculated'")
            if not values.get("rate"):
                raise ValueError("Field 'vat_data' are required for type 'calculated'")
        elif type_value == VatDataTypeEnum.mixed:
            if not values.get("amount"):
                raise ValueError("Field 'payment_purpose' are required for type 'mixed'")

        return values

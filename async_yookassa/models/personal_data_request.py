from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict, model_validator

from async_yookassa.enums.personal_data_enums import PersonalDataTypeEnum


class PersonalDataRequest(BaseModel):
    type: PersonalDataTypeEnum
    last_name: str
    first_name: str
    middle_name: str | None = None
    birthdate: datetime | None = None
    metadata: dict[str, Any] | None = None

    model_config = ConfigDict(use_enum_values=True)

    @model_validator(mode="before")
    def validate_required_fields(cls, values: dict[str, Any]) -> dict[str, Any]:
        type_value = values.get("type")

        if type_value == PersonalDataTypeEnum.payout_statement_recipient:
            if not values.get("birthdate"):
                raise ValueError("Field 'birthdate' is required for type 'payout_statement_recipient'")

        return values

from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict, Field

from async_yookassa.enums.personal_data_enums import (
    PersonalDataStatusEnum,
    PersonalDataTypeEnum,
)
from async_yookassa.models.payment_submodels.cancellation_details import (
    PersonalDataDetails,
)


class PersonalDataResponse(BaseModel):
    id: str = Field(min_length=36, max_length=50)
    type: PersonalDataTypeEnum
    status: PersonalDataStatusEnum
    cancellation_details: PersonalDataDetails
    created_at: datetime
    expires_at: datetime | None = None
    metadata: dict[str, Any] | None = None

    model_config = ConfigDict(use_enum_values=True)

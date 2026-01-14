from datetime import datetime
from typing import Any

from pydantic import Field

from async_yookassa.enums.personal_data_enums import (
    PersonalDataStatusEnum,
    PersonalDataTypeEnum,
)
from async_yookassa.models.base import ModelConfigBase
from async_yookassa.models.payment.cancellation_details import CancellationDetails


class PersonalDataResponse(ModelConfigBase):
    id: str = Field(min_length=36, max_length=50)
    type: PersonalDataTypeEnum
    status: PersonalDataStatusEnum
    cancellation_details: CancellationDetails | None = None
    created_at: datetime
    expires_at: datetime | None = None
    metadata: dict[str, Any] | None = None

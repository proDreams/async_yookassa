from datetime import datetime
from typing import Any, Literal

from async_yookassa.enums.personal_data_enums import PersonalDataTypeEnum
from async_yookassa.models.base import ModelConfigBase


class SBPPersonalDataRequest(ModelConfigBase):
    type: Literal[PersonalDataTypeEnum.sbp_payout_recipient]
    last_name: str
    first_name: str
    middle_name: str | None = None
    metadata: dict[str, Any] | None = None


class PayoutStatementRecipientPersonalDataRequest(SBPPersonalDataRequest):
    birthdate: datetime | None = None

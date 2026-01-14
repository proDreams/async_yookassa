from datetime import datetime
from typing import Any

from pydantic import Field

from async_yookassa.enums.deal_enums import DealFeeMomentEnum, DealTypeEnum
from async_yookassa.models.base import ModelConfigBase
from async_yookassa.models.list_options_base import ListOptionsBase


class DealRequest(ModelConfigBase):
    type: DealTypeEnum
    fee_moment: DealFeeMomentEnum
    metadata: dict[str, Any] | None = None
    description: str | None = Field(max_length=128, default=None)


class DealListOptions(ListOptionsBase):
    expires_at_gte: datetime | None = Field(default=None, serialization_alias="expires_at.gte")
    expires_at_gt: datetime | None = Field(default=None, serialization_alias="expires_at.gt")
    expires_at_lte: datetime | None = Field(default=None, serialization_alias="expires_at.lte")
    expires_at_lt: datetime | None = Field(default=None, serialization_alias="expires_at.lt")
    full_text_search: str | None = Field(min_length=4, max_length=128, default=None)
    status: str | None = None

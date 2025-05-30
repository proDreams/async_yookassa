from typing import Any

from pydantic import BaseModel, ConfigDict, Field

from async_yookassa.enums.deal_enums import DealFeeMomentEnum, DealTypeEnum


class DealRequest(BaseModel):
    type: DealTypeEnum
    fee_moment: DealFeeMomentEnum
    metadata: dict[str, Any] | None = None
    description: str | None = Field(max_length=128, default=None)

    model_config = ConfigDict(use_enum_values=True)

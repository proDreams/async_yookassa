from enum import Enum
from typing import Any

from pydantic import BaseModel, ConfigDict, Field

from async_yookassa.models.payment_submodels.amount_model import Amount


class StatusEnum(str, Enum):
    pending = "pending"
    waiting_for_capture = "waiting_for_capture"
    succeeded = "succeeded"
    canceled = "canceled"


class TransferBase(BaseModel):
    account_id: str
    amount: Amount
    description: str | None = Field(max_length=128, default=None)
    metadata: dict[str, Any] | None = None


class Transfer(TransferBase):
    platform_fee_amount: Amount


class TransferResponse(TransferBase):
    status: StatusEnum
    platform_fee_amount: Amount | None = None

    model_config = ConfigDict(use_enum_values=True)

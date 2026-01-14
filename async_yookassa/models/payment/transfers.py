from typing import Any

from pydantic import BaseModel, ConfigDict, Field

from async_yookassa.enums.transfers import TransferStatusEnum
from async_yookassa.models.payment.amount import Amount


class TransferBase(BaseModel):
    account_id: str
    amount: Amount
    platform_fee_amount: Amount | None = None


class Transfer(TransferBase):
    description: str | None = Field(max_length=128, default=None)
    metadata: dict[str, Any] | None = None


class TransferResponse(Transfer):
    status: TransferStatusEnum

    model_config = ConfigDict(use_enum_values=True)

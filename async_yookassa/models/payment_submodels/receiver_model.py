from enum import Enum

from pydantic import BaseModel, Field


class TypeEnum(str, Enum):
    bank_account = "bank_account"
    mobile_balance = "mobile_balance"
    digital_wallet = "digital_wallet"


class Receiver(BaseModel):
    type: TypeEnum
    account_number: str | None = Field(min_length=20, max_length=20)
    bic: str | None = Field(min_length=9, max_length=9)
    phone: str | None = Field(min_length=11, max_length=15)

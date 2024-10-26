from enum import Enum

from pydantic import BaseModel

from async_yoomoney.models.payment_submodels.amount_model import Amount


class TypeEnum(str, Enum):
    untaxed = "untaxed"
    calculated = "calculated"
    mixed = "mixed"


class VatData(BaseModel):
    type: TypeEnum
    amount: Amount | None = None
    rate: str | None = None

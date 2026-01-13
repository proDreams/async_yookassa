from pydantic import BaseModel, Field

from async_yookassa.models.payment.settlements import (
    Settlement,
)


class DealBase(BaseModel):
    id: str = Field(min_length=36, max_length=50)


class Deal(DealBase):
    settlements: list[Settlement]


class DealRefund(BaseModel):
    refund_settlements: list[Settlement]

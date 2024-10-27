from pydantic import BaseModel, Field

from async_yookassa.models.payment_submodels.deal_submodels.settlements_model import (
    Settlement,
)


class Deal(BaseModel):
    id: str = Field(min_length=36, max_length=50)
    settlements: list[Settlement]

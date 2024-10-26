from pydantic import BaseModel
from pydantic.v1 import Field

from async_yoomoney.models.payment_submodels.airline_submodels.legs_model import Legs
from async_yoomoney.models.payment_submodels.airline_submodels.passengers_model import (
    Passengers,
)


class Airline(BaseModel):
    ticket_number: str | None = Field(max_length=150)
    booking_reference: str | None = Field(max_length=20)
    passengers: list[Passengers] | None = None
    legs: list[Legs] | None = None

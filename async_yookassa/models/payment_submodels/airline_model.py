from pydantic import BaseModel
from pydantic.v1 import Field

from async_yookassa.models.payment_submodels.airline_submodels.legs_model import Legs
from async_yookassa.models.payment_submodels.airline_submodels.passengers_model import (
    Passengers,
)


class Airline(BaseModel):
    ticket_number: str | None = Field(max_length=150, default=None)
    booking_reference: str | None = Field(max_length=20, default=None)
    passengers: list[Passengers] | None = None
    legs: list[Legs] | None = None

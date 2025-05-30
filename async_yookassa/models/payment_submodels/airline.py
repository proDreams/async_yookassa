import re

from pydantic import BaseModel, field_validator
from pydantic.v1 import Field

from async_yookassa.models.payment_submodels.airline_submodels.legs import Leg
from async_yookassa.models.payment_submodels.airline_submodels.passengers import (
    Passenger,
)


class Airline(BaseModel):
    ticket_number: str | None = Field(max_length=150, default=None)
    booking_reference: str | None = Field(max_length=20, default=None)
    passengers: list[Passenger] | None = None
    legs: list[Leg] | None = None

    @field_validator("ticket_number", mode="before")
    def ticket_number_validator(cls, value: str) -> str:
        """
        Устанавливает ticket_number модели Airline.

        :param value: ticket_number модели Airline.
        :type value: str
        """
        if not re.match("^[0-9]{1,150}$", value):
            raise ValueError(
                r"Invalid value for `ticket_number`, must be a follow pattern or equal to `/^[0-9]{1,150}$/`"
            )

        return value

    @field_validator("passengers", mode="before")
    def passengers_validator(cls, value: list[Passenger]) -> list[Passenger]:
        """
        Устанавливает passengers модели Airline.

        :param value: passengers модели Airline.
        :type value: list[Passenger]
        """
        if len(value) > 500:
            raise ValueError("Invalid value for `passengers`, number of items must be less than or equal to `500`")

        return value

    @field_validator("legs", mode="before")
    def legs_validator(cls, value: list[Leg]) -> list[Leg]:
        """
        Устанавливает legs модели Airline.

        :param value: legs модели Airline.
        :type value: list[Leg]
        """
        if len(value) > 4:
            raise ValueError("Invalid value for `legs`, number of items must be less than or equal to `4`")

        return value

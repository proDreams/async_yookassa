import re
from datetime import datetime

from pydantic import BaseModel, Field, field_validator


class Leg(BaseModel):
    departure_airport: str = Field(min_length=3, max_length=3)
    destination_airport: str = Field(min_length=3, max_length=3)
    departure_date: str
    carrier_code: str | None = Field(min_length=2, max_length=3, default=None)

    @field_validator("departure_airport", mode="before")
    def departure_airport_validator(cls, value: str) -> str:
        """
        Устанавливает departure_airport модели Leg.

        :param value: departure_airport модели Leg.
        :type value: str
        """
        if not re.match("^[A-Z]{3}$", value):
            raise ValueError(
                r"Invalid value for `departure_airport`, must be a follow pattern or equal to `/^[A-Z]{3}/`"
            )

        return value

    @field_validator("destination_airport", mode="before")
    def destination_airport_validator(cls, value: str) -> str:
        """
        Устанавливает destination_airport модели Leg.

        :param value: destination_airport модели Leg.
        :type value: str
        """
        if not re.match("^[A-Z]{3}$", value):
            raise ValueError(
                r"Invalid value for `destination_airport`, must be a follow pattern or equal to `/^[A-Z]{3}/`"
            )

        return value

    @field_validator("departure_date", mode="before")
    def departure_date_validator(cls, value: str) -> str:
        """
        Устанавливает departure_date модели Leg.

        :param value: departure_date модели Leg.
        :type value: datetime
        """
        try:
            datetime.strptime(value, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")

        return value

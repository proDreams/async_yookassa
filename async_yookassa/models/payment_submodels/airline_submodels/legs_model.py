from pydantic import BaseModel, Field


class Legs(BaseModel):
    departure_airport: str = Field(min_length=3, max_length=3)
    destination_airport: str = Field(min_length=3, max_length=3)
    departure_date: str
    carrier_code: str | None = Field(min_length=2, max_length=3, default=None)

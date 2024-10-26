from pydantic import BaseModel


class Card(BaseModel):
    number: str
    expiry_year: str
    expiry_month: str
    cardholder: str | None = None
    csc: str | None = None

from pydantic import BaseModel, Field


class Customer(BaseModel):
    full_name: str | None = Field(max_length=256)
    inn: str | None = Field(max_length=12)
    email: str | None = None
    phone: str | None = Field(max_length=11, min_length=11)

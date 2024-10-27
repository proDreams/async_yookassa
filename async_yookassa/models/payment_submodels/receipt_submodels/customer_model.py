from pydantic import BaseModel, EmailStr, Field


class Customer(BaseModel):
    full_name: str | None = Field(max_length=256)
    inn: str | None = Field(max_length=12)
    email: EmailStr | None = None
    phone: str | None = Field(max_length=11, min_length=11)

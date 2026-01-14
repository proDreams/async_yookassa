from pydantic import BaseModel, EmailStr, Field


class Customer(BaseModel):
    full_name: str | None = Field(max_length=256, default=None)
    inn: str | None = Field(max_length=12, default=None)
    email: EmailStr | None = None
    phone: str | None = Field(max_length=11, min_length=11, default=None)

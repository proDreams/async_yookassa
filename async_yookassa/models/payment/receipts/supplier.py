from pydantic import BaseModel


class Supplier(BaseModel):
    name: str | None = None
    phone: str | None = None
    inn: str | None = None

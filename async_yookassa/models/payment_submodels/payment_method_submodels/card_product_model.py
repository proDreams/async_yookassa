from pydantic import BaseModel


class CardProduct(BaseModel):
    code: str
    name: str | None = None

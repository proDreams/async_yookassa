from pydantic import BaseModel


class MarkQuantity(BaseModel):
    numerator: int
    denominator: int

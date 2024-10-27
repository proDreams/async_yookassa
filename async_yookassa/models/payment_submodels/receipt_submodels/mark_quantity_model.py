from pydantic import BaseModel, Field


class MarkQuantity(BaseModel):
    numerator: int = Field(ge=1)
    denominator: int = Field(ge=1)

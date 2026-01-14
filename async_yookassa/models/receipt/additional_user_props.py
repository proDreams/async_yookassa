from pydantic import BaseModel, Field


class AdditionalUserProps(BaseModel):
    name: str = Field(max_length=64)
    value: str = Field(max_length=234)

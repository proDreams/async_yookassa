from pydantic import BaseModel, Field


class Passengers(BaseModel):
    first_name: str = Field(max_length=64)
    last_name: str = Field(max_length=64)

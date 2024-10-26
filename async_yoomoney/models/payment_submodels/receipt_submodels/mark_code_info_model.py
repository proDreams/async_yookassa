from pydantic import BaseModel, Field


class MarkCodeInfo(BaseModel):
    mark_code_raw: str | None = None
    unknown: str | None = Field(max_length=32)
    ean_8: str | None = Field(min_length=8, max_length=8)
    ean_13: str | None = Field(min_length=13, max_length=13)
    itf_14: str | None = Field(min_length=14, max_length=14)
    gs_10: str | None = Field(max_length=38)
    gs_1m: str | None = Field(max_length=200)
    short: str | None = Field(max_length=38)
    fur: str | None = Field(min_length=20, max_length=20)
    egais_20: str | None = Field(min_length=33, max_length=33)
    egais_30: str | None = Field(min_length=14, max_length=14)

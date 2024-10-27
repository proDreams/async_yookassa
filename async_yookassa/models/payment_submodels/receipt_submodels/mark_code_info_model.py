from pydantic import BaseModel, Field


class MarkCodeInfo(BaseModel):
    mark_code_raw: str | None = None
    unknown: str | None = Field(min_length=1, max_length=32, default=None)
    ean_8: str | None = Field(min_length=8, max_length=8, default=None)
    ean_13: str | None = Field(min_length=13, max_length=13, default=None)
    itf_14: str | None = Field(min_length=14, max_length=14, default=None)
    gs_10: str | None = Field(min_length=1, max_length=38, default=None)
    gs_1m: str | None = Field(min_length=1, max_length=200, default=None)
    short: str | None = Field(min_length=1, max_length=38, default=None)
    fur: str | None = Field(min_length=20, max_length=20, default=None)
    egais_20: str | None = Field(min_length=33, max_length=33, default=None)
    egais_30: str | None = Field(min_length=14, max_length=14, default=None)

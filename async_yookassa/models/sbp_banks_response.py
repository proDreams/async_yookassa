from pydantic import BaseModel, Field


class SbpBank(BaseModel):
    bank_id: str = Field(max_length=12)
    name: str = Field(max_length=128)
    bic: str = Field(max_length=9)


class SbpBankListResponse(BaseModel):
    type: str
    items: list[SbpBank]
    next_cursor: str | None = None

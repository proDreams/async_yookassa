from pydantic import BaseModel, Field


class SBPPayerBankDetails(BaseModel):
    bank_id: str = Field(max_length=12)
    bic: str


class B2BSBPayerBankDetails(BaseModel):
    full_name: str = Field(max_length=800)
    short_name: str = Field(max_length=160)
    address: str = Field(max_length=500)
    inn: str = Field(max_length=12)
    bank_name: str = Field(min_length=1, max_length=350)
    bank_branch: str = Field(min_length=1, max_length=140)
    bank_bik: str = Field(max_length=9)
    account: str = Field(max_length=20)
    kpp: str | None = Field(max_length=9, default=None)

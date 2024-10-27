from pydantic import BaseModel


class SBPPayerBankDetails(BaseModel):
    bank_id: str
    bic: str


class B2BSBPayerBankDetails(BaseModel):
    full_name: str
    short_name: str
    address: str
    inn: str
    bank_name: str
    bank_branch: str
    bank_bik: str
    account: str
    kpp: str | None = None

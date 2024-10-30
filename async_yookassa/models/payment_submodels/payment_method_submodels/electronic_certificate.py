from pydantic import BaseModel, Field

from async_yookassa.models.payment_submodels.amount import Amount


class ElectronicCertificate(BaseModel):
    amount: Amount
    basket_id: str


class Certificate(BaseModel):
    certificate_id: str = Field(min_length=20, max_length=30)
    tru_quantity: int
    available_compensation: Amount
    applied_compensation: Amount

from pydantic import BaseModel

from async_yookassa.models.payment_submodels.amount_model import Amount


class ElectronicCertificate(BaseModel):
    amount: Amount
    basket_id: str


class Certificate(BaseModel):
    certificate_id: str
    tru_quantity: int
    available_compensation: Amount
    applied_compensation: Amount

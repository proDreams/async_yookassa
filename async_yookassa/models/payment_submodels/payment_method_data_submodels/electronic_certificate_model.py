from pydantic import BaseModel

from async_yookassa.models.payment_submodels.amount_model import Amount


class ElectronicCertificate(BaseModel):
    amount: Amount
    basket_id: str

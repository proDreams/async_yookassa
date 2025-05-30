from pydantic import BaseModel

from async_yookassa.models.payment_submodels.airline import Airline
from async_yookassa.models.payment_submodels.amount import Amount
from async_yookassa.models.payment_submodels.deal import Deal
from async_yookassa.models.payment_submodels.receipt import Receipt
from async_yookassa.models.payment_submodels.transfers import Transfer


class CapturePaymentRequest(BaseModel):
    amount: Amount | None = None
    receipt: Receipt | None = None
    airline: Airline | None = None
    transfers: list[Transfer] | None = None
    deal: Deal | None = None

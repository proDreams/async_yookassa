from pydantic import BaseModel

from async_yookassa.models.payment_submodels.airline_model import Airline
from async_yookassa.models.payment_submodels.amount_model import Amount
from async_yookassa.models.payment_submodels.deal_model import Deal
from async_yookassa.models.payment_submodels.receipt_model import Receipt
from async_yookassa.models.payment_submodels.transfers_model import Transfer


class CapturePaymentRequest(BaseModel):
    amount: Amount | None = None
    receipt: Receipt | None = None
    airline: Airline | None = None
    transfers: list[Transfer] | None = None
    deal: Deal | None = None

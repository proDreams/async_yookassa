from pydantic import BaseModel

from async_yookassa.models.payment.airline import Airline
from async_yookassa.models.payment.amount import Amount
from async_yookassa.models.payment.deal import Deal
from async_yookassa.models.payment.receipts.base import Receipt
from async_yookassa.models.payment.transfers import Transfer


class CapturePaymentRequest(BaseModel):
    amount: Amount | None = None
    receipt: Receipt | None = None
    airline: Airline | None = None
    transfers: list[Transfer] | None = None
    deal: Deal | None = None

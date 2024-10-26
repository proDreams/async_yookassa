from typing import Any

from pydantic import BaseModel, Field

from async_yoomoney.models.payment_submodels.airline_model import Airline
from async_yoomoney.models.payment_submodels.amount_model import Amount
from async_yoomoney.models.payment_submodels.confirmation_model import Confirmation
from async_yoomoney.models.payment_submodels.deal_model import Deal
from async_yoomoney.models.payment_submodels.payment_method_data_model import (
    PaymentMethodData,
)
from async_yoomoney.models.payment_submodels.receipt_model import Receipt
from async_yoomoney.models.payment_submodels.receiver_model import Receiver
from async_yoomoney.models.payment_submodels.recipient_model import Recipient
from async_yoomoney.models.payment_submodels.transfers_model import Transfers


class PaymentRequest(BaseModel):
    amount: Amount
    description: str | None = Field(max_length=128, default=None)
    receipt: Receipt | None = None
    recipient: Recipient | None = None
    payment_token: str | None = None
    payment_method_id: str | None = None
    payment_method_data: PaymentMethodData | None = None
    confirmation: Confirmation | None = None
    save_payment_method: bool = False
    capture: bool = False
    client_ip: str | None = None
    metadata: dict[str, Any] | None = None
    airline: Airline | None = None
    transfers: list[Transfers] | None = None
    deal: Deal | None = None
    merchant_customer_id: str | None = None
    receiver: Receiver | None = None


print(PaymentRequest(**{"amount": {"value": 1000, "currency": "euq"}}).model_dump())

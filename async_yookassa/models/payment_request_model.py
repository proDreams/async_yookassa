from datetime import datetime, timedelta
from typing import Any

from pydantic import BaseModel, Field, model_validator

from async_yookassa.enums.payment_method_data_enums import PaymentMethodDataTypeEnum
from async_yookassa.models.payment_submodels.airline_model import Airline
from async_yookassa.models.payment_submodels.amount_model import Amount
from async_yookassa.models.payment_submodels.confirmation_model import Confirmation
from async_yookassa.models.payment_submodels.deal_model import Deal
from async_yookassa.models.payment_submodels.payment_method_data_model import (
    PaymentMethodData,
)
from async_yookassa.models.payment_submodels.receipt_model import Receipt
from async_yookassa.models.payment_submodels.receiver_model import Receiver
from async_yookassa.models.payment_submodels.recipient_model import Recipient
from async_yookassa.models.payment_submodels.transfers_model import Transfer


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
    transfers: list[Transfer] | None = None
    deal: Deal | None = None
    merchant_customer_id: str | None = Field(max_length=200, default=None)
    receiver: Receiver | None = None

    @model_validator(mode="before")
    def validate_data(cls, values):
        amount = values.get("amount")
        if amount is None or amount.value <= 0.0:
            raise ValueError("Invalid or unspecified payment amount")

        receipt = values.get("receipt")
        if receipt and receipt.has_items:
            if not (receipt.email or receipt.phone):
                raise ValueError("Both email and phone values are empty in receipt")
            if receipt.tax_system_code is None:
                for item in receipt.items:
                    if item.vat_code is None:
                        raise ValueError("Item vat_code and receipt tax_system_code not specified")

        payment_token = values.get("payment_token")
        payment_method_id = values.get("payment_method_id")
        payment_method_data = values.get("payment_method_data")

        if payment_token:
            if payment_method_id:
                raise ValueError("Both payment_token and payment_method_id values are specified")
            if payment_method_data:
                raise ValueError("Both payment_token and payment_method_data values are specified")
        elif payment_method_id and payment_method_data:
            raise ValueError("Both payment_method_id and payment_method_data values are specified")

        if payment_method_data and payment_method_data.type == PaymentMethodDataTypeEnum.bank_card:
            card = payment_method_data.card
            if card:
                date_now = datetime.now() - timedelta(hours=27)
                date_expiry = (
                    datetime(year=int(card.expiry_year), month=int(card.expiry_month), day=1)
                    + timedelta(days=31)
                    - timedelta(days=1)
                )
                if date_now >= date_expiry:
                    raise ValueError("Card expired")

        return values

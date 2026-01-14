from datetime import datetime, timedelta
from decimal import Decimal
from typing import Any, Self

from pydantic import EmailStr, Field, model_validator

from async_yookassa.enums.payment import PaymentMethodType, PaymentStatementDeliveryMethod, PaymentStatementType
from async_yookassa.models.base import ModelConfigBase
from async_yookassa.models.payment.airline import Airline
from async_yookassa.models.payment.amount import Amount
from async_yookassa.models.payment.confirmation import ConfirmationRequestUnion
from async_yookassa.models.payment.deal import Deal
from async_yookassa.models.payment.methods.data import PaymentMethodData
from async_yookassa.models.payment.order import PaymentOrder
from async_yookassa.models.payment.receipts.base import Receipt
from async_yookassa.models.payment.receiver import ReceiverUnion
from async_yookassa.models.payment.recipient import Recipient
from async_yookassa.models.payment.transfers import Transfer


class PaymentData(ModelConfigBase):
    amount: Amount
    description: str | None = Field(max_length=128, default=None)
    receipt: Receipt | None = None
    recipient: Recipient | None = None
    save_payment_method: bool = False
    capture: bool = False
    client_ip: str | None = None
    metadata: dict[str, Any] | None = None


class PaymentRequestStatementDeliveryMethod(ModelConfigBase):
    type: PaymentStatementDeliveryMethod
    email: EmailStr


class PaymentRequestStatement(ModelConfigBase):
    type: PaymentStatementType
    delivery_method: PaymentRequestStatementDeliveryMethod


class PaymentRequest(PaymentData):
    payment_token: str | None = None
    payment_method_id: str | None = None
    payment_method_data: PaymentMethodData | None = None
    confirmation: ConfirmationRequestUnion | None = None
    airline: Airline | None = None
    transfers: list[Transfer] | None = None
    deal: Deal | None = None
    merchant_customer_id: str | None = Field(max_length=200, default=None)
    payment_order: PaymentOrder | None = None
    receiver: ReceiverUnion | None = None
    statements: list[PaymentRequestStatement] | None = None

    @model_validator(mode="after")
    def validate_data(self, values) -> Self:
        amount = values.amount
        if amount is None or Decimal(amount.value) <= Decimal("0.0"):
            raise ValueError("Invalid or unspecified payment amount")

        receipt = values.receipt
        if receipt and receipt.items:
            if not (
                receipt.email
                or receipt.phone
                or receipt.customer
                and (receipt.customer.phone or receipt.customer.email)
            ):
                raise ValueError("Both email and phone values are empty in receipt")
            if receipt.tax_system_code is None:
                for item in receipt.items:
                    if item.vat_code is None:
                        raise ValueError("Item vat_code and receipt tax_system_code not specified")

        payment_token = values.payment_token
        payment_method_id = values.payment_method_id
        payment_method_data = values.payment_method_data

        if payment_token:
            if payment_method_id:
                raise ValueError("Both payment_token and payment_method_id values are specified")
            if payment_method_data:
                raise ValueError("Both payment_token and payment_method_data values are specified")
        elif payment_method_id and payment_method_data:
            raise ValueError("Both payment_method_id and payment_method_data values are specified")

        if payment_method_data and payment_method_data.type == PaymentMethodType.bank_card:
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

from typing import Annotated, Literal, Union

from pydantic import Field

from async_yookassa.enums.payment import PaymentMethodType
from async_yookassa.models.base import ModelConfigBase
from async_yookassa.models.payment.methods.card import (
    CardRequest,
)
from async_yookassa.models.payment.methods.vat_data import VatDataUnion


class PaymentMethodBase(ModelConfigBase):
    type: Literal[PaymentMethodType.sber_loan, PaymentMethodType.sbp]


class PhoneRequiredPaymentMethod(PaymentMethodBase):
    type: Literal[PaymentMethodType.mobile_balance]
    phone: str


class BankCardPaymentMethod(PaymentMethodBase):
    type: Literal[PaymentMethodType.bank_card]
    card: CardRequest | None = None


class PhoneNotRequiredPaymentMethod(PaymentMethodBase):
    type: Literal[PaymentMethodType.cash, PaymentMethodType.sber_bnpl]
    phone: str | None = None


class B2BSberbankPaymentMethod(PaymentMethodBase):
    type: Literal[PaymentMethodType.b2b_sberbank]
    payment_purpose: str = Field(max_length=210)
    vat_data: VatDataUnion


PaymentMethodData = Annotated[
    Union[
        PaymentMethodBase,
        PhoneRequiredPaymentMethod,
        BankCardPaymentMethod,
        PhoneNotRequiredPaymentMethod,
        B2BSberbankPaymentMethod,
    ],
    Field(discriminator="type"),
]

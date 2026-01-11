from typing import Annotated, Literal, Union

from pydantic import Field

from async_yookassa.enums.payment_method import PaymentMethodTypeEnum
from async_yookassa.enums.payment_method_data import PaymentMethodDataTypeEnum
from async_yookassa.models.base import ModelConfigBase
from async_yookassa.models.payment_submodels.payment_method_submodels.card import (
    CardRequest,
)
from async_yookassa.models.payment_submodels.payment_method_submodels.vat_data import VatDataUnion


class PaymentMethodBase(ModelConfigBase):
    type: Literal[PaymentMethodDataTypeEnum.sber_loan, PaymentMethodDataTypeEnum.sbp]


class PhoneRequiredPaymentMethod(PaymentMethodBase):
    type: Literal[PaymentMethodDataTypeEnum.mobile_balance]
    phone: str


class BankCardPaymentMethod(PaymentMethodBase):
    type: Literal[PaymentMethodDataTypeEnum.bank_card]
    card: CardRequest | None = None


class PhoneNotRequiredPaymentMethod(PaymentMethodBase):
    type: Literal[PaymentMethodDataTypeEnum.cash, PaymentMethodTypeEnum.sber_bnpl]
    phone: str | None = None


class B2BSberbankPaymentMethod(PaymentMethodBase):
    type: Literal[PaymentMethodDataTypeEnum.b2b_sberbank]
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

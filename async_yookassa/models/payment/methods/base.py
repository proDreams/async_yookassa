import re
from datetime import datetime
from typing import Annotated, Any, Literal, Union

from pydantic import BaseModel, ConfigDict, Field, field_validator

from async_yookassa.enums.payment import PaymentMethodStatus, PaymentMethodType
from async_yookassa.models.payment.amount import Amount
from async_yookassa.models.payment.methods.articles import (
    ArticleRefund,
    ArticleResponse,
)
from async_yookassa.models.payment.methods.card import (
    CardResponse,
)
from async_yookassa.models.payment.methods.electronic_certificate import (
    ElectronicCertificate,
)
from async_yookassa.models.payment.methods.payer_bank_details import (
    B2BSBPayerBankDetails,
    SBPPayerBankDetails,
)
from async_yookassa.models.payment.methods.vat_data import (
    VatDataUnion,
)


class PaymentMethodBase(BaseModel):
    id: str
    saved: bool
    status: PaymentMethodStatus
    title: str | None = None

    model_config = ConfigDict(use_enum_values=True)


class SberLoanPaymentMethod(PaymentMethodBase):
    type: Literal[PaymentMethodType.sber_loan]
    discount_amount: Amount | None = None
    loan_option: str | None = None
    suspended_until: datetime | None = None

    @field_validator("loan_option", mode="before")
    def validate_loan_option(cls, value: Any) -> str | None:
        if value is None:
            return None

        if not isinstance(value, str):
            raise ValueError("Value must be a string")

        if value == "loan":
            return value

        match_pattern = re.match(r"^installments_(\d+)$", value)

        if not match_pattern:
            raise ValueError("Value must be 'loan' or format 'installments_XX'")

        months = int(match_pattern.group(1))

        if months < 1:
            raise ValueError("Installment months must be greater than 0")

        return value


class AlfabankPaymentMethod(PaymentMethodBase):
    type: Literal[PaymentMethodType.alfabank]
    login: str | None = None


class GenericPaymentMethod(PaymentMethodBase):
    type: Literal[
        PaymentMethodType.mobile_balance,
        PaymentMethodType.installments,
        PaymentMethodType.cash,
        PaymentMethodType.sber_bnpl,
        PaymentMethodType.apple_pay,
        PaymentMethodType.google_pay,
        PaymentMethodType.qiwi,
        PaymentMethodType.wechat,
        PaymentMethodType.webmoney,
    ]


class BankCardPaymentMethod(PaymentMethodBase):
    type: Literal[PaymentMethodType.bank_card]
    card: CardResponse | None = None


class SBPPaymentMethodBase(PaymentMethodBase):
    type: Literal[PaymentMethodType.sbp]
    sbp_operation_id: str | None = None


class SBPPaymentMethodResponse(PaymentMethodBase):
    payer_bank_details: SBPPayerBankDetails | None = None


class B2BSberbankPaymentMethod(PaymentMethodBase):
    type: Literal[PaymentMethodType.b2b_sberbank]
    payer_bank_details: B2BSBPayerBankDetails | None = None
    payment_purpose: str = Field(max_length=210)
    vat_data: VatDataUnion


class ElectronicCertificatePaymentMethodBase(BankCardPaymentMethod):
    type: Literal[PaymentMethodType.electronic_certificate]
    electronic_certificate: ElectronicCertificate | None = None


class ElectronicCertificatePaymentMethodResponse(ElectronicCertificatePaymentMethodBase):
    articles: ArticleResponse | None = None


class ElectronicCertificatePaymentMethodRefund(ElectronicCertificatePaymentMethodBase):
    articles: ArticleRefund | None = None


class YooMoneyPaymentMethod(PaymentMethodBase):
    type: Literal[PaymentMethodType.yoo_money]
    account_number: str | None = None


class SberPayPaymentMethod(BankCardPaymentMethod):
    type: Literal[PaymentMethodType.sberbank]
    phone: str | None = None


class TPayPaymentMethod(BankCardPaymentMethod):
    type: Literal[PaymentMethodType.tinkoff_bank]


PaymentMethodUnion = Annotated[
    Union[
        SberLoanPaymentMethod,
        AlfabankPaymentMethod,
        BankCardPaymentMethod,
        SBPPaymentMethodResponse,
        B2BSberbankPaymentMethod,
        ElectronicCertificatePaymentMethodResponse,
        YooMoneyPaymentMethod,
        SberPayPaymentMethod,
        TPayPaymentMethod,
        GenericPaymentMethod,
    ],
    Field(discriminator="type"),
]

PaymentMethodRefundUnion = Annotated[
    Union[SBPPaymentMethodResponse, ElectronicCertificatePaymentMethodRefund],
    Field(discriminator="type"),
]

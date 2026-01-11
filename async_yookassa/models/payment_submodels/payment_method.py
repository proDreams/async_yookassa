import re
from datetime import datetime
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator

from async_yookassa.enums.payment_method import PaymentMethodStatusEnum, PaymentMethodTypeEnum
from async_yookassa.models.payment_submodels.amount import Amount
from async_yookassa.models.payment_submodels.payment_method_submodels.articles import (
    ArticleRefund,
    ArticleResponse,
)
from async_yookassa.models.payment_submodels.payment_method_submodels.card import (
    CardResponse,
)
from async_yookassa.models.payment_submodels.payment_method_submodels.electronic_certificate import (
    ElectronicCertificate,
)
from async_yookassa.models.payment_submodels.payment_method_submodels.payer_bank_details import (
    B2BSBPayerBankDetails,
    SBPPayerBankDetails,
)
from async_yookassa.models.payment_submodels.payment_method_submodels.vat_data import (
    VatDataUnion,
)


class PaymentMethodBase(BaseModel):
    id: str
    saved: bool
    status: PaymentMethodStatusEnum
    title: str | None = None

    model_config = ConfigDict(use_enum_values=True)


class SberLoanPaymentMethod(PaymentMethodBase):
    type: Literal[PaymentMethodTypeEnum.sber_loan]
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
    type: Literal[PaymentMethodTypeEnum.alfabank]
    login: str | None = None


class GenericPaymentMethod(PaymentMethodBase):
    type: Literal[
        PaymentMethodTypeEnum.mobile_balance,
        PaymentMethodTypeEnum.installments,
        PaymentMethodTypeEnum.cash,
        PaymentMethodTypeEnum.sber_bnpl,
        PaymentMethodTypeEnum.apple_pay,
        PaymentMethodTypeEnum.google_pay,
        PaymentMethodTypeEnum.qiwi,
        PaymentMethodTypeEnum.wechat,
        PaymentMethodTypeEnum.webmoney,
    ]


class BankCardPaymentMethod(PaymentMethodBase):
    type: Literal[PaymentMethodTypeEnum.bank_card]
    card: CardResponse | None = None


class SBPPaymentMethod(PaymentMethodBase):
    type: Literal[PaymentMethodTypeEnum.sbp]
    payer_bank_details: SBPPayerBankDetails | None = None
    sbp_operation_id: str | None = None


class B2BSberbankPaymentMethod(PaymentMethodBase):
    type: Literal[PaymentMethodTypeEnum.b2b_sberbank]
    payer_bank_details: B2BSBPayerBankDetails | None = None
    payment_purpose: str = Field(max_length=210)
    vat_data: VatDataUnion


class ElectronicCertificatePaymentMethod(BankCardPaymentMethod):
    type: Literal[PaymentMethodTypeEnum.electronic_certificate]
    articles: ArticleResponse | None = None
    electronic_certificate: ElectronicCertificate | None = None


class YooMoneyPaymentMethod(PaymentMethodBase):
    type: Literal[PaymentMethodTypeEnum.yoo_money]
    account_number: str | None = None


class SberPayPaymentMethod(BankCardPaymentMethod):
    type: Literal[PaymentMethodTypeEnum.sberbank]
    phone: str | None = None


class TPayPaymentMethod(BankCardPaymentMethod):
    type: Literal[PaymentMethodTypeEnum.tinkoff_bank]


class PaymentMethodRefund(PaymentMethodBase):
    articles: ArticleRefund | None = None

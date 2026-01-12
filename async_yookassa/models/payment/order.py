import re

from pydantic import Field, field_validator

from async_yookassa.enums.payment import PaymentOrderType
from async_yookassa.models.base import ModelConfigBase
from async_yookassa.models.payment.amount import Amount


class PaymentOrderPeriod(ModelConfigBase):
    month: int = Field(ge=1, le=12)
    year: int = Field(ge=1000, le=3000)


class PaymentOrderRecipientBank(ModelConfigBase):
    name: str
    bic: str
    account: str
    correspondent_account: str

    @field_validator("bic", mode="before")
    def bic_validator(cls, value: str) -> str:
        if not re.match("^[0-9]{9}$", value):
            raise ValueError(r"Invalid value ...")

        return value


class PaymentOrderRecipient(ModelConfigBase):
    name: str
    inn: str
    kpp: str
    bank: PaymentOrderRecipientBank

    @field_validator("inn", mode="before")
    def inn_validator(cls, value: str) -> str:
        if not re.match("^[0-9]{10}$", value):
            raise ValueError(r"Invalid value ...")

        return value

    @field_validator("kpp", mode="before")
    def kpp_validator(cls, value: str) -> str:
        if not re.match("^[0-9]{9}$", value):
            raise ValueError(r"Invalid value ...")

        return value


class PaymentOrder(ModelConfigBase):
    type: PaymentOrderType
    account_number: str | None = None
    amount: Amount
    kbk: str | None = None
    oktmo: str | None = None
    payment_document_id: str | None = None
    payment_document_number: str | None = None
    payment_period: PaymentOrderPeriod | None = None
    payment_purpose: str
    recipient: PaymentOrderRecipient
    service_id: str | None = None
    unified_account_number: str | None = None

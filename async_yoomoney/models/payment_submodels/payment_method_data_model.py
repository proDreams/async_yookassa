from enum import Enum

from pydantic import BaseModel, Field

from async_yoomoney.models.payment_submodels.payment_method_data_submodels.articles_model import (
    Articles,
)
from async_yoomoney.models.payment_submodels.payment_method_data_submodels.card_model import (
    Card,
)
from async_yoomoney.models.payment_submodels.payment_method_data_submodels.electronic_certificate_model import (
    ElectronicCertificate,
)
from async_yoomoney.models.payment_submodels.payment_method_data_submodels.vat_data_model import (
    VatData,
)


class TypeEnum(str, Enum):
    sber_loan = "sber_loan"
    mobile_balance = "mobile_balance"
    cash = "cash"
    sbp = "sbp"
    b2b_sberbank = "b2b_sberbank"
    electronic_certificate = "electronic_certificate"
    yoo_money = "yoo_money"
    sberbank = "sberbank"
    tinkoff_bank = "tinkoff_bank"


class PaymentMethodData(BaseModel):
    type: TypeEnum
    phone: str | None = None
    card: Card | None = None
    payment_purpose: str | None = Field(max_length=210)
    vat_data: VatData | None = None
    articles: list[Articles] | None = None
    electronic_certificate: ElectronicCertificate | None = None

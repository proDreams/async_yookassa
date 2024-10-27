from enum import Enum

from pydantic import BaseModel, model_validator

from async_yookassa.models.payment_submodels.amount_model import Amount
from async_yookassa.models.payment_submodels.payment_method_submodels.articles_model import (
    ArticleResponse,
)
from async_yookassa.models.payment_submodels.payment_method_submodels.card_model import (
    CardResponse,
)
from async_yookassa.models.payment_submodels.payment_method_submodels.electronic_certificate_model import (
    ElectronicCertificate,
)
from async_yookassa.models.payment_submodels.payment_method_submodels.payer_bank_details_model import (
    B2BSBPayerBankDetails,
    SBPPayerBankDetails,
)
from async_yookassa.models.payment_submodels.payment_method_submodels.vat_data_model import (
    VatData,
)


class TypeEnum(str, Enum):
    sber_loan = "sber_loan"
    alfabank = "alfabank"
    mobile_balance = "mobile_balance"
    bank_card = "bank_card"
    installments = "installments"
    cash = "cash"
    sbp = "sbp"
    b2b_sberbank = "b2b_sberbank"
    electronic_certificate = "electronic_certificate"
    yoo_money = "yoo_money"
    apple_pay = "apple_pay"
    google_pay = "google_pay"
    qiwi = "qiwi"
    sberbank = "sberbank"
    tinkoff_bank = "tinkoff_bank"
    wechat = "wechat"
    webmoney = "webmoney"


class PaymentMethod(BaseModel):
    type: TypeEnum
    id: str
    saved: bool
    title: str | None = None
    discount_amount: Amount | None = None
    loan_option: str | None = None
    login: str | None = None
    payer_bank_details: SBPPayerBankDetails | B2BSBPayerBankDetails | None = None
    sbp_operation_id: str | None = None
    payment_purpose: str | None = None
    vat_data: VatData | None = None
    articles: ArticleResponse | None = None
    card: CardResponse | None = None
    electronic_certificate: ElectronicCertificate | None = None
    account_number: str | None = None
    phone: str | None = None

    class Config:
        use_enum_values = True

    @model_validator(mode="before")
    def validate_required_fields(cls, values):
        type_value = values.get("type")

        if type_value == TypeEnum.sbp:
            if data := values.get("payer_bank_details"):
                values["payer_bank_details"] = SBPPayerBankDetails(**data)
        elif type_value == TypeEnum.b2b_sberbank:
            if not values.get("payment_purpose"):
                raise ValueError("Field 'payment_purpose' are required for type 'b2b_sberbank'")
            if not values.get("vat_data"):
                raise ValueError("Field 'vat_data' are required for type 'b2b_sberbank'")
            if data := values.get("payer_bank_details"):
                values["payer_bank_details"] = B2BSBPayerBankDetails(**data)

        return values

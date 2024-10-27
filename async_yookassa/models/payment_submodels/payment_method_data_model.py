from enum import Enum

from pydantic import BaseModel, ConfigDict, Field, model_validator

from async_yookassa.models.payment_submodels.payment_method_submodels.articles_model import (
    Article,
)
from async_yookassa.models.payment_submodels.payment_method_submodels.card_model import (
    CardRequest,
)
from async_yookassa.models.payment_submodels.payment_method_submodels.electronic_certificate_model import (
    ElectronicCertificate,
)
from async_yookassa.models.payment_submodels.payment_method_submodels.vat_data_model import (
    VatData,
)


class TypeEnum(str, Enum):
    sber_loan = "sber_loan"
    mobile_balance = "mobile_balance"
    bank_card = "bank_card"
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
    card: CardRequest | None = None
    payment_purpose: str | None = Field(max_length=210, default=None)
    vat_data: VatData | None = None
    articles: list[Article] | None = None
    electronic_certificate: ElectronicCertificate | None = None

    model_config = ConfigDict(use_enum_values=True)

    @model_validator(mode="before")
    def validate_required_fields(cls, values):
        type_value = values.get("type")

        if type_value == TypeEnum.mobile_balance:
            if not values.get("phone"):
                raise ValueError("Field 'phone' is required for type 'mobile_balance'")

        elif type_value == TypeEnum.b2b_sberbank:
            if not values.get("payment_purpose"):
                raise ValueError("Field 'payment_purpose' are required for type 'b2b_sberbank'")
            if not values.get("vat_data"):
                raise ValueError("Field 'vat_data' are required for type 'b2b_sberbank'")

        return values

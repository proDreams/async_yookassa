from typing import Any

from pydantic import BaseModel, ConfigDict, Field, model_validator

from async_yookassa.enums.payment_method_enums import PaymentMethodTypeEnum
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


class PaymentMethod(BaseModel):
    type: PaymentMethodTypeEnum
    id: str
    saved: bool
    title: str | None = None
    discount_amount: Amount | None = None
    loan_option: str | None = None
    login: str | None = None
    payer_bank_details: SBPPayerBankDetails | B2BSBPayerBankDetails | None = None
    sbp_operation_id: str | None = None
    payment_purpose: str | None = Field(max_length=210, default=None)
    vat_data: VatData | None = None
    articles: ArticleResponse | None = None
    card: CardResponse | None = None
    electronic_certificate: ElectronicCertificate | None = None
    account_number: str | None = None
    phone: str | None = None

    model_config = ConfigDict(use_enum_values=True)

    @model_validator(mode="before")
    def validate_required_fields(cls, values: dict[str, Any]):
        type_value = values.get("type")

        if type_value == PaymentMethodTypeEnum.sbp:
            if data := values.get("payer_bank_details"):
                values["payer_bank_details"] = SBPPayerBankDetails(**data)
        elif type_value == PaymentMethodTypeEnum.b2b_sberbank:
            if not values.get("payment_purpose"):
                raise ValueError("Field 'payment_purpose' are required for type 'b2b_sberbank'")
            if not values.get("vat_data"):
                raise ValueError("Field 'vat_data' are required for type 'b2b_sberbank'")
            if data := values.get("payer_bank_details"):
                values["payer_bank_details"] = B2BSBPayerBankDetails(**data)

        return values

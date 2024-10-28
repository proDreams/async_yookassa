from pydantic import BaseModel, ConfigDict, Field, model_validator

from async_yookassa.enums.payment_method_data_enums import PaymentMethodDataTypeEnum
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


class PaymentMethodData(BaseModel):
    type: PaymentMethodDataTypeEnum
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

        if type_value == PaymentMethodDataTypeEnum.mobile_balance:
            if not values.get("phone"):
                raise ValueError("Field 'phone' is required for type 'mobile_balance'")

        elif type_value == PaymentMethodDataTypeEnum.b2b_sberbank:
            if not values.get("payment_purpose"):
                raise ValueError("Field 'payment_purpose' are required for type 'b2b_sberbank'")
            if not values.get("vat_data"):
                raise ValueError("Field 'vat_data' are required for type 'b2b_sberbank'")

        return values

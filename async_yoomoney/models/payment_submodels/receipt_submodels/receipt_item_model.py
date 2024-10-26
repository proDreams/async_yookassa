from pydantic import BaseModel, Field

from async_yoomoney.models.payment_submodels.amount_model import Amount
from async_yoomoney.models.payment_submodels.receipt_submodels.mark_code_info_model import (
    MarkCodeInfo,
)
from async_yoomoney.models.payment_submodels.receipt_submodels.mark_quantity_model import (
    MarkQuantity,
)
from async_yoomoney.models.payment_submodels.receipt_submodels.payment_subject_industry_details_model import (
    PaymentSubjectIndustryDetails,
)


class ReceiptItem(BaseModel):
    description: str = Field(max_length=128)
    amount: Amount
    vat_code: int = Field(le=6)
    quantity: int
    measure: str | None = None
    mark_quantity: MarkQuantity | None = None
    payment_subject: str | None = None
    payment_mode: str | None = None
    country_of_origin_code: str | None = Field(min_length=2, max_length=2)
    customs_declaration_number: str | None = Field(max_length=32)
    excise: str | None = None
    product_code: str | None = None
    mark_code_info: MarkCodeInfo | None = None
    mark_mode: str | None = None
    payment_subject_industry_details: PaymentSubjectIndustryDetails | None = None

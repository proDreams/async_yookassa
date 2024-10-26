from pydantic import BaseModel, Field

from async_yoomoney.models.payment_submodels.receipt_submodels.customer_model import (
    Customer,
)
from async_yoomoney.models.payment_submodels.receipt_submodels.payment_subject_industry_details_model import (
    PaymentSubjectIndustryDetails,
)
from async_yoomoney.models.payment_submodels.receipt_submodels.receipt_item_model import (
    ReceiptItem,
)
from async_yoomoney.models.payment_submodels.receipt_submodels.receipt_operational_details_model import (
    ReceiptOperationalDetails,
)


class Receipt(BaseModel):
    customer: Customer | None = None
    items: list[ReceiptItem]
    phone: str | None = Field(min_length=11, max_length=11)
    email: str | None = None
    tax_system_code: str | None = Field(max_length=6)
    receipt_industry_details: list[PaymentSubjectIndustryDetails] | None = None
    receipt_operational_details: ReceiptOperationalDetails | None = None

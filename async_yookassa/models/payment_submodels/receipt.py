from pydantic import BaseModel, Field

from async_yookassa.models.payment_submodels.receipt_submodels.customer import Customer
from async_yookassa.models.payment_submodels.receipt_submodels.payment_subject_industry_details import (
    PaymentSubjectIndustryDetails,
)
from async_yookassa.models.payment_submodels.receipt_submodels.receipt_item import (
    ReceiptItemBase,
)
from async_yookassa.models.payment_submodels.receipt_submodels.receipt_operational_details import (
    ReceiptOperationalDetails,
)


class Receipt(BaseModel):
    customer: Customer | None = None
    items: list[ReceiptItemBase]
    internet: bool | None = None
    tax_system_code: int | None = Field(ge=1, le=6, default=None)
    timezone: int | None = Field(ge=1, le=11, default=None)
    receipt_industry_details: list[PaymentSubjectIndustryDetails] | None = None
    receipt_operational_details: ReceiptOperationalDetails | None = None

from pydantic import BaseModel, EmailStr, Field

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
    phone: str | None = Field(min_length=11, max_length=11, default=None)
    email: EmailStr | None = None
    tax_system_code: int | None = Field(le=6, default=None)
    receipt_industry_details: list[PaymentSubjectIndustryDetails] | None = None
    receipt_operational_details: ReceiptOperationalDetails | None = None

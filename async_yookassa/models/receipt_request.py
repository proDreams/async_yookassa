from pydantic import BaseModel, Field

from async_yookassa.enums.receipt_type import ReceiptType
from async_yookassa.models.payment_submodels.deal_submodels.settlements import (
    SettlementReceipt,
)
from async_yookassa.models.payment_submodels.receipt_submodels.customer import Customer
from async_yookassa.models.payment_submodels.receipt_submodels.payment_subject_industry_details import (
    PaymentSubjectIndustryDetails,
)
from async_yookassa.models.payment_submodels.receipt_submodels.receipt_item import (
    ReceiptItem,
)
from async_yookassa.models.payment_submodels.receipt_submodels.receipt_operational_details import (
    ReceiptOperationalDetails,
)
from async_yookassa.models.receipt_submodels.additional_user_props import (
    AdditionalUserProps,
)


class ReceiptRequest(BaseModel):
    type: ReceiptType
    payment_id: str | None = None
    refund_id: str | None = None
    customer: Customer
    items: list[ReceiptItem]
    send: bool = True
    tax_system_code: int | None = Field(ge=1, le=6, default=None)
    additional_user_props: AdditionalUserProps | None = None
    receipt_industry_details: list[PaymentSubjectIndustryDetails] | None = None
    receipt_operational_details: ReceiptOperationalDetails | None = None
    settlements: list[SettlementReceipt] | None = None
    on_behalf_of: str | None = None


class ReceiptListResponse(BaseModel):
    type: str
    items: list[ReceiptRequest]
    next_cursor: str | None = None

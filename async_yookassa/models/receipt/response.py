from datetime import datetime

from pydantic import BaseModel, Field

from async_yookassa.enums.payment import PaymentStatus
from async_yookassa.enums.receipt_type import ReceiptType
from async_yookassa.models.base import ModelConfigBase
from async_yookassa.models.payment.receipts.payment_subject_industry_details import (
    PaymentSubjectIndustryDetails,
)
from async_yookassa.models.payment.receipts.receipt_item import (
    ReceiptItem,
)
from async_yookassa.models.payment.receipts.receipt_operational_details import (
    ReceiptOperationalDetails,
)
from async_yookassa.models.payment.settlements import (
    SettlementReceipt,
)


class ReceiptResponse(ModelConfigBase):
    id: str = Field(min_length=39, max_length=39)
    type: ReceiptType
    payment_id: str | None = None
    refund_id: str | None = None
    status: PaymentStatus
    fiscal_document_number: str | None = None
    fiscal_storage_number: str | None = None
    fiscal_attribute: str | None = None
    registered_at: datetime | None = None
    fiscal_provider_id: str | None = None
    items: list[ReceiptItem]
    internet: bool | None = None
    settlements: list[SettlementReceipt] | None = None
    on_behalf_of: str | None = None
    tax_system_code: int | None = Field(ge=1, le=6)
    timezone: int | None = Field(ge=1, le=11)
    receipt_industry_details: list[PaymentSubjectIndustryDetails] | None = None
    receipt_operational_details: ReceiptOperationalDetails | None = None


class ReceiptListResponse(BaseModel):
    type: str
    items: list[ReceiptResponse]
    next_cursor: str | None = None

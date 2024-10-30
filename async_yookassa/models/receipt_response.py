from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from async_yookassa.enums.payment_response import ReceiptRegistrationEnum
from async_yookassa.enums.receipt_type import ReceiptType
from async_yookassa.models.payment_submodels.deal_submodels.settlements import (
    SettlementReceipt,
)
from async_yookassa.models.payment_submodels.receipt_submodels.payment_subject_industry_details import (
    PaymentSubjectIndustryDetails,
)
from async_yookassa.models.payment_submodels.receipt_submodels.receipt_item import (
    ReceiptItem,
)
from async_yookassa.models.payment_submodels.receipt_submodels.receipt_operational_details import (
    ReceiptOperationalDetails,
)


class ReceiptResponse(BaseModel):
    id: str = Field(min_length=39, max_length=39)
    type: ReceiptType
    payment_id: str | None = None
    refund_id: str | None = None
    status: ReceiptRegistrationEnum
    fiscal_document_number: str | None = None
    fiscal_storage_number: str | None = None
    fiscal_attribute: str | None = None
    registered_at: datetime | None = None
    fiscal_provider_id: str | None = None
    items: list[ReceiptItem]
    settlements: list[SettlementReceipt] | None = None
    on_behalf_of: str | None = None
    tax_system_code: int | None = None
    receipt_industry_details: list[PaymentSubjectIndustryDetails] | None = None
    receipt_operational_details: ReceiptOperationalDetails | None = None

    model_config = ConfigDict(use_enum_values=True)

from typing import Literal

from pydantic import BaseModel, Field

from async_yookassa.enums.receipt_type import ReceiptType
from async_yookassa.models.list_options_base import ListOptionsBase
from async_yookassa.models.payment.receipts.customer import Customer
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
from async_yookassa.models.receipt.additional_user_props import (
    AdditionalUserProps,
)


class ReceiptRequest(BaseModel):
    type: ReceiptType
    payment_id: str | None = None
    refund_id: str | None = None
    customer: Customer
    items: list[ReceiptItem]
    internet: bool | None = None
    send: bool = True
    tax_system_code: int | None = Field(ge=1, le=6, default=None)
    timezone: int | None = Field(ge=1, le=11, default=None)
    additional_user_props: AdditionalUserProps | None = None
    receipt_industry_details: list[PaymentSubjectIndustryDetails] | None = None
    receipt_operational_details: ReceiptOperationalDetails | None = None
    settlements: list[SettlementReceipt] | None = None
    on_behalf_of: str | None = None


class ReceiptListOptions(ListOptionsBase):
    payment_id: str | None = None
    refund_id: str | None = None
    status: Literal["pending", "succeeded", "canceled"] | None = None

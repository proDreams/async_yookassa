from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict, Field

from async_yookassa.enums.payment_response import ReceiptRegistrationEnum
from async_yookassa.models.payment_submodels.amount import Amount
from async_yookassa.models.payment_submodels.authorization_details import (
    AuthorizationDetails,
)
from async_yookassa.models.payment_submodels.cancellation_details import (
    CancellationDetails,
)
from async_yookassa.models.payment_submodels.confirmation import ConfirmationResponse
from async_yookassa.models.payment_submodels.deal import Deal
from async_yookassa.models.payment_submodels.invoice_details import InvoiceDetails
from async_yookassa.models.payment_submodels.payment_method import PaymentMethod
from async_yookassa.models.payment_submodels.recipient import RecipientResponse
from async_yookassa.models.payment_submodels.transfers import TransferResponse


class PaymentResponse(BaseModel):
    id: str = Field(min_length=36, max_length=36)
    status: ReceiptRegistrationEnum
    amount: Amount
    income_amount: Amount | None = None
    description: str | None = Field(max_length=128, default=None)
    recipient: RecipientResponse
    payment_method: PaymentMethod | None = None
    captured_at: datetime | None = None
    created_at: datetime
    expires_at: datetime | None = None
    confirmation: ConfirmationResponse | None = None
    test: bool
    refunded_amount: Amount | None = None
    paid: bool
    refundable: bool
    receipt_registration: ReceiptRegistrationEnum | None = None
    metadata: dict[str, Any] | None = None
    cancellation_details: CancellationDetails | None = None
    authorization_details: AuthorizationDetails | None = None
    transfers: list[TransferResponse] | None = None
    deal: Deal | None = None
    merchant_customer_id: str | None = Field(max_length=200, default=None)
    invoice_details: InvoiceDetails | None = None

    model_config = ConfigDict(use_enum_values=True)


class PaymentListResponse(BaseModel):
    type: str
    items: list[PaymentResponse]
    next_cursor: str | None = None

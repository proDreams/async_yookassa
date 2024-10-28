from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict, Field

from async_yookassa.enums.payment_response_enums import (
    PaymentResponseStatusEnum,
    ReceiptRegistrationEnum,
)
from async_yookassa.models.payment_submodels.amount_model import Amount
from async_yookassa.models.payment_submodels.authorization_details_model import (
    AuthorizationDetails,
)
from async_yookassa.models.payment_submodels.cancellation_details_model import (
    CancellationDetails,
)
from async_yookassa.models.payment_submodels.confirmation_model import Confirmation
from async_yookassa.models.payment_submodels.deal_model import Deal
from async_yookassa.models.payment_submodels.invoice_details_model import InvoiceDetails
from async_yookassa.models.payment_submodels.payment_method_model import PaymentMethod
from async_yookassa.models.payment_submodels.recipient_model import RecipientResponse
from async_yookassa.models.payment_submodels.transfers_model import TransferResponse


class PaymentResponse(BaseModel):
    id: str = Field(min_length=36, max_length=36)
    status: PaymentResponseStatusEnum
    amount: Amount
    income_amount: Amount | None = None
    description: str | None = Field(max_length=128, default=None)
    recipient: RecipientResponse
    payment_method: PaymentMethod | None = None
    captured_at: datetime | None = None
    created_at: datetime
    expires_at: datetime | None = None
    confirmation: Confirmation | None = None
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

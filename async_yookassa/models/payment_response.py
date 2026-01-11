from datetime import datetime
from typing import Annotated, Any, Literal, Union

from pydantic import BaseModel, ConfigDict, Field

from async_yookassa.enums.payment_response import PaymentStatusEnum
from async_yookassa.models.base import ModelConfigBase
from async_yookassa.models.payment_submodels.amount import Amount
from async_yookassa.models.payment_submodels.authorization_details import (
    AuthorizationDetails,
)
from async_yookassa.models.payment_submodels.cancellation_details import (
    CancellationDetails,
)
from async_yookassa.models.payment_submodels.confirmation import ConfirmationUnion
from async_yookassa.models.payment_submodels.deal import Deal
from async_yookassa.models.payment_submodels.invoice_details import InvoiceDetails
from async_yookassa.models.payment_submodels.payment_method import (
    AlfabankPaymentMethod,
    B2BSberbankPaymentMethod,
    BankCardPaymentMethod,
    ElectronicCertificatePaymentMethod,
    GenericPaymentMethod,
    SberLoanPaymentMethod,
    SberPayPaymentMethod,
    SBPPaymentMethod,
    TPayPaymentMethod,
    YooMoneyPaymentMethod,
)
from async_yookassa.models.payment_submodels.recipient import RecipientResponse
from async_yookassa.models.payment_submodels.transfers import TransferResponse

PaymentMethodUnion = Annotated[
    Union[
        SberLoanPaymentMethod,
        AlfabankPaymentMethod,
        BankCardPaymentMethod,
        SBPPaymentMethod,
        B2BSberbankPaymentMethod,
        ElectronicCertificatePaymentMethod,
        YooMoneyPaymentMethod,
        SberPayPaymentMethod,
        TPayPaymentMethod,
        GenericPaymentMethod,
    ],
    Field(discriminator="type"),
]


class PaymentResponse(ModelConfigBase):
    id: str = Field(min_length=36, max_length=36)
    status: PaymentStatusEnum
    amount: Amount
    income_amount: Amount | None = None
    description: str | None = Field(max_length=128, default=None)
    recipient: RecipientResponse
    payment_method: PaymentMethodUnion | None = None
    captured_at: datetime | None = None
    created_at: datetime
    expires_at: datetime | None = None
    confirmation: ConfirmationUnion | None = None
    test: bool
    refunded_amount: Amount | None = None
    paid: bool
    refundable: bool
    receipt_registration: PaymentStatusEnum | None = None
    metadata: dict[str, Any] | None = None
    cancellation_details: CancellationDetails | None = None
    authorization_details: AuthorizationDetails | None = None
    transfers: list[TransferResponse] | None = None
    deal: Deal | None = None
    merchant_customer_id: str | None = Field(max_length=200, default=None)
    invoice_details: InvoiceDetails | None = None


class PaymentListOptions(BaseModel):
    created_at_gte: datetime | None = Field(default=None, serialization_alias="created_at.gte")
    created_at_gt: datetime | None = Field(default=None, serialization_alias="created_at.gt")
    created_at_lte: datetime | None = Field(default=None, serialization_alias="created_at.lte")
    created_at_lt: datetime | None = Field(default=None, serialization_alias="created_at.lt")
    captured_at_gte: datetime | None = Field(default=None, serialization_alias="captured_at.gte")
    captured_at_gt: datetime | None = Field(default=None, serialization_alias="captured_at.gt")
    captured_at_lte: datetime | None = Field(default=None, serialization_alias="captured_at.lte")
    captured_at_lt: datetime | None = Field(default=None, serialization_alias="captured_at.lt")
    payment_method: str | None = None
    status: Literal["pending", "waiting_for_capture", "succeeded", "canceled"] | str | None = None
    limit: int | None = Field(default=10, ge=1, le=100)
    cursor: str | None = None

    model_config = ConfigDict(populate_by_name=True)


class PaymentListResponse(BaseModel):
    type: str
    items: list[PaymentResponse]
    next_cursor: str | None = None

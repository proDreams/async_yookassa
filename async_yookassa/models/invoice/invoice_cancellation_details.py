from async_yookassa.enums.invoice_cancellation_details import (
    InvoicePartyEnum,
    InvoiceReasonEnum,
)
from async_yookassa.models.base import ModelConfigBase


class InvoiceCancellationDetails(ModelConfigBase):
    party: InvoicePartyEnum
    reason: InvoiceReasonEnum

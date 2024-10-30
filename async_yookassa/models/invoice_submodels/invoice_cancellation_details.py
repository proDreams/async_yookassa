from pydantic import BaseModel, ConfigDict

from async_yookassa.enums.invoice_cancellation_details import (
    InvoicePartyEnum,
    InvoiceReasonEnum,
)


class InvoiceCancellationDetails(BaseModel):
    party: InvoicePartyEnum
    reason: InvoiceReasonEnum

    model_config = ConfigDict(use_enum_values=True)

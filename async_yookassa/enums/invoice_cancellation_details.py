from enum import Enum


class InvoicePartyEnum(str, Enum):
    yoo_money = "yoo_money"
    merchant = "merchant"


class InvoiceReasonEnum(str, Enum):
    invoice_canceled = "invoice_canceled"
    invoice_expired = "invoice_expired"
    general_decline = "general_decline"
    payment_canceled = "payment_canceled"
    payment_expired_on_capture = "payment_expired_on_capture"

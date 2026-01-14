from enum import StrEnum


class WebhookEvent(StrEnum):
    PAYMENT_WAITING_FOR_CAPTURE = "payment.waiting_for_capture"
    PAYMENT_SUCCEEDED = "payment.succeeded"
    PAYMENT_CANCELED = "payment.canceled"
    PAYMENT_METHOD_ACTIVE = "payment_method.active"
    REFUND_SUCCEEDED = "refund.succeeded"
    PAYOUT_SUCCEEDED = "payout.succeeded"
    PAYOUT_CANCELED = "payout.canceled"
    DEAL_CLOSED = "deal.closed"

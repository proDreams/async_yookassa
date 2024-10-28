from enum import Enum


class PaymentResponseStatusEnum(str, Enum):
    pending = "pending"
    waiting_for_capture = "waiting_for_capture"
    succeeded = "succeeded"
    canceled = "canceled"


class ReceiptRegistrationEnum(str, Enum):
    pending = "pending"
    succeeded = "succeeded"
    canceled = "canceled"

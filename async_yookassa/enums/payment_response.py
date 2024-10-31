from enum import Enum


class ReceiptRegistrationEnum(str, Enum):
    pending = "pending"
    succeeded = "succeeded"
    canceled = "canceled"


class PaymentResponseStatusEnum(ReceiptRegistrationEnum):
    waiting_for_capture = "waiting_for_capture"


class SelfEmployedStatusEnum(ReceiptRegistrationEnum):
    unregistered = "unregistered"

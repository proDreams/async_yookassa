from enum import Enum


class ReceiptRegistrationEnum(str, Enum):
    pending = "pending"
    succeeded = "succeeded"
    canceled = "canceled"
    waiting_for_capture = "waiting_for_capture"
    unregistered = "unregistered"

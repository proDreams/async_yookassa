from enum import StrEnum


class PaymentStatusEnum(StrEnum):
    pending = "pending"
    succeeded = "succeeded"
    canceled = "canceled"
    waiting_for_capture = "waiting_for_capture"
    unregistered = "unregistered"

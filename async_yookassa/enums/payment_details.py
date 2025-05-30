from enum import Enum


class PaymentDetailsStatusEnum(str, Enum):
    waiting_for_capture = "waiting_for_capture"
    succeeded = "succeeded"
    canceled = "canceled"

from enum import Enum


class TransferStatusEnum(str, Enum):
    pending = "pending"
    waiting_for_capture = "waiting_for_capture"
    succeeded = "succeeded"
    canceled = "canceled"

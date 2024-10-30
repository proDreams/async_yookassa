from enum import Enum


class ReceiptType(str, Enum):
    payment = "payment"
    refund = "refund"

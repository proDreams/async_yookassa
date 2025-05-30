from enum import Enum


class SettlementTypeEnum(str, Enum):
    payout = "payout"


class SettlementReceiptEnum(str, Enum):
    cashless = "cashless"
    prepayment = "prepayment"
    postpayment = "postpayment"
    consideration = "consideration"

from enum import StrEnum


class SettlementTypeEnum(StrEnum):
    payout = "payout"


class SettlementReceiptEnum(StrEnum):
    cashless = "cashless"
    prepayment = "prepayment"
    postpayment = "postpayment"
    consideration = "consideration"

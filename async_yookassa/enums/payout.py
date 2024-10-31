from enum import Enum


class PayoutTypeEnum(str, Enum):
    bank_card = "bank_card"
    sbp = "sbp"
    yoo_money = "yoo_money"

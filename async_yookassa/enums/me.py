from enum import Enum


class MeStatusEnum(str, Enum):
    enabled = "enabled"
    disabled = "disabled"


class PayoutMethodsEnum(str, Enum):
    bank_card = "bank_card"
    yoo_money = "yoo_money"
    sbp = "sbp"

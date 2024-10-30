from enum import Enum


class PaymentMethodDataTypeEnum(str, Enum):
    sber_loan = "sber_loan"
    mobile_balance = "mobile_balance"
    bank_card = "bank_card"
    cash = "cash"
    sbp = "sbp"
    b2b_sberbank = "b2b_sberbank"
    electronic_certificate = "electronic_certificate"
    yoo_money = "yoo_money"
    sberbank = "sberbank"
    tinkoff_bank = "tinkoff_bank"

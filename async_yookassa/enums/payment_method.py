from enum import StrEnum


class PaymentMethodTypeEnum(StrEnum):
    sber_loan = "sber_loan"
    alfabank = "alfabank"
    mobile_balance = "mobile_balance"
    bank_card = "bank_card"
    installments = "installments"
    cash = "cash"
    sber_bnpl = "sber_bnpl"
    sbp = "sbp"
    b2b_sberbank = "b2b_sberbank"
    electronic_certificate = "electronic_certificate"
    yoo_money = "yoo_money"
    apple_pay = "apple_pay"
    google_pay = "google_pay"
    qiwi = "qiwi"
    sberbank = "sberbank"
    tinkoff_bank = "tinkoff_bank"
    wechat = "wechat"
    webmoney = "webmoney"


class PaymentMethodStatusEnum(StrEnum):
    pending = "pending"
    active = "active"
    inactive = "inactive"

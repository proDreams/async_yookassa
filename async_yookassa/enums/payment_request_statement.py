from enum import StrEnum


class PaymentRequestStatementEnum(StrEnum):
    PAYMENT_OVERVIEW = "payment_overview"


class PaymentRequestDeliveryMethod(StrEnum):
    EMAIL = "email"

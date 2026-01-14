"""Payment-related enums for YooKassa API."""

from enum import StrEnum


class PaymentStatus(StrEnum):
    """Статус платежа."""

    pending = "pending"
    succeeded = "succeeded"
    canceled = "canceled"
    waiting_for_capture = "waiting_for_capture"


class ReceiptRegistrationStatus(StrEnum):
    """Статус регистрации чека."""

    pending = "pending"
    succeeded = "succeeded"
    canceled = "canceled"


class PaymentMethodType(StrEnum):
    """Тип платёжного метода."""

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


class PaymentMethodStatus(StrEnum):
    """Статус сохранённого платёжного метода."""

    pending = "pending"
    active = "active"
    inactive = "inactive"


class ConfirmationType(StrEnum):
    """Тип подтверждения платежа."""

    embedded = "embedded"
    external = "external"
    mobile_application = "mobile_application"
    qr = "qr"
    redirect = "redirect"


class CancellationParty(StrEnum):
    """Инициатор отмены платежа."""

    merchant = "merchant"
    payment_network = "payment_network"
    yoo_money = "yoo_money"


class CancellationReason(StrEnum):
    """Причина отмены платежа."""

    three_d_secure_failed = "3d_secure_failed"
    call_issuer = "call_issuer"
    canceled_by_merchant = "canceled_by_merchant"
    card_expired = "card_expired"
    country_forbidden = "country_forbidden"
    deal_expired = "deal_expired"
    expired_on_capture = "expired_on_capture"
    expired_on_confirmation = "expired_on_confirmation"
    fraud_suspected = "fraud_suspected"
    general_decline = "general_decline"
    identification_required = "identification_required"
    insufficient_funds = "insufficient_funds"
    internal_timeout = "internal_timeout"
    invalid_card_number = "invalid_card_number"
    invalid_csc = "invalid_csc"
    issuer_unavailable = "issuer_unavailable"
    payment_method_limit_exceeded = "payment_method_limit_exceeded"
    payment_method_restricted = "payment_method_restricted"
    permission_revoked = "permission_revoked"
    unsupported_mobile_operator = "unsupported_mobile_operator"
    rejected_by_payee = "rejected_by_payee"
    rejected_by_timeout = "rejected_by_timeout"
    yoo_money_account_closed = "yoo_money_account_closed"
    payment_article_number_not_found = "payment_article_number_not_found"
    payment_basket_id_not_found = "payment_basket_id_not_found"
    payment_tru_code_not_found = "payment_tru_code_not_found"
    some_articles_already_refunded = "some_articles_already_refunded"
    too_many_refunding_articles = "too_many_refunding_articles"
    one_time_limit_exceeded = "one_time_limit_exceeded"
    periodic_limit_exceeded = "periodic_limit_exceeded"
    recipient_check_failed = "recipient_check_failed"
    recipient_not_found = "recipient_not_found"


class CardType(StrEnum):
    """Тип банковской карты."""

    mastercard = "MasterCard"
    visa = "Visa"
    mir = "Mir"
    union_pay = "UnionPay"
    jcb = "JCB"
    american_express = "AmericanExpress"
    diners_club = "DinersClub"
    discover = "DiscoverCard"
    insta_payment = "InstaPayment"
    insta_payment_tm = "InstaPaymentTM"
    laser = "Laser"
    dankort = "Dankort"
    solo = "Solo"
    switch = "Switch"
    unknown = "Unknown"


class CardSource(StrEnum):
    """Источник данных банковской карты."""

    mir_pay = "mir_pay"
    apple_pay = "apple_pay"
    google_pay = "google_pay"


class PaymentOrderLocale(StrEnum):
    """Локаль платёжной формы."""

    ru = "ru_RU"
    en = "en_US"


class PaymentOrderType(StrEnum):
    """Тип платёжного поручения."""

    utilities = "utilities"


class PaymentStatementType(StrEnum):
    """Тип выписки по платежу."""

    payment_overview = "payment_overview"
    refund_usage = "refund_usage"


class PaymentStatementDeliveryMethod(StrEnum):
    """Способ доставки выписки."""

    email = "email"

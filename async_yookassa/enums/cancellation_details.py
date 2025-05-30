from enum import Enum


class PartyEnum(str, Enum):
    merchant = "merchant"
    payment_network = "payment_network"
    yoo_money = "yoo_money"


class ReasonEnum(str, Enum):
    general_decline = "general_decline"
    insufficient_funds = "insufficient_funds"
    three_d_secure_failed = "3d_secure_failed"
    call_issuer = "call_issuer"
    canceled_by_merchant = "canceled_by_merchant"
    card_expired = "card_expired"
    country_forbidden = "country_forbidden"
    deal_expired = "deal_expired"
    expired_on_capture = "expired_on_capture"
    expired_on_confirmation = "expired_on_confirmation"
    fraud_suspected = "fraud_suspected"
    identification_required = "identification_required"
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


class PersonalDataReasonEnum(str, Enum):
    expired_by_timeout = "expired_by_timeout"

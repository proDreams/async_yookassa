from enum import Enum


class PartyEnum(str, Enum):
    yoo_money = "yoo_money"
    payment_network = "payment_network"
    merchant = "merchant"


class ReasonEnum(str, Enum):
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

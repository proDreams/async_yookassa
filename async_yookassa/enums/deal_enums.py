from enum import Enum


class DealTypeEnum(str, Enum):
    safe_deal = "safe_deal"


class DealFeeMomentEnum(str, Enum):
    payment_succeeded = "payment_succeeded"
    deal_closed = "deal_closed"


class DealStatusEnum(str, Enum):
    opened = "opened"
    closed = "closed"

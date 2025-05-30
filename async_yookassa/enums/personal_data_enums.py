from enum import Enum


class PersonalDataTypeEnum(str, Enum):
    sbp_payout_recipient = "sbp_payout_recipient"
    payout_statement_recipient = "payout_statement_recipient"


class PersonalDataStatusEnum(str, Enum):
    waiting_for_operation = "waiting_for_operation"
    active = "active"
    canceled = "canceled"

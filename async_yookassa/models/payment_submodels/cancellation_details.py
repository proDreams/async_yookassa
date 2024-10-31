from pydantic import BaseModel, ConfigDict

from async_yookassa.enums.cancellation_details import (
    PartyEnum,
    PartyEnumPN,
    PartyEnumYM,
    PersonalDataReasonEnum,
    ReasonEnum,
    ReasonPayoutEnum,
    ReasonRefundEnum,
)


class Details(BaseModel):
    model_config = ConfigDict(use_enum_values=True)


class CancellationDetails(Details):
    party: PartyEnum
    reason: ReasonEnum


class RefundDetails(Details):
    party: PartyEnumPN
    reason: ReasonRefundEnum


class PayoutDetails(Details):
    party: PartyEnumPN
    reason: ReasonPayoutEnum


class PersonalDataDetails(Details):
    party: PartyEnumYM
    reason: PersonalDataReasonEnum

from pydantic import BaseModel, ConfigDict

from async_yookassa.enums.cancellation_details import (
    PartyEnum,
    PersonalDataReasonEnum,
    ReasonEnum,
)


class Details(BaseModel):
    model_config = ConfigDict(use_enum_values=True)


class CancellationDetails(Details):
    party: PartyEnum
    reason: ReasonEnum


class RefundDetails(Details):
    party: PartyEnum
    reason: ReasonEnum


class PayoutDetails(Details):
    party: PartyEnum
    reason: ReasonEnum


class PersonalDataDetails(Details):
    party: PartyEnum
    reason: PersonalDataReasonEnum

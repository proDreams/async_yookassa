from pydantic import BaseModel, ConfigDict

from async_yookassa.enums.payment import CancellationParty, CancellationReason


class Details(BaseModel):
    model_config = ConfigDict(use_enum_values=True)


class CancellationDetails(Details):
    party: CancellationParty
    reason: CancellationReason


class RefundDetails(Details):
    party: CancellationParty
    reason: CancellationReason


class PayoutDetails(Details):
    party: CancellationParty
    reason: CancellationReason


class PersonalDataDetails(Details):
    party: CancellationParty
    reason: CancellationReason  # PersonalDataReasonEnum is subset of CancellationReason

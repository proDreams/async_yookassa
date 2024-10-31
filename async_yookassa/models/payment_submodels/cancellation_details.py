from pydantic import BaseModel, ConfigDict

from async_yookassa.enums.cancellation_details import (
    PartyEnum,
    PartyEnumBase,
    ReasonEnum,
    ReasonPayoutEnum,
    ReasonRefundEnum,
)


class CancellationDetails(BaseModel):
    party: PartyEnum
    reason: ReasonEnum

    model_config = ConfigDict(use_enum_values=True)


class RefundDetails(BaseModel):
    party: PartyEnumBase
    reason: ReasonRefundEnum

    model_config = ConfigDict(use_enum_values=True)


class PayoutDetails(BaseModel):
    party: PartyEnumBase
    reason: ReasonPayoutEnum

    model_config = ConfigDict(use_enum_values=True)

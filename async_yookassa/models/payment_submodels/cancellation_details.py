from pydantic import BaseModel, ConfigDict

from async_yookassa.enums.cancellation_details import PartyEnum, ReasonEnum


class CancellationDetails(BaseModel):
    party: PartyEnum
    reason: ReasonEnum

    model_config = ConfigDict(use_enum_values=True)

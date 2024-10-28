from pydantic import BaseModel, ConfigDict

from async_yookassa.enums.candellation_details_enums import PartyEnum, ReasonEnum


class CancellationDetails(BaseModel):
    party: PartyEnum
    reason: ReasonEnum

    model_config = ConfigDict(use_enum_values=True)

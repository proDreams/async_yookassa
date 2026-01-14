from async_yookassa.enums.payment import CancellationParty, CancellationReason
from async_yookassa.models.base import ModelConfigBase


class CancellationDetails(ModelConfigBase):
    party: CancellationParty
    reason: CancellationReason

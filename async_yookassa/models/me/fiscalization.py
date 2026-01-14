from async_yookassa.enums.fiscalization import FiscalizationProviderEnum
from async_yookassa.models.base import ModelConfigBase


class Fiscalization(ModelConfigBase):
    enabled: bool
    provider: FiscalizationProviderEnum

from pydantic import BaseModel

from async_yookassa.enums.fiscalization import FiscalizationProviderEnum


class Fiscalization(BaseModel):
    enabled: bool
    provider: FiscalizationProviderEnum

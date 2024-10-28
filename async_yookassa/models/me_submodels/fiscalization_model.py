from pydantic import BaseModel

from async_yookassa.enums import FiscalizationProviderEnum


class Fiscalization(BaseModel):
    enabled: bool
    provider: FiscalizationProviderEnum

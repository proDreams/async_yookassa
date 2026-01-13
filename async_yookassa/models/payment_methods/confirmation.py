from typing import Literal

from async_yookassa.enums.payment import ConfirmationType
from async_yookassa.models.base import ModelConfigBase


class RedirectConfirmationResponse(ModelConfigBase):
    type: Literal[ConfirmationType.redirect]
    confirmation_url: str
    enforce: bool | None = None
    return_url: str | None = None


class RedirectConfirmationRequest(ModelConfigBase):
    type: Literal[ConfirmationType.redirect]
    enforce: bool | None = None
    locale: str | None = None
    return_url: str

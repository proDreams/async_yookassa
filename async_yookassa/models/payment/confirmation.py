from typing import Annotated, Literal, Union

from pydantic import BaseModel, ConfigDict, Field

from async_yookassa.enums.payment import ConfirmationType
from async_yookassa.models.base import ModelConfigBase


class ExternalConfirmation(ModelConfigBase):
    type: Literal[ConfirmationType.external]


class EmbeddedConfirmation(ModelConfigBase):
    type: Literal[ConfirmationType.embedded]
    confirmation_token: str


class MobileApplicationConfirmation(ModelConfigBase):
    type: Literal[ConfirmationType.mobile_application]
    confirmation_url: str


class QRConfirmation(ModelConfigBase):
    type: Literal[ConfirmationType.qr]
    confirmation_data: str


class RedirectConfirmation(MobileApplicationConfirmation):
    type: Literal[ConfirmationType.redirect]
    enforce: bool | None = None
    return_url: str | None = Field(max_length=2048, default=None)


ConfirmationUnion = Annotated[
    Union[
        ExternalConfirmation,
        EmbeddedConfirmation,
        MobileApplicationConfirmation,
        QRConfirmation,
        RedirectConfirmation,
    ],
    Field(discriminator="type"),
]


class ConfirmationRequestBase(ModelConfigBase):
    type: Literal[ConfirmationType.embedded, ConfirmationType.external]
    locale: str | None = None


class MobileApplicationConfirmationRequest(ConfirmationRequestBase):
    type: Literal[ConfirmationType.mobile_application]
    return_url: str


class QRConfirmationRequest(ConfirmationRequestBase):
    type: Literal[ConfirmationType.qr]
    return_url: str | None = None


class RedirectConfirmationRequest(MobileApplicationConfirmationRequest):
    type: Literal[ConfirmationType.redirect]
    enforce: bool | None = None


ConfirmationRequestUnion = Annotated[
    Union[
        ConfirmationRequestBase,
        MobileApplicationConfirmationRequest,
        QRConfirmationRequest,
        RedirectConfirmationRequest,
    ],
    Field(discriminator="type"),
]


class ConfirmationSelfEmployed(BaseModel):
    type: ConfirmationType

    model_config = ConfigDict(use_enum_values=True)


class ConfirmationSelfEmployedResponse(ConfirmationSelfEmployed):
    confirmation_url: str

from typing import Annotated, Literal, Union

from pydantic import BaseModel, ConfigDict, Field

from async_yookassa.enums.confirmation import ConfirmationTypeEnum
from async_yookassa.models.base import ModelConfigBase


class ExternalConfirmation(ModelConfigBase):
    type: Literal[ConfirmationTypeEnum.external]


class EmbeddedConfirmation(ModelConfigBase):
    type: Literal[ConfirmationTypeEnum.embedded]
    confirmation_token: str


class MobileApplicationConfirmation(ModelConfigBase):
    type: Literal[ConfirmationTypeEnum.mobile_application]
    confirmation_url: str


class QRConfirmation(ModelConfigBase):
    type: Literal[ConfirmationTypeEnum.qr]
    confirmation_data: str


class RedirectConfirmation(MobileApplicationConfirmation):
    type: Literal[ConfirmationTypeEnum.redirect]
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
    type: Literal[ConfirmationTypeEnum.embedded, ConfirmationTypeEnum.external]
    locale: str | None = None


class MobileApplicationConfirmationRequest(ConfirmationRequestBase):
    type: Literal[ConfirmationTypeEnum.mobile_application]
    return_url: str


class QRConfirmationRequest(ConfirmationRequestBase):
    type: Literal[ConfirmationTypeEnum.qr]
    return_url: str | None = None


class RedirectConfirmationRequest(MobileApplicationConfirmationRequest):
    type: Literal[ConfirmationTypeEnum.redirect]
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
    type: ConfirmationTypeEnum

    model_config = ConfigDict(use_enum_values=True)


class ConfirmationSelfEmployedResponse(ConfirmationSelfEmployed):
    confirmation_url: str

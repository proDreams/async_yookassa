from enum import Enum

from pydantic import BaseModel, model_validator


class TypeEnum(str, Enum):
    embedded = "embedded"
    external = "external"
    mobile_application = "mobile_application"
    qr = "qr"
    redirect = "redirect"


class ConfirmationBase(BaseModel):
    type: TypeEnum
    return_url: str | None = None
    enforce: bool | None = None


class Confirmation(ConfirmationBase):
    locale: str | None = None

    class Config:
        use_enum_values = True

    @model_validator(mode="before")
    def validate_required_fields(cls, values):
        type_value = values.get("type")

        if type_value == TypeEnum.mobile_application:
            if not values.get("return_url"):
                raise ValueError("Field 'return_url' is required for type 'mobile_application'")

        if type_value == TypeEnum.redirect:
            if not values.get("return_url"):
                raise ValueError("Field 'return_url' is required for type 'redirect'")


class ConfirmationResponse(ConfirmationBase):
    confirmation_token: str | None = None
    confirmation_url: str | None = None
    confirmation_data: str | None = None

    @model_validator(mode="before")
    def validate_required_fields(cls, values):
        type_value = values.get("type")

        if type_value == TypeEnum.embedded:
            if not values.get("confirmation_token"):
                raise ValueError("Field 'confirmation_token' is required for type 'embedded'")
        elif type_value == TypeEnum.mobile_application:
            if not values.get("confirmation_url"):
                raise ValueError("Field 'confirmation_url' is required for type 'mobile_application'")
        elif type_value == TypeEnum.redirect:
            if not values.get("confirmation_url"):
                raise ValueError("Field 'confirmation_url' is required for type 'redirect'")
        elif type_value == TypeEnum.qr:
            if not values.get("confirmation_data"):
                raise ValueError("Field 'confirmation_data' is required for type 'qr'")

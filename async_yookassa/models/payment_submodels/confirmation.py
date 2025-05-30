from pydantic import BaseModel, ConfigDict, Field, model_validator

from async_yookassa.enums.confirmation import ConfirmationTypeEnum


class ConfirmationBase(BaseModel):
    type: ConfirmationTypeEnum
    return_url: str | None = Field(max_length=2048, default=None)
    enforce: bool | None = None

    model_config = ConfigDict(use_enum_values=True)


class Confirmation(ConfirmationBase):
    locale: str | None = None

    model_config = ConfigDict(use_enum_values=True)

    @model_validator(mode="before")
    def validate_required_fields(cls, values):
        type_value = values.get("type")

        if type_value == ConfirmationTypeEnum.mobile_application:
            if not values.get("return_url"):
                raise ValueError("Field 'return_url' is required for type 'mobile_application'")

        if type_value == ConfirmationTypeEnum.redirect:
            if not values.get("return_url"):
                raise ValueError("Field 'return_url' is required for type 'redirect'")

        return values


class ConfirmationResponse(ConfirmationBase):
    confirmation_token: str | None = None
    confirmation_url: str | None = None
    confirmation_data: str | None = None

    @model_validator(mode="before")
    def validate_required_fields(cls, values):
        type_value = values.get("type")

        if type_value == ConfirmationTypeEnum.embedded:
            if not values.get("confirmation_token"):
                raise ValueError("Field 'confirmation_token' is required for type 'embedded'")
        elif type_value == ConfirmationTypeEnum.mobile_application:
            if not values.get("confirmation_url"):
                raise ValueError("Field 'confirmation_url' is required for type 'mobile_application'")
        elif type_value == ConfirmationTypeEnum.redirect:
            if not values.get("confirmation_url"):
                raise ValueError("Field 'confirmation_url' is required for type 'redirect'")
        elif type_value == ConfirmationTypeEnum.qr:
            if not values.get("confirmation_data"):
                raise ValueError("Field 'confirmation_data' is required for type 'qr'")

        return values


class ConfirmationSelfEmployed(BaseModel):
    type: ConfirmationTypeEnum

    model_config = ConfigDict(use_enum_values=True)


class ConfirmationSelfEmployedResponse(ConfirmationSelfEmployed):
    confirmation_url: str

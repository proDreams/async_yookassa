from typing import Annotated, Literal, Union

from pydantic import EmailStr, Field

from async_yookassa.enums.delivery_method import DeliveryMethodType
from async_yookassa.models.base import ModelConfigBase


class SMSDeliveryMethod(ModelConfigBase):
    type: Literal[DeliveryMethodType.SMS]


class SMSDeliveryMethodRequest(SMSDeliveryMethod):
    phone: str


class EmailDeliveryMethod(ModelConfigBase):
    type: Literal[DeliveryMethodType.EMAIL]


class EmailDeliveryMethodRequest(EmailDeliveryMethod):
    email: EmailStr


class SelfDeliveryMethodRequest(ModelConfigBase):
    type: Literal[DeliveryMethodType.SELF]


class SelfDeliveryMethodResponse(SelfDeliveryMethodRequest):
    url: str | None = Field(max_length=2048, default=None)


DeliveryMethodResponseUnion = Annotated[
    Union[SMSDeliveryMethod, EmailDeliveryMethod, SelfDeliveryMethodResponse],
    Field(discriminator="type"),
]
DeliveryMethodRequestUnion = Annotated[
    Union[SMSDeliveryMethodRequest, EmailDeliveryMethodRequest, SelfDeliveryMethodRequest],
    Field(discriminator="type"),
]

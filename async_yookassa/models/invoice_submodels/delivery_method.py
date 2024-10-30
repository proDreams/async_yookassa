from pydantic import BaseModel, ConfigDict, Field

from async_yookassa.enums.delivery_method import DeliveryMethodTypeEnum


class DeliveryMethod(BaseModel):
    type: DeliveryMethodTypeEnum
    url: str | None = Field(max_length=2048, default=None)

    model_config = ConfigDict(use_enum_values=True)

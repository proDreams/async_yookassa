from pydantic import BaseModel, Field

from async_yookassa.enums.payment_details import PaymentDetailsStatusEnum


class PaymentDetails(BaseModel):
    id: str = Field(min_length=36, max_length=36)
    status: PaymentDetailsStatusEnum

from pydantic import BaseModel, Field

from async_yookassa.enums.payment_details import PaymentDetailsStatusEnum


class PaymentDetails(BaseModel):
    id: str = Field(min_length=39, max_length=39)
    status: PaymentDetailsStatusEnum

from pydantic import BaseModel

from async_yookassa.models.payment_response import PaymentResponse


class PaymentListResponse(BaseModel):
    type: str
    items: list[PaymentResponse]
    next_cursor: str | None = None

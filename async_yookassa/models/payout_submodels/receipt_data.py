from pydantic import BaseModel, Field

from async_yookassa.models.payment_submodels.amount import Amount


class ReceiptData(BaseModel):
    service_name: str = Field(min_length=1, max_length=50)
    amount: Amount | None = None


class ReceiptDataResponse(ReceiptData):
    npd_receipt_id: str | None = None
    url: str | None = None

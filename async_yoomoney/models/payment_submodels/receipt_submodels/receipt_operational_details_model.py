from datetime import datetime

from pydantic import BaseModel, Field


class ReceiptOperationalDetails(BaseModel):
    operation_id: int = Field(gt=0, lt=255)
    value: str = Field(max_length=64)
    created_at: datetime

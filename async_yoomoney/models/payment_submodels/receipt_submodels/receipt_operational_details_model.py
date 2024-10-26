from pydantic import BaseModel, Field


class ReceiptOperationalDetails(BaseModel):
    operation_id: int = Field(le=255)
    value: str = Field(max_length=64)
    created_at: str

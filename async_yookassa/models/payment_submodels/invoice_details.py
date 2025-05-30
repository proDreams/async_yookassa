from pydantic import BaseModel, Field


class InvoiceDetails(BaseModel):
    id: str | None = Field(min_length=39, max_length=39, default=None)

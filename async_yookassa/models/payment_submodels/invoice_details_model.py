from pydantic import BaseModel


class InvoiceDetails(BaseModel):
    id: str | None

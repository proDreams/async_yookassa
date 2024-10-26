from pydantic import BaseModel, Field


class PaymentSubjectIndustryDetails(BaseModel):
    federal_id: str
    document_date: str
    document_number: str = Field(max_length=32)
    value: str = Field(max_length=256)

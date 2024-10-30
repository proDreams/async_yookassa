import re

from pydantic import BaseModel, Field, field_validator


class PaymentSubjectIndustryDetails(BaseModel):
    federal_id: str
    document_date: str
    document_number: str = Field(max_length=32)
    value: str = Field(max_length=256)

    @field_validator("federal_id", mode="before")
    def federal_id_validator(cls, value: str) -> str:
        """
        Устанавливает federal_id модели PaymentSubjectIndustryDetails.

        :param value: federal_id модели PaymentSubjectIndustryDetails.
        :type value: str
        """
        if not re.search(r"(^00[1-9]$)|(^0[1-6][0-9]$)|(^07[0-3]$)", value):
            raise ValueError(
                r"Invalid value for `federal_id`, "
                r"must be a follow pattern or equal to `/(^00[1-9]$)|(^0[1-6]{1}[0-9]$)|(^07[0-3]$)/`"
            )

        return value

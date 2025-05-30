from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from async_yookassa.enums.payment_response import ReceiptRegistrationEnum
from async_yookassa.models.payment_submodels.confirmation import (
    ConfirmationSelfEmployedResponse,
)


class SelfEmployedResponse(BaseModel):
    id: str = Field(min_length=36, max_length=50)
    status: ReceiptRegistrationEnum
    created_at: datetime
    itn: str | None = None
    phone: str | None = None
    confirmation: ConfirmationSelfEmployedResponse | None = None
    test: bool

    model_config = ConfigDict(use_enum_values=True)

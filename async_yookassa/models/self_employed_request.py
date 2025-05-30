from typing import Any

from pydantic import BaseModel, model_validator

from async_yookassa.models.payment_submodels.confirmation import (
    ConfirmationSelfEmployed,
)


class SelfEmployedRequest(BaseModel):
    itn: str | None = None
    phone: str | None = None
    confirmation: ConfirmationSelfEmployed | None = None

    @model_validator(mode="before")
    def validate_itn(cls, value: dict[str, Any]) -> dict[str, Any]:
        if value.get("itn") is None and value.get("phone") is None:
            raise ValueError("Both itn and phone values are empty in self_employed_request")

        return value

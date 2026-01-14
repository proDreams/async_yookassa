"""Personal Data service for YooKassa API."""

import uuid
from typing import Any

from async_yookassa.models.personal_data import (
    PayoutStatementRecipientPersonalDataRequest,
    PersonalDataResponse,
    SBPPersonalDataRequest,
)
from async_yookassa.services.base import BaseService


class PersonalDataService(BaseService):
    """Сервис для работы с персональными данными."""

    BASE_PATH = "/personal_data"

    async def find_one(self, personal_data_id: str) -> PersonalDataResponse:
        """
        placeholder
        """

        if not isinstance(personal_data_id, str):
            raise ValueError("Invalid payout_id value")

        response = await self._get(f"{self.BASE_PATH}/{personal_data_id}")
        return PersonalDataResponse(**response)

    async def create(
        self,
        params: dict[str, Any] | SBPPersonalDataRequest | PayoutStatementRecipientPersonalDataRequest,
        idempotency_key: uuid.UUID | None = None,
    ) -> PersonalDataResponse:
        """
        placeholder
        """

        if isinstance(params, dict):
            body = params
        elif isinstance(params, SBPPersonalDataRequest | PayoutStatementRecipientPersonalDataRequest):
            body = self._serialize_request(params)
        else:
            raise TypeError("Invalid params value type")

        response = await self._post(
            self.BASE_PATH,
            body=body,
            idempotency_key=idempotency_key,
        )
        return PersonalDataResponse(**response)

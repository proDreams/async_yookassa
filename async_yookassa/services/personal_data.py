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
    """
    Сервис для работы с персональными данными.

    Использование:
    ```python
    async with YooKassaClient(...) as client:
        # Сохранение персональных данных
        data = await client.personal_data.create(SBPPersonalDataRequest(...))

        # Получение данных
        data = await client.personal_data.find_one("data_id")
    ```
    """

    BASE_PATH = "/personal_data"

    async def find_one(self, personal_data_id: str) -> PersonalDataResponse:
        """
        Получение информации о сохраненных персональных данных.

        :param personal_data_id: Уникальный идентификатор персональных данных
        :return: Объект ответа PersonalDataResponse
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
        Создание (сохранение) персональных данных.

        :param params: Параметры сохранения (SBPPersonalDataRequest или PayoutStatementRecipientPersonalDataRequest)
        :param idempotency_key: Ключ идемпотентности
        :return: Объект ответа PersonalDataResponse
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

"""Webhook service for YooKassa API."""

import uuid
from typing import Any

from async_yookassa.models.webhook.request import WebhookRequest
from async_yookassa.models.webhook.response import WebhookListResponse, WebhookResponse
from async_yookassa.services.base import BaseService


class WebhookService(BaseService):
    """Сервис для работы с вебхуками."""

    BASE_PATH = "/webhooks"

    async def create(
        self,
        params: dict[str, Any] | WebhookRequest,
        idempotency_key: uuid.UUID | None = None,
    ) -> WebhookResponse:
        """
        Создание вебхука.

        :param params: Данные вебхука
        :param idempotency_key: Ключ идемпотентности
        :return: WebhookResponse
        """

        if isinstance(params, dict):
            request = WebhookRequest(**params)
        elif isinstance(params, WebhookRequest):
            request = params
        else:
            raise TypeError("Invalid params value type")

        body = self._serialize_request(request)

        response = await self._post(
            self.BASE_PATH,
            body=body,
            idempotency_key=idempotency_key,
        )
        return WebhookResponse(**response)

    async def delete(
        self,
        webhook_id: str,
        idempotency_key: uuid.UUID | None = None,
    ) -> None:
        """
        Удаление вебхука.

        :param webhook_id: Уникальный идентификатор вебхука
        :param idempotency_key: Ключ идемпотентности
        """
        if not isinstance(webhook_id, str):
            raise ValueError("Invalid webhook_id value")

        await self._http.request(
            method="DELETE",
            path=f"{self.BASE_PATH}/{webhook_id}",
            headers=self._get_idempotency_headers(idempotency_key),
        )

    async def list(self) -> WebhookListResponse:
        """
        Возвращает список вебхуков.

        :return: WebhookListResponse
        """
        response = await self._get(self.BASE_PATH)
        return WebhookListResponse(**response)

import uuid
from typing import Any

from async_yookassa.apiclient import APIClient
from async_yookassa.enums.request_methods import HTTPMethodEnum
from async_yookassa.models.webhook_request import WebhookRequest
from async_yookassa.models.webhook_response import WebhookList, WebhookResponse
from async_yookassa.utils import get_base_headers


class Webhook:
    """
    Класс, представляющий модель Webhook.
    """

    base_path = "/webhooks"

    def __init__(self):
        self.client = APIClient()

    @classmethod
    async def list(cls) -> WebhookList:
        """
        Возвращает список вебхуков

        :return: Объект ответа WebhookList, возвращаемого API при запросе списка вебхуков
        """
        instance = cls()

        path = cls.base_path

        response = await instance.client.request(method=HTTPMethodEnum.GET, path=path)

        return WebhookList(**response)

    @classmethod
    async def add(
        cls, params: dict[str, Any] | WebhookRequest, idempotency_key: uuid.UUID | None = None
    ) -> WebhookResponse:
        """
        Добавление вебхука

        :param params: Данные передаваемые в API
        :param idempotency_key: Ключ идемпотентности
        :return: Объект ответа WebhookResponse, возвращаемого API при запросе информации о вебхуке
        """
        instance = cls()

        path = cls.base_path

        headers = get_base_headers(idempotency_key=idempotency_key)

        if isinstance(params, dict):
            params_object = WebhookRequest(**params)
        elif isinstance(params, WebhookRequest):
            params_object = params
        else:
            raise TypeError("Invalid params value type")

        response = await instance.client.request(
            body=params_object, method=HTTPMethodEnum.POST, path=path, headers=headers
        )

        return WebhookResponse(**response)

    @classmethod
    async def remove(cls, webhook_id: str, idempotency_key: uuid.UUID | None = None) -> WebhookResponse:
        """
        Удаление вебхука

        :param webhook_id: Уникальный идентификатор вебхука
        :param idempotency_key: Ключ идемпотентности
        :return: Объект ответа WebhookResponse, возвращаемого API при запросе информации о вебхуке
        """
        instance = cls()

        path = cls.base_path + "/" + webhook_id

        headers = get_base_headers(idempotency_key=idempotency_key)

        response = await instance.client.request(method=HTTPMethodEnum.DELETE, path=path, headers=headers)

        return WebhookResponse(**response)

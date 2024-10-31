import uuid
from typing import Any

from async_yookassa.apiclient import APIClient
from async_yookassa.enums.request_methods import HTTPMethodEnum
from async_yookassa.models.self_employed_request import SelfEmployedRequest
from async_yookassa.models.self_employed_response import SelfEmployedResponse
from async_yookassa.utils import get_base_headers


class SelfEmployed:
    """
    Класс, представляющий модель SelfEmployed.
    """

    base_path = "/self_employed"

    def __init__(self):
        self.client = APIClient()

    @classmethod
    async def find_one(cls, self_employed_id: str) -> SelfEmployedResponse:
        """
        Возвращает информацию о сомозанятом

        :param self_employed_id: Уникальный идентификатор сомозанятого
        :return: Объект ответа SelfEmployedResponse, возвращаемого API при запросе информации о сомозанятом
        """
        instance = cls()

        if not isinstance(self_employed_id, str):
            raise ValueError("Invalid self_employed_id value")

        path = instance.base_path + "/" + self_employed_id

        response = await instance.client.request(method=HTTPMethodEnum.GET, path=path)
        return SelfEmployedResponse(**response)

    @classmethod
    async def create(
        cls, params: dict[str, Any] | SelfEmployedRequest, idempotency_key: uuid.UUID | None = None
    ) -> SelfEmployedResponse:
        """
        Создание сомозанятого

        :param params: Данные передаваемые в API
        :param idempotency_key: Ключ идемпотентности
        :return: Объект ответа SelfEmployedResponse, возвращаемого API при запросе информации о сомозанятом
        """
        instance = cls()

        path = cls.base_path

        headers = get_base_headers(idempotency_key=idempotency_key)

        if isinstance(params, dict):
            params_object = SelfEmployedRequest(**params)
        elif isinstance(params, SelfEmployedRequest):
            params_object = params
        else:
            raise TypeError("Invalid params value type")

        response = await instance.client.request(
            body=params_object, method=HTTPMethodEnum.POST, path=path, headers=headers
        )

        return SelfEmployedResponse(**response)

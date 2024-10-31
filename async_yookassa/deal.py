import uuid
from typing import Any

from async_yookassa.apiclient import APIClient
from async_yookassa.enums.request_methods import HTTPMethodEnum
from async_yookassa.models.deal_request import DealRequest
from async_yookassa.models.deal_response import DealListResponse, DealResponse
from async_yookassa.utils import get_base_headers


class Deal:
    """
    Класс, представляющий модель Deal.
    """

    base_path = "/deals"

    def __init__(self):
        self.client = APIClient()

    @classmethod
    async def find_one(cls, deal_id: str) -> DealResponse:
        """
        Возвращает информацию о сделке

        :param deal_id: Уникальный идентификатор сделки
        :return: Объект ответа DealResponse, возвращаемого API при запросе сделки
        """
        instance = cls()

        if not isinstance(deal_id, str):
            raise ValueError("Invalid payment_id value")

        path = instance.base_path + "/" + deal_id

        response = await instance.client.request(method=HTTPMethodEnum.GET, path=path)
        return DealResponse(**response)

    @classmethod
    async def create(
        cls, params: dict[str, Any] | DealRequest, idempotency_key: uuid.UUID | None = None
    ) -> DealResponse:
        """
        Создание сделки

        :param params: Данные передаваемые в API
        :param idempotency_key: Ключ идемпотентности
        :return: Объект ответа DealResponse, возвращаемого API при запросе сделки
        """
        instance = cls()

        path = cls.base_path

        headers = get_base_headers(idempotency_key=idempotency_key)

        if isinstance(params, dict):
            params_object = DealRequest(**params)
        elif isinstance(params, DealRequest):
            params_object = params
        else:
            raise TypeError("Invalid params value type")

        response = await instance.client.request(
            body=params_object, method=HTTPMethodEnum.POST, path=path, headers=headers
        )
        return DealResponse(**response)

    @classmethod
    async def list(cls, params: dict[str, str] | None = None) -> DealListResponse:
        """
        Возвращает список сделок

        :param params: Данные передаваемые в API
        :return: Объект ответа DealListResponse, возвращаемого API при запросе списка сделок
        """

        instance = cls()

        path = cls.base_path

        response = await instance.client.request(method=HTTPMethodEnum.GET, path=path, query_params=params)
        return DealListResponse(**response)

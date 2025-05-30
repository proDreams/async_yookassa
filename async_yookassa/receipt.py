import uuid
from typing import Any

from async_yookassa.apiclient import APIClient
from async_yookassa.enums.request_methods import HTTPMethodEnum
from async_yookassa.models.receipt_request import ReceiptListResponse, ReceiptRequest
from async_yookassa.models.receipt_response import ReceiptResponse
from async_yookassa.utils import get_base_headers


class Receipt:
    """
    Класс, представляющий модель Receipt.
    """

    base_path = "/receipts"

    def __init__(self):
        self.client = APIClient()

    @classmethod
    async def find_one(cls, receipt_id: str) -> ReceiptResponse:
        """
        Возвращает информацию о чеке

        :param receipt_id: Уникальный идентификатор чека
        :return: Объект ответа ReceiptResponse, возвращаемого API при запросе информации о чеке
        """
        instance = cls()
        if not isinstance(receipt_id, str):
            raise ValueError("Invalid payment_id value")

        path = instance.base_path + "/" + receipt_id

        response = await instance.client.request(method=HTTPMethodEnum.GET, path=path)
        return ReceiptResponse(**response)

    @classmethod
    async def create(
        cls, params: dict[str, Any] | ReceiptRequest, idempotency_key: uuid.UUID | None = None
    ) -> ReceiptResponse:
        """
        Создание чека

        :param params: Данные передаваемые в API
        :param idempotency_key: Ключ идемпотентности
        :return: Объект ответа ReceiptResponse, возвращаемого API при запросе информации о чеке
        """
        instance = cls()

        path = cls.base_path

        headers = get_base_headers(idempotency_key=idempotency_key)

        if isinstance(params, dict):
            params_object = ReceiptRequest(**params)
        elif isinstance(params, ReceiptRequest):
            params_object = params
        else:
            raise TypeError("Invalid params value type")

        response = await instance.client.request(
            body=params_object, method=HTTPMethodEnum.POST, path=path, headers=headers
        )
        return ReceiptResponse(**response)

    @classmethod
    async def list(cls, params: dict[str, str]) -> ReceiptListResponse:
        """
        Возвращает список чеков

        :param params: Данные передаваемые в API
        :return: Объект ответа ReceiptListResponse, возвращаемого API при запросе списка чеков
        """
        instance = cls()

        path = cls.base_path

        response = await instance.client.request(method=HTTPMethodEnum.GET, path=path, query_params=params)
        return ReceiptListResponse(**response)

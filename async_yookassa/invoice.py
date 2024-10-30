import uuid
from typing import Any

from async_yookassa.apiclient import APIClient
from async_yookassa.enums.request_methods import HTTPMethodEnum
from async_yookassa.models.invoice_request import InvoiceRequest
from async_yookassa.models.invoice_response import InvoiceResponse
from async_yookassa.utils import get_base_headers


class Invoice:
    """
    Класс, представляющий модель Invoice.
    """

    base_path = "/invoices"

    def __init__(self):
        self.client = APIClient()

    @classmethod
    async def find_one(cls, invoice_id: str) -> InvoiceResponse:
        """
        Возвращает информацию о счёте

        :param invoice_id: Уникальный идентификатор счёта
        :return: Объект ответа InvoiceResponse, возвращаемого API при запросе счёта
        """
        instance = cls()

        if not isinstance(invoice_id, str):
            raise ValueError("Invalid invoice_id value")

        path = instance.base_path + "/" + invoice_id

        response = await instance.client.request(method=HTTPMethodEnum.GET, path=path)
        return InvoiceResponse(**response)

    @classmethod
    async def create(
        cls, params: dict[str, Any] | InvoiceRequest, idempotency_key: uuid.UUID | None = None
    ) -> InvoiceResponse:
        """
        Создание счёта

        :param params: Данные передаваемые в API
        :param idempotency_key: Ключ идемпотентности
        :return: Объект ответа InvoiceResponse, возвращаемого API при запросе выплате
        """
        instance = cls()

        path = cls.base_path

        headers = get_base_headers(idempotency_key=idempotency_key)

        if isinstance(params, dict):
            params_object = InvoiceRequest(**params)
        elif isinstance(params, InvoiceRequest):
            params_object = params
        else:
            raise TypeError("Invalid params value type")

        response = await instance.client.request(
            body=params_object, method=HTTPMethodEnum.POST, path=path, headers=headers
        )
        return InvoiceResponse(**response)

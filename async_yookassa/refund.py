import uuid
from typing import Any

from async_yookassa.apiclient import APIClient
from async_yookassa.enums.request_methods import HTTPMethodEnum
from async_yookassa.models.refund_request import RefundRequest
from async_yookassa.models.refund_response import RefundResponse
from async_yookassa.utils import get_base_headers


class Refund:
    """
    Класс, представляющий модель Refund.
    """

    base_path = "/refunds"

    def __init__(self):
        self.client = APIClient()

    @classmethod
    async def create(cls, params: dict[str, Any] | RefundRequest, idempotency_key: uuid.UUID | None = None):
        """
        Создание возврата

        :param params: Данные передаваемые в API
        :param idempotency_key: Ключ идемпотентности
        :return: Объект ответа RefundResponse, возвращаемого API при запросе информации о возврате
        """
        instance = cls()

        path = cls.base_path

        headers = get_base_headers(idempotency_key=idempotency_key)

        if isinstance(params, dict):
            params_object = RefundRequest(**params)
        elif isinstance(params, RefundRequest):
            params_object = params
        else:
            raise TypeError("Invalid params value type")

        response = await instance.client.request(
            body=params_object, method=HTTPMethodEnum.POST, path=path, headers=headers
        )

        return RefundResponse(**response)

import uuid
from typing import Any

from async_yookassa.apiclient import APIClient
from async_yookassa.enums.request_methods import HTTPMethodEnum
from async_yookassa.models.payout_request import PayoutRequest
from async_yookassa.models.payout_response import PayoutResponse
from async_yookassa.utils import get_base_headers


class Payout:
    """
    Класс, представляющий модель Payout.
    """

    base_path = "/payouts"

    def __init__(self):
        self.client = APIClient()

    @classmethod
    async def find_one(cls, payout_id: str) -> PayoutResponse:
        """
        Возвращает информацию о выплате

        :param payout_id: Уникальный идентификатор выплаты
        :return: Объект ответа PayoutResponse, возвращаемого API при запросе выплаты
        """
        instance = cls()

        if not isinstance(payout_id, str):
            raise ValueError("Invalid payout_id value")

        path = instance.base_path + "/" + payout_id

        response = await instance.client.request(method=HTTPMethodEnum.GET, path=path)

        return PayoutResponse(**response)

    @classmethod
    async def create(
        cls, params: dict[str, Any] | PayoutRequest, idempotency_key: uuid.UUID | None = None
    ) -> PayoutResponse:
        """
        Создание выплаты

        :param params: Данные передаваемые в API
        :param idempotency_key: Ключ идемпотентности
        :return: Объект ответа PayoutResponse, возвращаемого API при запросе выплате
        """
        instance = cls()
        path = cls.base_path

        headers = get_base_headers(idempotency_key=idempotency_key)

        if isinstance(params, dict):
            params_object = PayoutRequest(**params)
        elif isinstance(params, PayoutRequest):
            params_object = params
        else:
            raise TypeError("Invalid params value type")

        response = await instance.client.request(
            body=params_object, method=HTTPMethodEnum.POST, path=path, headers=headers
        )
        return PayoutResponse(**response)

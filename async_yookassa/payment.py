import uuid
from typing import Any

from async_yookassa.apiclient import APIClient
from async_yookassa.enums.request_methods_enum import HTTPMethodEnum
from async_yookassa.models.payment_capture_model import CapturePaymentRequest
from async_yookassa.models.payment_list_response_model import PaymentListResponse
from async_yookassa.models.payment_request_model import PaymentRequest
from async_yookassa.models.payment_response_model import PaymentResponse


class Payment:
    """
    Класс, представляющий модель Payment.
    """

    base_path = "/payments"

    CMS_NAME = "async_yookassa_python"

    def __init__(self):
        self.client = APIClient()

    @classmethod
    async def find_one(cls, payment_id: str) -> PaymentResponse:
        """
        Возвращает информацию о платеже

        :param payment_id: Уникальный идентификатор платежа
        :return: Объект ответа PaymentResponse, возвращаемого API при запросе платежа
        """
        instance = cls()
        if not isinstance(payment_id, str):
            raise ValueError("Invalid payment_id value")

        path = instance.base_path + "/" + payment_id

        response = await instance.client.request(method=HTTPMethodEnum.GET, path=path)
        return PaymentResponse(**response)

    @classmethod
    async def create(
        cls, params: dict[str, Any] | PaymentRequest, idempotency_key: uuid.UUID | None = None
    ) -> PaymentResponse:
        """
        Создание платежа

        :param params: Данные передаваемые в API
        :param idempotency_key: Ключ идемпотентности
        :return: Объект ответа PaymentResponse, возвращаемого API при запросе платежа
        """
        instance = cls()

        path = instance.base_path

        headers = cls.get_base_headers(idempotency_key=idempotency_key)

        if isinstance(params, dict):
            params_object = PaymentRequest(**params)
        elif isinstance(params, PaymentRequest):
            params_object = params
        else:
            raise TypeError("Invalid params value type")

        params_object = instance.add_default_cms_name(params_object=params_object)

        response = await instance.client.request(
            body=params_object, method=HTTPMethodEnum.POST, path=path, query_params=None, headers=headers
        )
        return PaymentResponse(**response)

    @classmethod
    async def capture(
        cls,
        payment_id: str,
        params: dict[str, Any] | CapturePaymentRequest | None = None,
        idempotency_key: uuid.UUID | None = None,
    ):
        """
        Подтверждение платежа

        :param payment_id: Уникальный идентификатор платежа
        :param params: Данные передаваемые в API
        :param idempotency_key: Ключ идемпотентности
        :return: Объект ответа PaymentResponse, возвращаемого API при запросе платежа
        """
        instance = cls()
        if not isinstance(payment_id, str):
            raise ValueError("Invalid payment_id value")

        path = instance.base_path + "/" + payment_id + "/capture"

        headers = cls.get_base_headers(idempotency_key=idempotency_key)

        if isinstance(params, dict):
            params_object = CapturePaymentRequest(**params)
        elif isinstance(params, CapturePaymentRequest):
            params_object = params
        else:
            params_object = None

        response = await instance.client.request(
            body=params_object, method=HTTPMethodEnum.POST, path=path, headers=headers
        )
        return PaymentResponse(**response)

    @classmethod
    async def cancel(cls, payment_id: str, idempotency_key: uuid.UUID | None = None):
        """
        Отмена платежа

        :param payment_id: Уникальный идентификатор платежа
        :param idempotency_key: Ключ идемпотентности
        :return: Объект ответа PaymentResponse, возвращаемого API при запросе платежа
        """
        instance = cls()
        if not isinstance(payment_id, str):
            raise ValueError("Invalid payment_id value")

        path = instance.base_path + "/" + payment_id + "/cancel"

        headers = cls.get_base_headers(idempotency_key=idempotency_key)

        response = await instance.client.request(method=HTTPMethodEnum.POST, path=path, headers=headers)
        return PaymentResponse(**response)

    @classmethod
    async def list(cls, params: dict[str, Any] | None = None):
        """
        Возвращает список платежей

        :param params: Данные передаваемые в API
        :return: Объект ответа PaymentListResponse, возвращаемого API при запросе списка платежей
        """
        instance = cls()

        path = cls.base_path

        response = await instance.client.request(method=HTTPMethodEnum.GET, path=path, query_params=params)
        return PaymentListResponse(**response)

    @staticmethod
    def get_base_headers(idempotency_key: uuid.UUID | None = None) -> dict[str, str]:
        if not idempotency_key:
            idempotency_key = uuid.uuid4()
        return {"Idempotence-Key": str(idempotency_key)}

    def add_default_cms_name(self, params_object: PaymentRequest) -> PaymentRequest:
        """
        Добавляет cms_name в metadata со значением по умолчанию

        :param params_object: Данные передаваемые в API
        :return: PaymentRequest Объект запроса к API
        """
        if not params_object.metadata:
            params_object.metadata = {"cms_name": self.CMS_NAME}

        if "cms_name" not in params_object.metadata:
            params_object.metadata["cms_name"] = self.CMS_NAME

        return params_object

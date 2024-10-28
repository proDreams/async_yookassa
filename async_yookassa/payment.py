import uuid
from typing import Any

from async_yookassa.apiclient import APIClient
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
    async def create(cls, params: dict[str, Any], idempotency_key: uuid.UUID = None) -> PaymentResponse:
        """
        Создание платежа

        :param params: Данные передаваемые в API
        :param idempotency_key: Ключ идемпотентности
        :return: PaymentResponse Объект ответа, возвращаемого API при запросе платежа
        """
        instance = cls()
        path = cls.base_path

        if not idempotency_key:
            idempotency_key = uuid.uuid4()

        headers = {"Idempotence-Key": str(idempotency_key)}

        if isinstance(params, dict):
            params_object = PaymentRequest(**params)
        elif isinstance(params, PaymentRequest):
            params_object = params
        else:
            raise TypeError("Invalid params value type")

        params_object = instance.add_default_cms_name(params_object)

        response = await instance.client.request(
            body=params_object, method="POST", path=path, query_params=None, headers=headers
        )
        return PaymentResponse(**response)

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

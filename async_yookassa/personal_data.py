import uuid
from typing import Any

from async_yookassa.apiclient import APIClient
from async_yookassa.enums.request_methods import HTTPMethodEnum
from async_yookassa.models.personal_data_request import PersonalDataRequest
from async_yookassa.models.personal_data_response import PersonalDataResponse
from async_yookassa.utils import get_base_headers


class PersonalData:
    """
    Класс, представляющий модель PersonalData.
    """

    base_path = "/personal_data"

    def __init__(self):
        self.client = APIClient()

    @classmethod
    async def find_one(cls, personal_data_id: str) -> PersonalDataResponse:
        """
        Возвращает информацию о персональных данных

        :param personal_data_id: Уникальный идентификатор персональных данных
        :return: Объект ответа PersonalDataResponse, возвращаемого API при запросе персональных данных
        """
        instance = cls()

        if not isinstance(personal_data_id, str):
            raise ValueError("Invalid personal_data_id value")

        path = instance.base_path + "/" + personal_data_id

        response = await instance.client.request(method=HTTPMethodEnum.GET, path=path)
        return PersonalDataResponse(**response)

    @classmethod
    async def create(
        cls, params: dict[str, Any] | PersonalDataRequest, idempotency_key: uuid.UUID | None = None
    ) -> PersonalDataResponse:
        """
        Создание персональных данных

        :param params: Данные передаваемые в API
        :param idempotency_key: Ключ идемпотентности
        :return: Объект ответа PersonalDataResponse, возвращаемого API при запросе персональных данных
        """
        instance = cls()

        path = cls.base_path

        headers = get_base_headers(idempotency_key=idempotency_key)

        if isinstance(params, dict):
            params_object = PersonalDataRequest(**params)
        elif isinstance(params, PersonalDataRequest):
            params_object = params
        else:
            raise TypeError("Invalid params value type")

        response = await instance.client.request(
            body=params_object, method=HTTPMethodEnum.POST, path=path, headers=headers
        )
        return PersonalDataResponse(**response)

from base64 import b64encode
from typing import Any

from httpx import AsyncClient, Response

from async_yookassa import Configuration
from async_yookassa.exceptions.api_error import APIError
from async_yookassa.exceptions.bad_request_error import BadRequestError
from async_yookassa.exceptions.forbidden_error import ForbiddenError
from async_yookassa.exceptions.not_found_error import NotFoundError
from async_yookassa.exceptions.response_processing_error import ResponseProcessingError
from async_yookassa.exceptions.too_many_request_error import TooManyRequestsError
from async_yookassa.exceptions.unauthorized_error import UnauthorizedError
from async_yookassa.models.deal_request import DealRequest
from async_yookassa.models.invoice_request import InvoiceRequest
from async_yookassa.models.payment_request import PaymentRequest
from async_yookassa.models.payout_request import PayoutRequest
from async_yookassa.models.personal_data_request import PersonalDataRequest
from async_yookassa.models.receipt_request import ReceiptRequest
from async_yookassa.models.refund_request import RefundRequest
from async_yookassa.models.self_employed_request import SelfEmployedRequest
from async_yookassa.models.user_agent import UserAgent
from async_yookassa.models.webhook_request import WebhookRequest


class APIClient:
    """
    Класс клиента API.
    """

    def __init__(self):
        self.configuration = Configuration.instantiate()
        self.endpoint = Configuration.api_endpoint()
        self.account_id = self.configuration.account_id
        self.secret_key = self.configuration.secret_key
        self.auth_token = self.configuration.auth_token
        self.async_client = AsyncClient(timeout=self.configuration.timeout)

        self.user_agent = UserAgent()
        if self.configuration.agent_framework:
            self.user_agent.framework = self.configuration.agent_framework
        if self.configuration.agent_cms:
            self.user_agent.cms = self.configuration.agent_cms
        if self.configuration.agent_module:
            self.user_agent.module = self.configuration.agent_module

    async def request(
        self,
        body: (
            PaymentRequest
            | InvoiceRequest
            | RefundRequest
            | ReceiptRequest
            | PayoutRequest
            | SelfEmployedRequest
            | PersonalDataRequest
            | DealRequest
            | WebhookRequest
            | None
        ) = None,
        method: str = "",
        path: str = "",
        query_params: dict[str, str] | None = None,
        headers: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        """
        Подготовка запроса.

        :param method: HTTP метод
        :param path: URL запроса
        :param query_params: Словарь GET параметров запроса
        :param headers: Словарь заголовков запроса
        :param body: Тело запроса
        :return: Ответ на запрос в формате JSON
        """
        if isinstance(body, PaymentRequest):
            body = body.model_dump()

        request_headers = self.prepare_request_headers(headers=headers)
        raw_response = await self.execute(
            body=body, method=method, path=path, query_params=query_params, request_headers=request_headers
        )

        if raw_response.status_code != 200:
            self.__handle_error(raw_response=raw_response)

        return raw_response.json()

    async def execute(
        self,
        method: str,
        path: str,
        request_headers: dict[str, str],
        query_params: dict[str, str] | None = None,
        body: dict[str, Any] | None = None,
    ) -> Response:
        """
        Выполнение запроса.

        :param body: Тело запроса
        :param method: HTTP метод
        :param path: URL запроса
        :param query_params: Массив GET параметров запроса
        :param request_headers: Массив заголовков запроса
        :return: Response
        """
        async with self.async_client as client:
            # self.log_request(body, method, path, query_params, request_headers)

            raw_response = await client.request(
                method=method, url=self.endpoint + path, params=query_params, headers=request_headers, json=body
            )

            # self.log_response(raw_response.content, self.get_response_info(raw_response), raw_response.headers)

        return raw_response

    def prepare_request_headers(self, headers: dict[str, str]) -> dict[str, str]:
        """
        Подготовка заголовков запроса.

        :param headers: Словарь заголовков запроса
        :return: Словарь заголовков запроса
        """
        request_headers = {"Content-type": "application/json"}
        if self.auth_token is not None:
            auth_headers = {"Authorization": "Bearer " + self.auth_token}
        else:
            auth_headers = {"Authorization": self.basic_auth(self.account_id, self.secret_key)}

        request_headers.update(auth_headers)

        request_headers.update({"YM-User-Agent": self.user_agent.get_header_string()})

        if isinstance(headers, dict):
            request_headers.update(headers)
        return request_headers

    @staticmethod
    def basic_auth(username: str, password: str) -> str:
        """
        Формирование токена для Basic авторизации.

        :param username: Идентификатор аккаунта
        :param password: Секретный ключ магазина
        :return: Строка авторизации
        """
        token = b64encode(f"{username}:{password}".encode()).decode("ascii")
        return f"Basic {token}"

    @staticmethod
    def __handle_error(raw_response: Response) -> None:
        """
        Выбрасывает исключение по коду ошибки.
        """
        http_code = raw_response.status_code
        if http_code == BadRequestError.HTTP_CODE:
            raise BadRequestError(raw_response.json())
        elif http_code == ForbiddenError.HTTP_CODE:
            raise ForbiddenError(raw_response.json())
        elif http_code == NotFoundError.HTTP_CODE:
            raise NotFoundError(raw_response.json())
        elif http_code == TooManyRequestsError.HTTP_CODE:
            raise TooManyRequestsError(raw_response.json())
        elif http_code == UnauthorizedError.HTTP_CODE:
            raise UnauthorizedError(raw_response.json())
        elif http_code == ResponseProcessingError.HTTP_CODE:
            raise ResponseProcessingError(raw_response.json())
        else:
            raise APIError(raw_response.text)

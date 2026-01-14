"""Internal HTTP utilities for YooKassaClient."""

from base64 import b64encode
from typing import Any

from httpx import AsyncClient, Response

from async_yookassa._config import ClientConfig
from async_yookassa.exceptions.api_error import APIError
from async_yookassa.exceptions.bad_request_error import BadRequestError
from async_yookassa.exceptions.forbidden_error import ForbiddenError
from async_yookassa.exceptions.not_found_error import NotFoundError
from async_yookassa.exceptions.response_processing_error import ResponseProcessingError
from async_yookassa.exceptions.too_many_request_error import TooManyRequestsError
from async_yookassa.exceptions.unauthorized_error import UnauthorizedError


class HttpClient:
    """Внутренний HTTP клиент для работы с YooKassa API."""

    def __init__(
        self,
        config: ClientConfig,
        http_client: AsyncClient,
        user_agent_header: str,
    ) -> None:
        self._config = config
        self._http = http_client
        self._user_agent = user_agent_header

    async def request(
        self,
        method: str,
        path: str,
        body: dict[str, Any] | None = None,
        query_params: dict[str, str] | None = None,
        headers: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        """
        Выполнение HTTP запроса к API YooKassa.

        :param method: HTTP метод (GET, POST, PUT, DELETE)
        :param path: Относительный путь запроса (например, /payments)
        :param body: Тело запроса (словарь, будет преобразован в JSON)
        :param query_params: GET параметры запроса
        :param headers: Дополнительные заголовки запроса
        :return: Ответ от API в виде словаря
        :raises APIError: При ошибках API
        """
        request_headers = self._prepare_headers(headers)
        url = self._config.api_url + path

        response = await self._http.request(
            method=method,
            url=url,
            params=query_params,
            headers=request_headers,
            json=body,
        )

        if response.status_code != 200:
            self._handle_error(response)

        return response.json()

    def _prepare_headers(self, extra_headers: dict[str, str] | None) -> dict[str, str]:
        """
        Подготовка заголовков для запроса.

        Добавляет Authorization и YM-User-Agent.
        """
        headers = {
            "Content-Type": "application/json",
            "YM-User-Agent": self._user_agent,
        }

        # Авторизация
        if self._config.is_oauth:
            headers["Authorization"] = f"Bearer {self._config.auth_token}"
        else:
            token = b64encode(f"{self._config.account_id}:{self._config.secret_key}".encode()).decode("ascii")
            headers["Authorization"] = f"Basic {token}"

        if extra_headers:
            headers.update(extra_headers)

        return headers

    @staticmethod
    def _handle_error(response: Response) -> None:
        """
        Обработка ошибок HTTP ответа.

        :param response: Объект ответа httpx
        :raises: Соответствующее исключение из async_yookassa.exceptions
        """
        status = response.status_code

        error_map = {
            BadRequestError.HTTP_CODE: BadRequestError,
            ForbiddenError.HTTP_CODE: ForbiddenError,
            NotFoundError.HTTP_CODE: NotFoundError,
            TooManyRequestsError.HTTP_CODE: TooManyRequestsError,
            UnauthorizedError.HTTP_CODE: UnauthorizedError,
            ResponseProcessingError.HTTP_CODE: ResponseProcessingError,
        }

        error_class = error_map.get(status)
        if error_class:
            raise error_class(response.json())

        raise APIError(response.text)

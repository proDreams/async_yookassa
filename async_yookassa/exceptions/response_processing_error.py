from async_yookassa.exceptions.api_error import APIError


class ResponseProcessingError(APIError):
    """
    Запрос был принят на обработку, но она не завершена.
    """

    HTTP_CODE = 202

from async_yookassa.exceptions.api_error import APIError


class NotFoundError(APIError):
    """
    Ресурс не найден.
    """

    HTTP_CODE = 404

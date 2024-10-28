from async_yookassa.exceptions.api_error import APIError


class AuthorizeError(APIError):
    """
    Ошибка авторизации. Не установлен заголовок.
    """

    pass

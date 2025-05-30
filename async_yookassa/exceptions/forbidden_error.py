from async_yookassa.exceptions.api_error import APIError


class ForbiddenError(APIError):
    """
    Секретный ключ или OAuth-токен верный, но не хватает прав для совершения операции.
    """

    HTTP_CODE = 403

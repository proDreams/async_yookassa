from async_yookassa.exceptions.api_error import APIError


class UnauthorizedError(APIError):
    """
    [Basic Auth] Неверный идентификатор вашего аккаунта в ЮKassa или секретный ключ
    (имя пользователя и пароль при аутентификации).
    [OAuth 2.0] Невалидный OAuth-токен: он некорректный, устарел или его отозвали. Запросите токен заново.
    """

    HTTP_CODE = 401

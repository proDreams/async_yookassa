from async_yookassa.exceptions.api_error import APIError


class BadRequestError(APIError):
    """
    Неправильный запрос. Чаще всего этот статус выдается из-за нарушения правил взаимодействия с API.
    """

    HTTP_CODE = 400

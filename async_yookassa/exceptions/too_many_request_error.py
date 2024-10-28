from async_yookassa.exceptions.api_error import APIError


class TooManyRequestsError(APIError):
    """
    Превышен лимит запросов в единицу времени. Попробуйте снизить интенсивность запросов.
    """

    HTTP_CODE = 429

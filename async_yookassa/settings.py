from async_yookassa.apiclient import APIClient
from async_yookassa.enums.request_methods import HTTPMethodEnum
from async_yookassa.models.me import Me


class Settings:
    """
    Класс, представляющий модель Settings.
    """

    base_path = "/me"

    def __init__(self):
        self.client = APIClient()

    @classmethod
    async def get_account_settings(cls, params: dict[str, str] | None = None) -> Me:
        """
        Возвращает информацию о магазине

        :param params: (dict | None) Параметры поиска.
            В настоящее время доступен только {'on_behalf_of': account_id}
        :return: Me Информация о настройках магазина или шлюза
        """
        instance = cls()
        path = cls.base_path

        response = await instance.client.request(method=HTTPMethodEnum.GET, path=path, query_params=params)
        return Me(**response)

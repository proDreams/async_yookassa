from async_yookassa.apiclient import APIClient
from async_yookassa.enums.request_methods import HTTPMethodEnum
from async_yookassa.models.sbp_banks_response import SbpBankListResponse


class SbpBanks:
    """
    Класс, представляющий модель SbpBanks.
    """

    base_path = "/sbp_banks"

    def __init__(self):
        self.client = APIClient()

    @classmethod
    async def list(cls) -> SbpBankListResponse:
        """
        Возвращает список участников СБП

        :return: Объект ответа SbpBankListResponse, возвращаемого API при запросе списка участников СБП
        """
        instance = cls()

        path = cls.base_path

        response = await instance.client.request(method=HTTPMethodEnum.GET, path=path)

        return SbpBankListResponse(**response)

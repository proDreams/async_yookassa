"""SBP Banks service for YooKassa API."""

from async_yookassa.models.sbp_bank import SbpBankListResponse
from async_yookassa.services.base import BaseService


class SBPBanksService(BaseService):
    """
    Сервис для работы с участниками СБП.

    Использование:
    ```python
    async with YooKassaClient(...) as client:
        # Получение списка банков
        banks = await client.sbp_bank.list()
    ```
    """

    BASE_PATH = "/sbp_banks"

    async def list(self) -> SbpBankListResponse:
        """
        Получение списка банков-участников СБП.

        :return: Объект ответа SbpBankListResponse
        """

        response = await self._get(self.BASE_PATH)
        return SbpBankListResponse(**response)

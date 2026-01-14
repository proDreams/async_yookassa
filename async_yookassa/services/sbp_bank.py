"""SBP Banks service for YooKassa API."""

from async_yookassa.models.sbp_bank.response import SbpBankListResponse
from async_yookassa.services.base import BaseService


class SBPBanksService(BaseService):
    """Сервис для работы с участниками СБП."""

    BASE_PATH = "/sbp_banks"

    async def list(self) -> SbpBankListResponse:
        """
        placeholder
        """

        response = await self._get(self.BASE_PATH)
        return SbpBankListResponse(**response)

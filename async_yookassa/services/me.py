"""Me service for YooKassa API."""

from async_yookassa.models.me import MeResponse
from async_yookassa.services.base import BaseService


class MeService(BaseService):
    """Сервис для работы с настройками."""

    BASE_PATH = "/me"

    async def get_me(self, on_behalf_of: str | None = None) -> MeResponse:
        """
        plaseholder
        """

        query_params = None
        if on_behalf_of is not None:
            query_params = {"on_behalf_of": on_behalf_of}

        response = await self._get(f"{self.BASE_PATH}", query_params=query_params)
        return MeResponse(**response)

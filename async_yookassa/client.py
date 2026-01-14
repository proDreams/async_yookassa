"""Main async client for YooKassa API."""

import platform
import sys
from typing import TYPE_CHECKING, Self

import distro
from httpx import AsyncClient

from async_yookassa._config import ClientConfig
from async_yookassa._http import HttpClient

if TYPE_CHECKING:
    from async_yookassa.services.deal import DealService
    from async_yookassa.services.invoice import InvoiceService
    from async_yookassa.services.me import MeService
    from async_yookassa.services.payment import PaymentService
    from async_yookassa.services.payment_methods import PaymentMethodsService
    from async_yookassa.services.payout import PayoutService
    from async_yookassa.services.personal_data import PersonalDataService
    from async_yookassa.services.receipt import ReceiptService
    from async_yookassa.services.refund import RefundService
    from async_yookassa.services.sbp_bank import SBPBanksService
    from async_yookassa.services.webhook import WebhookService


class YooKassaClient:
    """
    Асинхронный клиент YooKassa API.

    Рекомендуемый способ использования:

    ```python
    async with YooKassaClient(account_id="...", secret_key="...") as client:
        payment = await client.payment.create(PaymentRequest(...))
    ```

    Или с OAuth:

    ```python
    async with YooKassaClient(auth_token="...") as client:
        payment = await client.payment.find_one("payment_id")
    ```
    """

    __version__ = "1.0.0"

    def __init__(
        self,
        account_id: str | None = None,
        secret_key: str | None = None,
        auth_token: str | None = None,
        *,
        timeout: int = 30,
        api_url: str = "https://api.yookassa.ru/v3",
        http_client: AsyncClient | None = None,
    ) -> None:
        """
        Инициализация клиента.

        :param account_id: Идентификатор магазина (для Basic Auth)
        :param secret_key: Секретный ключ (для Basic Auth)
        :param auth_token: OAuth токен
        :param timeout: Таймаут запросов в секундах
        :param api_url: URL API (по умолчанию продакшн)
        :param http_client: Кастомный AsyncClient (опционально)
        """
        self._config = ClientConfig(
            account_id=account_id,
            secret_key=secret_key,
            auth_token=auth_token,
            api_url=api_url,
        )
        self._http = http_client or AsyncClient(timeout=timeout)
        self._owns_http = http_client is None

        self._http_client = HttpClient(
            config=self._config,
            http_client=self._http,
            user_agent_header=self._build_user_agent(),
        )

        self._payment: PaymentService | None = None
        self._payment_methods: PaymentMethodsService | None = None
        self._personal_data: PersonalDataService | None = None
        self._refund: RefundService | None = None
        self._receipt: ReceiptService | None = None
        self._payout: PayoutService | None = None
        self._invoice: InvoiceService | None = None
        self._deal: DealService | None = None
        self._webhook: WebhookService | None = None
        self._me: MeService | None = None
        self._sbp_bank: SBPBanksService | None = None

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, *args) -> None:
        await self.close()

    async def close(self) -> None:
        """Закрывает HTTP клиент (если он был создан внутри класса)."""
        if self._owns_http:
            await self._http.aclose()

    @property
    def payment(self) -> PaymentService:
        """Сервис для работы с платежами."""
        if self._payment is None:
            from async_yookassa.services.payment import PaymentService

            self._payment = PaymentService(self._http_client)
        return self._payment

    @property
    def payment_methods(self) -> PaymentMethodsService:
        """Сервис для работы со способами оплаты."""
        if self._payment_methods is None:
            from async_yookassa.services.payment_methods import PaymentMethodsService

            self._payment_methods = PaymentMethodsService(self._http_client)
        return self._payment_methods

    @property
    def refund(self) -> RefundService:
        """Сервис для работы с возвратами."""
        if self._refund is None:
            from async_yookassa.services.refund import RefundService

            self._refund = RefundService(self._http_client)
        return self._refund

    @property
    def receipt(self) -> ReceiptService:
        """Сервис для работы с чеками."""
        if self._receipt is None:
            from async_yookassa.services.receipt import ReceiptService

            self._receipt = ReceiptService(self._http_client)
        return self._receipt

    @property
    def payout(self) -> PayoutService:
        """Сервис для работы с выплатами."""
        if self._payout is None:
            from async_yookassa.services.payout import PayoutService

            self._payout = PayoutService(self._http_client)
        return self._payout

    @property
    def invoice(self) -> InvoiceService:
        """Сервис для работы со счетами."""
        if self._invoice is None:
            from async_yookassa.services.invoice import InvoiceService

            self._invoice = InvoiceService(self._http_client)
        return self._invoice

    @property
    def deal(self) -> DealService:
        """Сервис для работы со сделками."""
        if self._deal is None:
            from async_yookassa.services.deal import DealService

            self._deal = DealService(self._http_client)
        return self._deal

    @property
    def webhook(self) -> WebhookService:
        """Сервис для работы с вебхуками."""
        if self._webhook is None:
            from async_yookassa.services.webhook import WebhookService

            self._webhook = WebhookService(self._http_client)
        return self._webhook

    @property
    def me(self) -> MeService:
        """Сервис для получения информации о магазине."""
        if self._me is None:
            from async_yookassa.services.me import MeService

            self._me = MeService(self._http_client)
        return self._me

    @property
    def personal_data(self) -> PersonalDataService:
        """Сервис для работы с персональными данными."""
        if self._personal_data is None:
            from async_yookassa.services.personal_data import PersonalDataService

            self._personal_data = PersonalDataService(self._http_client)
        return self._personal_data

    @property
    def sbp_bank(self) -> SBPBanksService:
        """Сервис для получения списка банков-участников СБП."""
        if self._sbp_bank is None:
            from async_yookassa.services.sbp_bank import SBPBanksService

            self._sbp_bank = SBPBanksService(self._http_client)
        return self._sbp_bank

    def _build_user_agent(self) -> str:
        """Формирует User-Agent строку."""
        parts = [
            self._get_os_info(),
            f"Python/{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}",
            f"Async YooKassa Python/{self.__version__}",
        ]
        return " ".join(parts)

    @staticmethod
    def _get_os_info() -> str:
        """Определяет информацию об ОС."""
        system = platform.system()
        if system == "Linux":
            return f"{distro.name().capitalize()}/{distro.version()}"
        return f"{system}/{platform.release()}"

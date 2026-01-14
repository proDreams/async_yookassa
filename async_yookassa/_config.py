"""Internal configuration for YooKassaClient."""

from dataclasses import dataclass

from async_yookassa.exceptions.configuration_errors import ConfigurationError


@dataclass(frozen=True, slots=True)
class ClientConfig:
    """
    Конфигурация клиента YooKassa API.

    Использует либо Basic Auth (account_id + secret_key),
    либо OAuth (auth_token), но не оба одновременно.
    """

    account_id: str | None = None
    secret_key: str | None = None
    auth_token: str | None = None
    api_url: str = "https://api.yookassa.ru/v3"

    def __post_init__(self) -> None:
        self._validate()

    def _validate(self) -> None:
        """Проверка корректности конфигурации."""
        has_basic = self.account_id is not None and self.secret_key is not None
        has_token = self.auth_token is not None

        if not has_basic and not has_token:
            raise ConfigurationError("Either (account_id, secret_key) or auth_token is required")

        if has_basic and has_token:
            raise ConfigurationError("Cannot use both basic auth and auth_token")

    @property
    def is_oauth(self) -> bool:
        """
        Проверяет использование OAuth авторизации.

        :return: True, если установлен auth_token, иначе False.
        """
        return self.auth_token is not None

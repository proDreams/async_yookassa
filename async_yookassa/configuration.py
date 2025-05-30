from dataclasses import dataclass
from typing import Self

from async_yookassa.exceptions.configuration_errors import ConfigurationError
from async_yookassa.models.configuration_submodels.version import Version


@dataclass
class Configuration:
    api_url: str = "https://api.yookassa.ru/v3"
    account_id: str | None = None
    secret_key: str | None = None
    timeout: int = 1800
    max_attempts: int = 3
    auth_token: str | None = None
    agent_framework: Version | None = None
    agent_cms: Version | None = None
    agent_module: Version | None = None

    def __post_init__(self):
        self.assert_has_api_credentials()

    @classmethod
    def configure(cls, account_id: str, secret_key: str, **kwargs) -> None:
        """
        Устанавливает настройки конфигурации для базовой авторизации.

        :param account_id: Идентификатор магазина.
        :param secret_key: Секретный ключ.
        :param kwargs: Словарь с дополнительными параметрами.
        """
        cls.account_id = account_id
        cls.secret_key = secret_key
        cls.auth_token = None
        cls.api_url = kwargs.get("api_url", cls.api_url)
        cls.timeout = kwargs.get("timeout", cls.timeout)
        cls.max_attempts = kwargs.get("max_attempts", cls.max_attempts)

    @classmethod
    def configure_auth_token(cls, token: str, **kwargs) -> None:
        """
        Устанавливает настройки конфигурации для авторизации по OAuth.

        :param token: Ключ OAuth.
        :param kwargs: Словарь с дополнительными параметрами.
        """
        cls.account_id = None
        cls.secret_key = None
        cls.auth_token = token
        cls.api_url = kwargs.get("api_url", cls.api_url)
        cls.timeout = kwargs.get("timeout", cls.timeout)
        cls.max_attempts = kwargs.get("max_attempts", cls.max_attempts)

    def configure_user_agent(
        self, framework: Version | None = None, cms: Version | None = None, module: Version | None = None
    ) -> None:
        """
        Устанавливает настройки конфигурации для User-Agent.

        :param framework: Версия фреймворка.
        :param cms: Версия CMS.
        :param module: Версия модуля.
        """
        if isinstance(framework, Version):
            self.agent_framework = framework
        if isinstance(cms, Version):
            self.agent_cms = cms
        if isinstance(module, Version):
            self.agent_module = module

    @classmethod
    def instantiate(cls) -> Self:
        """
        Получение объекта конфигурации.

        :return: Объект конфигурации
        """
        return cls(
            account_id=cls.account_id,
            secret_key=cls.secret_key,
            timeout=cls.timeout,
            max_attempts=cls.max_attempts,
            auth_token=cls.auth_token,
            agent_framework=cls.agent_framework,
            agent_cms=cls.agent_cms,
            agent_module=cls.agent_module,
            api_url=cls.api_url,
        )

    @staticmethod
    def api_endpoint() -> str:
        """Возвращает URL для API Кассы."""
        return Configuration.api_url

    def has_api_credentials(self) -> bool:
        """Проверка наличия параметров базовой авторизации."""
        return self.account_id is not None and self.secret_key is not None

    def assert_has_api_credentials(self) -> None:
        """Проверка наличия API параметров, выброс исключения ConfigurationError при ошибке."""
        if self.auth_token is None and not self.has_api_credentials():
            raise ConfigurationError("account_id and secret_key are required")
        elif self.auth_token and self.has_api_credentials():
            raise ConfigurationError("Could not configure authorization with both auth_token and basic auth")

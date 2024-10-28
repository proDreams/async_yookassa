from async_yookassa.exceptions.configuration_errors import ConfigurationError
from async_yookassa.models.configuration_submodels.version_model import Version


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
    verify: str | None = None

    def __init__(self, **kwargs):
        self.assert_has_api_credentials()

    @staticmethod
    async def configure(account_id: str, secret_key: str, **kwargs) -> None:
        """
        Устанавливает настройки конфигурации для базовой авторизации.

        :param account_id: Идентификатор магазина.
        :param secret_key: Секретный ключ.
        :param kwargs: Словарь с дополнительными параметрами.
        """
        Configuration._account_id = account_id
        Configuration.secret_key = secret_key
        Configuration.auth_token = None
        Configuration.api_url = kwargs.get("api_url", "https://api.yookassa.ru/v3")
        Configuration.timeout = kwargs.get("timeout", 1800)
        Configuration.max_attempts = kwargs.get("max_attempts", 3)
        Configuration.verify = kwargs.get("verify", None)

    @staticmethod
    async def configure_auth_token(token: str, **kwargs) -> None:
        """
        Устанавливает настройки конфигурации для авторизации по OAuth.

        :param token: Ключ OAuth.
        :param kwargs: Словарь с дополнительными параметрами.
        """
        Configuration.account_id = None
        Configuration.secret_key = None
        Configuration.auth_token = token
        Configuration.api_url = kwargs.get("api_url", "https://api.yookassa.ru/v3")
        Configuration.timeout = kwargs.get("timeout", 1800)
        Configuration.max_attempts = kwargs.get("max_attempts", 3)
        Configuration.verify = kwargs.get("verify", None)

    @staticmethod
    async def configure_user_agent(
        framework: Version | None = None, cms: Version | None = None, module: Version | None = None
    ) -> None:
        """
        Устанавливает настройки конфигурации для User-Agent.

        :param framework: Версия фреймворка.
        :param cms: Версия CMS.
        :param module: Версия модуля.
        """
        if isinstance(framework, Version):
            Configuration.agent_framework = framework
        if isinstance(cms, Version):
            Configuration.agent_cms = cms
        if isinstance(module, Version):
            Configuration.agent_module = module

    @staticmethod
    async def instantiate() -> "Configuration":
        """
        Получение объекта конфигурации.

        :return: Объект конфигурации
        """
        return Configuration(
            account_id=Configuration.account_id,
            secret_key=Configuration.secret_key,
            timeout=Configuration.timeout,
            max_attempts=Configuration.max_attempts,
            auth_token=Configuration.auth_token,
            agent_framework=Configuration.agent_framework,
            agent_cms=Configuration.agent_cms,
            agent_module=Configuration.agent_module,
            api_url=Configuration.api_url,
            verify=Configuration.verify,
        )

    @staticmethod
    def api_endpoint() -> str:
        """
        Получение объекта конфигурации базового URL для API Кассы.

        :return: Строка с API URL
        """
        return Configuration.api_url

    def has_api_credentials(self) -> bool:
        """
        Установлены ли параметры для базовой авторизации.

        :return: Результат проверки условия
        """
        return self.account_id is not None and self.secret_key is not None

    def assert_has_api_credentials(self) -> None:
        """
        Установлены ли параметры для базовой авторизации или авторизации по OAuth.
        Если параметры не установлены, то будет вызвано исключение ConfigurationError
        """
        if self.auth_token is None and not self.has_api_credentials():
            raise ConfigurationError("account_id and secret_key are required")
        elif self.auth_token and self.has_api_credentials():
            raise ConfigurationError("Could not configure authorization with auth_token and basic auth")

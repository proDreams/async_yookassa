import platform
import sys
from typing import Self

import distro
from pydantic import BaseModel, Field

import async_yookassa
from async_yookassa.models.configuration_submodels.version import Version


class UserAgent(BaseModel):
    """
    Класс для создания заголовка User-Agent в запросах к API
    """

    os: Version = Field(default_factory=lambda: UserAgent.define_os())
    python: Version = Field(default_factory=lambda: UserAgent.define_python())
    sdk: Version = Field(default_factory=lambda: UserAgent.define_sdk())
    framework: Version | None = None
    cms: Version | None = None
    module: Version | None = None

    @staticmethod
    def define_os() -> Version:
        """Определение системы."""
        simple = UserAgent.__define_simple_os()
        if simple.name == "Windows":
            return Version(name=simple.name, version=simple.version)
        elif simple.name == "Linux":
            smart = UserAgent.__define_linux_os()
            return Version(name=smart.name.capitalize(), version=smart.version)
        return Version(name=simple.name, version=simple.version)

    @staticmethod
    def define_python() -> Version:
        """Определение версии Python."""
        info = sys.version_info
        version = f"{info.major}.{info.minor}.{info.micro}"
        return Version(name="Python", version=version)

    @staticmethod
    def define_sdk() -> Version:
        """Определение версии SDK."""
        version = async_yookassa.__version__
        return Version(name="Async YooKassa Python", version=version)

    def set_framework(self, name: str, version: str) -> Self:
        """Устанавливает версию фреймворка."""
        self.framework = Version(name=name, version=version)
        return self

    def set_cms(self, name: str, version: str) -> Self:
        """Устанавливает версию CMS."""
        self.cms = Version(name=name, version=version)
        return self

    def set_module(self, name: str, version: str) -> Self:
        """Устанавливает версию модуля."""
        self.module = Version(name=name, version=version)
        return self

    def get_header_string(self) -> str:
        """Возвращает значения header в виде строки."""
        part_delimiter = " "
        headers = [str(self.os), str(self.python)]
        if self.framework:
            headers.append(str(self.framework))
        if self.cms:
            headers.append(str(self.cms))
        if self.module:
            headers.append(str(self.module))
        headers.append(str(self.sdk))
        return part_delimiter.join(headers)

    @staticmethod
    def __define_simple_os() -> Version:
        """Определение данных системы для Windows."""
        return Version(name=platform.system(), version=platform.release())

    @staticmethod
    def __define_linux_os() -> Version:
        """Определение данных системы для Linux."""
        return Version(name=distro.name(), version=distro.version())

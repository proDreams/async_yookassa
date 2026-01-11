"""UserAgent dataclass for building User-Agent headers."""

from __future__ import annotations

import platform
import sys
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

import distro

from async_yookassa.models.configuration_submodels.version import Version

if TYPE_CHECKING:
    pass


@dataclass
class UserAgent:
    """
    Класс для создания заголовка User-Agent в запросах к API.
    """

    os: Version = field(default_factory=lambda: UserAgent._define_os())
    python: Version = field(default_factory=lambda: UserAgent._define_python())
    sdk: Version = field(default_factory=lambda: UserAgent._define_sdk())
    framework: Version | None = None
    cms: Version | None = None
    module: Version | None = None

    @staticmethod
    def _define_os() -> Version:
        """Определение системы."""
        system = platform.system()
        if system == "Linux":
            return Version(name=distro.name().capitalize(), version=distro.version())
        return Version(name=system, version=platform.release())

    @staticmethod
    def _define_python() -> Version:
        """Определение версии Python."""
        info = sys.version_info
        return Version(name="Python", version=f"{info.major}.{info.minor}.{info.micro}")

    @staticmethod
    def _define_sdk() -> Version:
        """Определение версии SDK."""
        import async_yookassa

        return Version(name="Async YooKassa Python", version=async_yookassa.__version__)

    def set_framework(self, name: str, version: str) -> UserAgent:
        """Устанавливает версию фреймворка."""
        self.framework = Version(name=name, version=version)
        return self

    def set_cms(self, name: str, version: str) -> UserAgent:
        """Устанавливает версию CMS."""
        self.cms = Version(name=name, version=version)
        return self

    def set_module(self, name: str, version: str) -> UserAgent:
        """Устанавливает версию модуля."""
        self.module = Version(name=name, version=version)
        return self

    def get_header_string(self) -> str:
        """Возвращает значения header в виде строки."""
        parts = [str(self.os), str(self.python)]
        if self.framework:
            parts.append(str(self.framework))
        if self.cms:
            parts.append(str(self.cms))
        if self.module:
            parts.append(str(self.module))
        parts.append(str(self.sdk))
        return " ".join(parts)

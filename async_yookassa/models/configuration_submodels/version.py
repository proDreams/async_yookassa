"""Version dataclass for User-Agent headers."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Version:
    """
    Версия компонента для User-Agent.

    Используется для указания версий SDK, фреймворка, CMS и модуля.
    """

    name: str
    version: str

    def __str__(self) -> str:
        return f"{self.name}/{self.version}"

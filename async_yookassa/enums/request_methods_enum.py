from enum import Enum


class HTTPMethodEnum(str, Enum):
    GET = "GET"
    POST = "POST"

    def __str__(self) -> str:
        return self.value

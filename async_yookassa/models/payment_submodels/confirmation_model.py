from enum import Enum

from pydantic import BaseModel


class TypeEnum(str, Enum):
    embedded = "embedded"
    external = "external"
    mobile_application = "mobile_application"
    qr = "qr"
    redirect = "redirect"


class Confirmation(BaseModel):
    type: TypeEnum
    locale: str | None = None
    return_url: str | None = None
    enforce: bool | None = None

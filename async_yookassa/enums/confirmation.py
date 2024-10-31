from enum import Enum


class ConfirmationTypeBase(str, Enum):
    redirect = "redirect"


class ConfirmationTypeEnum(ConfirmationTypeBase):
    embedded = "embedded"
    external = "external"
    mobile_application = "mobile_application"
    qr = "qr"

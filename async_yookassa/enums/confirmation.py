from enum import Enum


class ConfirmationTypeEnum(str, Enum):
    embedded = "embedded"
    external = "external"
    mobile_application = "mobile_application"
    qr = "qr"
    redirect = "redirect"

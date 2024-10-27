from enum import Enum

from pydantic import BaseModel

from async_yookassa.models.payment_submodels.payment_method_submodels.card_product_model import (
    CardProduct,
)


class CardRequest(BaseModel):
    number: str
    expiry_year: str
    expiry_month: str
    cardholder: str | None = None
    csc: str | None = None


class CardTypeEnum(str, Enum):
    MasterCard = "MasterCard"
    Visa = "Visa"
    Mir = "Mir"
    UnionPay = "UnionPay"
    JCB = "JCB"
    AmericanExpress = "AmericanExpress"
    DinersClub = "DinersClub"
    DiscoverCard = "DiscoverCard"
    InstaPayment = "InstaPayment"
    InstaPaymentTM = "InstaPaymentTM"
    Laser = "Laser"
    Dankort = "Dankort"
    Solo = "Solo"
    Switch = "Switch"
    Unknown = "Unknown"


class CardResponse(BaseModel):
    first6: str | None = None
    last4: str
    expiry_year: str
    expiry_month: str
    card_type: CardTypeEnum
    card_product: CardProduct | None = None
    issuer_country: str | None = None
    issuer_name: str | None = None
    source: str | None = None

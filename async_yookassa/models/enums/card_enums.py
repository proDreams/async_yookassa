from enum import Enum


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


class SourceEnum(str, Enum):
    mir_pay = "mir_pay"
    apple_pay = "apple_pay"
    google_pay = "google_pay"

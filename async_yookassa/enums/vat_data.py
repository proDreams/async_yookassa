from enum import Enum


class VatDataTypeEnum(str, Enum):
    untaxed = "untaxed"
    calculated = "calculated"
    mixed = "mixed"


class RateEnum(str, Enum):
    five = "5"
    seven = "7"
    ten = "10"
    twenty = "20"
    twenty_two = "22"

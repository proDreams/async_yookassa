from enum import Enum


class VatDataTypeEnum(str, Enum):
    untaxed = "untaxed"
    calculated = "calculated"
    mixed = "mixed"


class RateEnum(str, Enum):
    seven = "7"
    ten = "10"
    eighteen = "18"
    twenty = "20"

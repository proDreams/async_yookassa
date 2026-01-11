from enum import StrEnum


class ItemMeasureEnum(StrEnum):
    """
    Мера количества предмета расчета (Тег в 54 ФЗ — 2108).
    Используется в параметре measure массива items.
    """

    PIECE = "piece"
    GRAM = "gram"
    KILOGRAM = "kilogram"
    TON = "ton"
    CENTIMETER = "centimeter"
    DECIMETER = "decimeter"
    METER = "meter"
    SQUARE_CENTIMETER = "square_centimeter"
    SQUARE_DECIMETER = "square_decimeter"
    SQUARE_METER = "square_meter"
    MILLILITER = "milliliter"
    LITER = "liter"
    CUBIC_METER = "cubic_meter"
    KILOWATT_HOUR = "kilowatt_hour"
    GIGACALORIE = "gigacalorie"
    DAY = "day"
    HOUR = "hour"
    MINUTE = "minute"
    SECOND = "second"
    KILOBYTE = "kilobyte"
    MEGABYTE = "megabyte"
    GIGABYTE = "gigabyte"
    TERABYTE = "terabyte"
    ANOTHER = "another"

from enum import Enum


class FiscalizationProviderEnum(str, Enum):
    avanpost = "avanpost"
    a_qsi = "a_qsi"
    atol = "atol"
    business_ru = "business_ru"
    digital_kassa = "digital_kassa"
    evotor = "evotor"
    first_ofd = "first_ofd"
    kit_invest = "kit_invest"
    komtet = "komtet"
    life_pay = "life_pay"
    mertrade = "mertrade"
    modul_kassa = "modul_kassa"
    rocket = "rocket"
    shtrih_m = "shtrih_m"

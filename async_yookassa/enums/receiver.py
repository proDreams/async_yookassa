from enum import Enum


class ReceiverTypeEnum(str, Enum):
    bank_account = "bank_account"
    mobile_balance = "mobile_balance"
    digital_wallet = "digital_wallet"

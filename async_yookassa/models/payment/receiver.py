from typing import Annotated, Literal, Union

from pydantic import Field

from async_yookassa.enums.receiver import ReceiverTypeEnum
from async_yookassa.models.base import ModelConfigBase


class MobileBalanceReceiver(ModelConfigBase):
    type: Literal[ReceiverTypeEnum.mobile_balance]
    phone: str = Field(min_length=11, max_length=15)


class DigitalWalletReceiver(ModelConfigBase):
    type: Literal[ReceiverTypeEnum.digital_wallet]
    account_number: str = Field(min_length=20, max_length=20)


class BankAccountReceiver(DigitalWalletReceiver):
    type: Literal[ReceiverTypeEnum.bank_account]
    bic: str = Field(min_length=9, max_length=9)


ReceiverUnion = Annotated[
    Union[MobileBalanceReceiver, DigitalWalletReceiver, BankAccountReceiver],
    Field(discriminator="type"),
]

from typing import Annotated, Literal, Union

from pydantic import Field

from async_yookassa.enums.payout import PayoutTypeEnum
from async_yookassa.models.base import ModelConfigBase
from async_yookassa.models.payment.methods.card import (
    CardResponseBase,
)


class CardPayoutDestination(ModelConfigBase):
    type: Literal[PayoutTypeEnum.bank_card]
    card: CardResponseBase | None = None


class CardPayoutDestinationRequest(CardPayoutDestination):
    card: CardResponseBase


class SBPPayoutDestinationRequest(ModelConfigBase):
    type: Literal[PayoutTypeEnum.sbp]
    bank_id: str
    phone: str


class SBPPayoutDestination(SBPPayoutDestinationRequest):
    recipient_checked: bool


class YooMoneyPayoutDestination(ModelConfigBase):
    type: Literal[PayoutTypeEnum.yoo_money]
    account_number: str = Field(min_length=11, max_length=33)


PayoutDestinationUnion = Annotated[
    Union[CardPayoutDestination, SBPPayoutDestination, YooMoneyPayoutDestination],
    Field(discriminator="type"),
]
PayoutDestinationRequestUnion = Annotated[
    Union[CardPayoutDestinationRequest, SBPPayoutDestinationRequest, YooMoneyPayoutDestination],
    Field(discriminator="type"),
]

from pydantic import Field

from async_yookassa.enums.me import MeStatusEnum, PayoutMethodsEnum
from async_yookassa.enums.payment import PaymentMethodType
from async_yookassa.models.base import ModelConfigBase
from async_yookassa.models.me.fiscalization import Fiscalization
from async_yookassa.models.payment.amount import Amount


class MeResponse(ModelConfigBase):
    account_id: str
    status: MeStatusEnum
    test: bool
    fiscalization: Fiscalization | None = None
    fiscalization_enabled: bool | None = None
    payment_methods: list[PaymentMethodType] | None = None
    itn: str | None = Field(min_length=1, max_length=20, default=None)
    payout_methods: list[PayoutMethodsEnum]
    name: str | None = None
    payout_balance: Amount | None = None

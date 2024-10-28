from pydantic import BaseModel, Field

from async_yookassa.enums.me_enums import MeStatusEnum, PayoutMethodsEnum
from async_yookassa.enums.payment_method_enums import PaymentMethodTypeEnum
from async_yookassa.models.me_submodels.fiscalization_model import Fiscalization
from async_yookassa.models.payment_submodels.amount_model import Amount


class Me(BaseModel):
    account_id: str
    status: MeStatusEnum
    test: bool
    fiscalization: Fiscalization | None = None
    fiscalization_enabled: bool | None = None
    payment_methods: list[PaymentMethodTypeEnum] | None = None
    itn: str | None = Field(min_length=1, max_length=20, default=None)
    payout_methods: list[PayoutMethodsEnum]
    name: str | None = None
    payout_balance: Amount | None = None

from pydantic import BaseModel, ConfigDict

from async_yookassa.enums.settlement import SettlementReceiptEnum, SettlementTypeEnum
from async_yookassa.models.payment_submodels.amount import Amount


class Settlement(BaseModel):
    type: str = SettlementTypeEnum.payout
    amount: Amount

    model_config = ConfigDict(use_enum_values=True)


class SettlementReceipt(Settlement):
    type: SettlementReceiptEnum

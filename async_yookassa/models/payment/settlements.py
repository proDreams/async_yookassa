from async_yookassa.enums.settlement import SettlementReceiptEnum, SettlementTypeEnum
from async_yookassa.models.base import ModelConfigBase
from async_yookassa.models.payment.amount import Amount


class Settlement(ModelConfigBase):
    type: str = SettlementTypeEnum.payout
    amount: Amount


class SettlementReceipt(Settlement):
    type: SettlementReceiptEnum

from typing import Annotated, Literal, Union

from pydantic import Field

from async_yookassa.enums.vat_data import RateEnum, VatDataTypeEnum
from async_yookassa.models.base import ModelConfigBase
from async_yookassa.models.payment.amount import Amount


class UntaxedVatData(ModelConfigBase):
    type: Literal[VatDataTypeEnum.untaxed]


class MixedVatData(ModelConfigBase):
    type: Literal[VatDataTypeEnum.mixed]
    amount: Amount


class CalculatedVatData(MixedVatData):
    type: Literal[VatDataTypeEnum.calculated]
    rate: RateEnum


VatDataUnion = Annotated[
    Union[UntaxedVatData, MixedVatData, CalculatedVatData],
    Field(discriminator="type"),
]

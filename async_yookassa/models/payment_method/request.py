from async_yookassa.enums.payment_methods import PaymentMethodType
from async_yookassa.models.base import ModelConfigBase
from async_yookassa.models.payment.methods.card import CardRequest
from async_yookassa.models.payment_method.confirmation import RedirectConfirmationRequest
from async_yookassa.models.payment_method.holder import HolderRequest


class PaymentMethodRequest(ModelConfigBase):
    type: PaymentMethodType
    card: CardRequest
    holder: HolderRequest
    client_ip: str | None = None
    confirmation: RedirectConfirmationRequest

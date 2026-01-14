from async_yookassa.enums.payment import PaymentMethodStatus
from async_yookassa.enums.payment_methods import PaymentMethodType
from async_yookassa.models.base import ModelConfigBase
from async_yookassa.models.payment.methods.card import CardResponse
from async_yookassa.models.payment_method.confirmation import RedirectConfirmationResponse
from async_yookassa.models.payment_method.holder import HolderResponse


class PaymentMethodResponse(ModelConfigBase):
    type: PaymentMethodType
    card: CardResponse | None = None
    id: str
    saved: bool
    status: PaymentMethodStatus
    holder: HolderResponse
    title: str | None = None
    confirmation: RedirectConfirmationResponse

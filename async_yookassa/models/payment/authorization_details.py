from pydantic import BaseModel

from async_yookassa.models.payment.three_d_secure import (
    ThreeDSecure,
)


class AuthorizationDetails(BaseModel):
    rrn: str | None = None
    auth_code: str | None = None
    three_d_secure: ThreeDSecure

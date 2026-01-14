from pydantic import BaseModel

from async_yookassa.enums.webhook_event import WebhookEvent


class WebhookRequest(BaseModel):
    event: WebhookEvent
    url: str

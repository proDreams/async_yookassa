from pydantic import BaseModel

from async_yookassa.enums.webhook_event import WebhookEvent


class WebhookResponse(BaseModel):
    id: str
    event: WebhookEvent
    url: str


class WebhookListResponse(BaseModel):
    type: str
    items: list[WebhookResponse]

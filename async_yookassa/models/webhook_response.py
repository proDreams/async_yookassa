from pydantic import BaseModel

from async_yookassa.models.webhook_request import WebhookRequest


class WebhookResponse(WebhookRequest):
    id: str


class WebhookListResponse(BaseModel):
    type: str
    items: list[WebhookResponse]
    next_cursor: str | None = None

from pydantic import BaseModel


class WebhookRequest(BaseModel):
    event: str
    url: str

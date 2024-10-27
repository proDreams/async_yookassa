from pydantic import BaseModel


class Recipient(BaseModel):
    gateway_id: str

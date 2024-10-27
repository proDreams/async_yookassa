from pydantic import BaseModel


class Recipient(BaseModel):
    gateway_id: str


class RecipientResponse(Recipient):
    account_id: str

from pydantic import BaseModel


class HolderResponse(BaseModel):
    account_id: str
    gateway_id: str | None = None


class HolderRequest(BaseModel):
    gateway_id: str

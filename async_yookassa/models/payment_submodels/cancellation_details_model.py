from pydantic import BaseModel


class CancellationDetails(BaseModel):
    party: str
    reason: str

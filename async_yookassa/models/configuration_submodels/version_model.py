from pydantic import BaseModel


class Version(BaseModel):
    name: str
    version: str

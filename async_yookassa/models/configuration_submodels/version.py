from pydantic import BaseModel


class Version(BaseModel):
    name: str
    version: str

    def __str__(self):
        return f"{self.name}/{self.version}"

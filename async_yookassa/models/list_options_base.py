from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class ListOptionsBase(BaseModel):
    created_at_gte: datetime | None = Field(default=None, serialization_alias="created_at.gte")
    created_at_gt: datetime | None = Field(default=None, serialization_alias="created_at.gt")
    created_at_lte: datetime | None = Field(default=None, serialization_alias="created_at.lte")
    created_at_lt: datetime | None = Field(default=None, serialization_alias="created_at.lt")
    limit: int | None = Field(default=10, ge=1, le=100)
    cursor: str | None = None

    model_config = ConfigDict(populate_by_name=True)

from pydantic import BaseModel, ConfigDict


class ModelConfigBase(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

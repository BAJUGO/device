from pydantic import BaseModel, Field, ConfigDict

class BaseReturn(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int


class CharacterMetaPatchSchema(BaseModel):
    name: str | None = Field(None, max_length=40)
    last_name: str | None = Field(None, max_length=40)
    description: str | None = Field(None, max_length=1000)


class CharacterMetaCreateSchema(BaseModel):
    name: str = Field(max_length=30)
    last_name: str | None = Field(None, max_length=30)
    description: str | None = Field(None, max_length=1000)


class CharacterMetaSchema(BaseReturn, CharacterMetaCreateSchema):
    pass


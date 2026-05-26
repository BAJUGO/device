from sqlalchemy.orm import  Mapped, mapped_column, relationship
from sqlalchemy import String,Text


from core import Base


class CharacterMeta(Base):
    __tablename__ = "characters_meta"

    name: Mapped[str] = mapped_column(String(40))
    last_name: Mapped[str] = mapped_column(String(40), nullable=True)

    description: Mapped[str] = mapped_column(String(1000), nullable=True)

    blob_key: Mapped[str] = mapped_column(String(255), nullable=False, unique=True, index=True)




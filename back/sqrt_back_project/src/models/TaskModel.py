from typing import Optional
from sqlalchemy import ForeignKey


from sqlalchemy.orm import Mapped, mapped_column
from enum import Enum


from configs.db import Base


class Quadro(Enum):
    pass


class Role(Base):
    __tablename__ = 'role'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]


class Task(Base):
    __tablename__ = 'task'

    id: Mapped[int] = mapped_column(primary_key=True)
    title:Mapped[str]



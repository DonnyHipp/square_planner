from typing import Optional

from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from src.configs.db import Base


class Act(Base):
    title: Mapped[Optional[str]]
    kpi: Mapped[Optional[int]]

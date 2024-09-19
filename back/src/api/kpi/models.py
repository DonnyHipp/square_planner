import uuid
from typing import Optional

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from src.configs.db import Base


class KPI(Base):
    __tablename__ = "kpi"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    title: Mapped[str] = mapped_column(String, nullable=False)
    target_value: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    goal_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("goals.id")
    )

    goal = relationship("Goal", back_populates="kpi")
    tasks = relationship("Task", back_populates="kpi")

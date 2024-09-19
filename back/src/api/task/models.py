import uuid
from typing import Optional

from sqlalchemy import String, ForeignKey, UUID, Text
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column, relationship

from src.configs.db import Base


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    kpi_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("kpis.id")
    )

    kpi = relationship("KPI", back_populates="tasks")

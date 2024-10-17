import uuid
from typing import Optional, List

from sqlalchemy import String, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, Mapped, mapped_column

from src.configs.db import BaseDB


class SphereOfLife(BaseDB):
    __tablename__ = "sphere"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    title: Mapped[str] = mapped_column(String, nullable=False)
    goals: Mapped[List["Goal"]] = relationship("Goal", back_populates="sphere")


class Goal(BaseDB):
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(
        Text, nullable=True, max_length=200
    )
    sphere_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("spheres.id")
    )

    sphere = relationship("Sphere", back_populates="goals")
    kpis = relationship("KPI", back_populates="goal")

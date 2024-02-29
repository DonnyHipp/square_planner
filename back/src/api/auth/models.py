from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from configs.db import TimestampUUIDMixin, Base

# from src.configs.db import Base, TimestampUUIDMixin


class User(TimestampUUIDMixin, Base):
    email: Mapped[str] = mapped_column(unique=True)
    first_name: Mapped[str | None]
    last_name: Mapped[str | None]
    hashed_password: Mapped[str] = mapped_column(String(1024), nullable=False)
    is_activated: Mapped[bool] = mapped_column(default=True)
    is_superuser: Mapped[bool] = mapped_column(default=True)

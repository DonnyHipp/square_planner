import uuid
from enum import Enum
from typing import Optional

from src.api.subscription.constants import SubscriptionsChoices
from src.configs.db import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey


class Subscription(Base):
    __tablename__ = "subscription"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    subscription: Mapped[int] = mapped_column(Enum(SubscriptionsChoices))
    title: Mapped[Optional[str]] = None
    advantages: Mapped[Optional[int]] = mapped_column(
        ForeignKey("subscription.id")
    )


class SubscriptionAdvantage(Base):
    __tablename__ = "subscription"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    title: Mapped[str]

from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from enum import Enum as SQLAlchemyEnum

Base = declarative_base()

class Importance(str, SQLAlchemyEnum):
    URGENT_IMPORTANT = "urgent_important"
    URGENT_NOT_IMPORTANT = "urgent_not_important"
    NOT_URGENT_IMPORTANT = "not_urgent_important"
    NOT_URGENT_NOT_IMPORTANT = "not_urgent_not_important"

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    creation_date = Column(DateTime, default=datetime.utcnow)
    update_date = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    deadline = Column(DateTime)
    quadrant = Column(Enum(Importance), nullable=False)
    role_id = Column(Integer, ForeignKey('roles.id'))
    metric_id = Column(Integer, ForeignKey('metrics.id'))

    role_name = Column(String)  # Добавляем mapped column для связи с ролью (без relationship)
    metric_name = Column(String)  # Добавляем mapped column для связи с метрикой (без relationship)

# Добавляем таблицы для ролей и метрик
class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)

class Metric(Base):
    __tablename__ = 'metrics'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
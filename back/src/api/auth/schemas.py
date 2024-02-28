from typing import Optional
from pydantic import BaseModel, EmailStr, UUID4
import uuid


class BaseUser(BaseModel):
    id: UUID4
    email: EmailStr
    first_name: str
    last_name: str
    is_active: bool = True
    is_superuser: bool = False

    class Config:
        orm_mode = True


class BaseUserCreate(BaseModel):
    email: EmailStr
    password: str
    first_name: Optional[str]
    last_name: Optional[str]
    is_activated: Optional[bool] = True
    is_superuser: Optional[bool] = False


class BaseUserUpdate(BaseModel):
    password: Optional[str] = None
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = None
    is_superuser: Optional[bool] = None
    is_verified: Optional[bool] = None

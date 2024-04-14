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


class LoginUser(BaseModel):
    email: EmailStr
    password: str


class UserInDB(BaseUser):
    hashed_password: str


class BaseUserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = None
    is_superuser: Optional[bool] = None
    is_verified: Optional[bool] = None


class BaseUserCreate:
    pass

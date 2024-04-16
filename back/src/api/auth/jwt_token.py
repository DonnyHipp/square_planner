from datetime import datetime, timezone, timedelta

from jose import jwt
from pydantic import BaseModel

from src.api.auth.password import password_manager
from src.configs.settings import settings

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


def get_password_hash(password):
    return password_manager.hash(password)


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
    return encoded_jwt


def create_token(user_name: str):
    access_token_expires = timedelta(minutes=settings.JWT_ACCESS_LIFETIME)
    access_token = create_access_token(
        data={"sub": user_name}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")

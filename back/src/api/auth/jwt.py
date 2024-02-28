from datetime import datetime, timedelta

import jwt

from src.configs.settings import settings

__all__ = ["create_token", "decode_token"]


def create_access_token(*, data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM
    )
    return encoded_jwt


def create_refresh_token(email):
    expires = timedelta(minutes=settings.JWT_EXPIRE)
    return create_access_token(data={"sub": email}, expires_delta=expires)


def create_token(email):
    access_token_expires = timedelta(minutes=settings.JWT_EXPIRE)
    access_token = create_access_token(
        data={"sub": email}, expires_delta=access_token_expires
    )
    return access_token


def decode_token(token):
    return jwt.decode(
        token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM]
    )

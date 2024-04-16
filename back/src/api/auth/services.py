import uuid
from typing import Protocol

from jose import jwt, JWTError
from fastapi import HTTPException

from src.api.auth import models, repository, schemas
from src.api.auth.exceptions import credentials_exception
from src.configs.settings import settings


class UserServiceProtocol(Protocol):

    async def registry_user(self):
        raise NotImplementedError

    async def login_user(self, user):
        raise NotImplementedError

    async def update_user(self):
        raise NotImplementedError

    async def change_superuser_rule(self):
        raise NotImplementedError


class UserService(UserServiceProtocol):

    def __init__(self, repository: repository.UserAbstractRepository) -> None:
        self.repository = repository

    async def registry_user(self, user: schemas.UserCreate) -> models.User:
        return await self.repository.create_user(user)

    async def login_user(self, password: str, email: str | None = None):
        user = await self.repository.get_user(email=email)
        if not user:
            raise HTTPException(status_code=400, detail="Incorrect email")
        verify = await self.repository.verify_user_password(user, password)
        if not verify:
            raise HTTPException(status_code=400, detail="Incorrect password")
        return user

    async def get_user_from_jwt(self, token: str):
        try:
            payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
            username: str = payload.get("sub")
            if username is None:
                raise credentials_exception
        except JWTError:
            raise credentials_exception
        user = await self.repository.get_user(email=username)
        if user is None:
            raise credentials_exception
        return user

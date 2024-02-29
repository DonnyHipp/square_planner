import uuid
from typing import Protocol

from api.auth import models, repository, schemas
from fastapi import HTTPException


class UserServiceProtocol(Protocol):

    async def registry_user(self):
        raise NotImplementedError

    async def login_user(self):
        raise NotImplementedError

    async def update_user(self):
        raise NotImplementedError

    async def change_superuser_rule(self):
        raise NotImplementedError


class UserService(UserServiceProtocol):

    def __init__(self, repository: repository.UserAbstractRepository) -> None:
        self.repository = repository

    async def registry_user(self, user: schemas.BaseUserCreate) -> models.User:
        return await self.repository.create_user(user)

    async def login_user(self, password: str, email: str | None = None):
        user = await self.repository.get_user(email=email)
        if not user:
            raise HTTPException(status_code=400, detail="Incorrect email")
        verify = await self.repository.verify_user_password(user, password)
        if not verify:
            raise HTTPException(status_code=400, detail="Incorrect password")
        return user

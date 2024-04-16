import uuid
from abc import ABC
from typing import Protocol

from src.api.auth import exceptions, models, schemas
from src.api.auth.password import password_manager
from sqlalchemy import select

from src.configs.db import async_session_maker


class UserAbstractRepository(ABC):

    async def get_user(self):
        raise NotImplementedError

    async def create_user(self):
        raise NotImplementedError

    async def verify_user_password(self):
        raise NotImplementedError

    async def verify_user_password(self):
        raise NotImplementedError


class UserRepository(UserAbstractRepository):

    async def get_user(
        self,
        user_id: uuid.UUID | None = None,
        email: str | None = None,
    ) -> models.User | None:
        filters = []
        if user_id:
            filters.append(models.User.id == user_id)
        if email:
            filters.append(models.User.email == email)

        stmt = select(models.User).where(*filters)

        async with async_session_maker() as session:
            result = await session.execute(stmt)
            user = result.unique().scalar_one_or_none()
        return user

    async def create_user(self, user: schemas.UserCreate) -> models.User:

        if await self.get_user(email=user.email):
            raise exceptions.UserAlreadyExists()

        password_hash = password_manager.hash(user.password)

        user = models.User(
            email=user.email,
            hashed_password=password_hash,
        )

        async with async_session_maker() as session:
            session.add(user)
            await session.commit()
        return user

    async def verify_user_password(self, user: models.User, password: str) -> bool:
        user = await self.get_user(email=user.email)
        return password_manager.verify(password, user.hashed_password)



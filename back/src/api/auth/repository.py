import uuid
from typing import Protocol

from src.api.auth import exceptions, models, schemas
from src.api.auth.password import password_manager
from sqlalchemy import select

from src.configs.db import async_session_maker


class UserAbstractRepository(Protocol):

    async def get_user(self):
        raise NotImplementedError

    async def create_user(self):
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

    async def create_user(self, user: schemas.BaseUserCreate) -> models.User:

        if await self.get_user(email=user.email):
            raise exceptions.UserAlreadyExists()

        if password_manager.string_security_check:
            password_hash = password_manager.hash(user.password)
        else:
            raise exceptions.WeekPassword

        user = models.User(
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name,
            hashed_password=password_hash,
        )

        async with async_session_maker() as session:
            session.add(user)
            await session.commit()
        return user



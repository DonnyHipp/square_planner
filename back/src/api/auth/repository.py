import uuid
from sqlalchemy import select
from api.auth import models
from src.configs.db import async_session_maker
from api.auth.password import password_hasher


class UserRepository:
    def __init__(self, session: async_session_maker):
        self._session = session

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
        result = await self.session.execute(stmt)
        user = result.unique().scalar_one_or_none()

        return user

    async def create_user(
        self,
        email: str,
        password: str,
        first_name: str | None = None,
        last_name: str | None = None,
    ) -> models.User:
        password_hash = password_hasher(password)
        user = models.User(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password_hash,
        )
        with async_session_maker as session:
            await session.add(user)

        return user

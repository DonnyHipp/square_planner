import uuid

from fastapi_users import FastAPIUsers

from .backend import auth_backend
from .manager import get_user_manager
from ...configs.db import User


fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)

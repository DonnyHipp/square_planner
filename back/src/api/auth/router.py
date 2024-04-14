from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

from src.api.auth import handlers

router = APIRouter(prefix="/user", tags=["Auth"])


router.add_api_route(methods=["POST"], path="/register", endpoint=handlers.register)
router.add_api_route(methods=["GET"], path="/read_user", endpoint=handlers.read_user)
router.add_api_route(methods=["POST"], path="/token", endpoint=handlers.login_for_access_token)

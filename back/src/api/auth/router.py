from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

from api.auth import handlers

router = APIRouter(prefix="/user")


# router.add_api_route(path="/{user_id}", methods=["GET"], endpoint=handlers.get_user)
# router.add_api_route(path="/{user_id}", methods=["POST"], endpoint=handlers.update_user
# router.add_api_route(methods=["GET"], path="/check", endpoint=handlers.check_token)
router.add_api_route(methods=["POST"], path="/token", endpoint=handlers.login)
router.add_api_route(methods=["POST"], path="/register", endpoint=handlers.register)
# router.add_api_route(methods=["GET"], path="/logout", endpoint=handlers.logout)

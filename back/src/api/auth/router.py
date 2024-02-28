from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

router = APIRouter(prefix="/user")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# router.add_api_route(path="/{user_id}", methods=["GET"], endpoint=handlers.check_user)
# router.add_api_route(path="/{user_id}", methods=["GET"], endpoint=handlers.get_user)
# router.add_api_route(path="/{user_id}", methods=["POST"], endpoint=handlers.update_user
# router.add_api_route(methods=["GET"], path="/check", endpoint=handlers.check_token)
# router.add_api_route(methods=["DELETE"], path="/logout", endpoint=handlers.logout)

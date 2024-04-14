from http import HTTPStatus
from typing import Annotated

from fastapi import status, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from src.api.auth import schemas, exceptions, dependencies
from src.api.auth.jwt_token import Token, create_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def register(user: schemas.LoginUser):
    try:
        user = await dependencies.user_service.registry_user(user)
        return schemas.LoginUser(user)
    except exceptions.UserAlreadyExists:
        return HTTPException(
            status_code=404, detail="User with this email already exists"
        )


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    try:
        user = dependencies.user_service.get_user_from_jwt(token)
    except Exception:
        raise exceptions.credentials_exception
    return user


async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    user = dependencies.login(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return create_token(user.email)


async def read_user(
    current_user: Annotated[schemas.BaseUser, Depends(get_current_user)],
):
    return current_user


def logout():
    pass

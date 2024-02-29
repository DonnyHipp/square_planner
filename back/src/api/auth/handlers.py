from http import HTTPStatus

from fastapi import Response
from fastapi.exceptions import HTTPException

from api.auth import schemas, exceptions, dependencies


async def register(user: schemas.BaseUserCreate):
    try:
        user = await dependencies.user_service.registry_user(user)
        return user
    except exceptions.UserAlreadyExists:
        return HTTPException(
            status_code=404, detail="User with this email already exists"
        )


async def login(response: Response, user: schemas.LoginUser):

    active_user = await dependencies.user_service.login_user(
        user.password,
        user.email,
    )
    if not active_user:
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED,
            detail="Неверные имя пользователя или пароль",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token, refresh_token = dependencies.set_tokens({"sub": user.email}, response)
    return {"access_token": access_token, "token_type": "bearer"}


def logout():
    pass

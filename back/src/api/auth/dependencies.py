from http import HTTPStatus

from fastapi import HTTPException

from src.api.auth import services, repository, schemas


user_repository = repository.UserRepository()
user_service = services.UserService(user_repository)


async def login(user: schemas.LoginUser):

    active_user = await user_service.login_user(
        user.password,
        user.email,
    )
    if not active_user:
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED,
            detail="Неверные имя пользователя или пароль",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user



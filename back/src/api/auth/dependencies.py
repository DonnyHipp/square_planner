from fastapi import Cookie, Depends, HTTPException
from fastapi.security import APIKeyCookie, OAuth2PasswordBearer

from api.auth import services, repository, jwt_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

user_repository = repository.UserRepository()
user_service = services.UserService(user_repository)
jwt_tool = jwt_token.JWT()


def get_tokens_from_coockie(tokens: Cookie()):
    print(tokens)
    return


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt_tool.decode_jwt(token)
        email = payload.get("sub")
        if email is None:
            raise credentials_exception
        user = user_repository.get_user(email=email)
        if user is None:
            raise credentials_exception
    except Exception:
        raise credentials_exception
    return user


def set_tokens(data: str, response):
    access_token, refresh_token = jwt_tool.generate_two_tokens(data)
    response.set_cookie(key="access_token", value=access_token, httponly=True)
    response.set_cookie(key="refresh_token", value=refresh_token, httponly=True)
    return access_token, refresh_token

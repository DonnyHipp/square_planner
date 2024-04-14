from fastapi import HTTPException
from fastapi import status

class WeekPassword(Exception):
    pass


class UserAlreadyExists(Exception):
    pass


credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)

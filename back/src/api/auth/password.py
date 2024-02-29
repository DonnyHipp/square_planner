from typing import Protocol, Tuple

from passlib import pwd
from passlib.context import CryptContext


class PasswordProtocol(Protocol):
    def verify_and_update(
        self, plain_password: str, hashed_password: str
    ) -> Tuple[bool, str]:
        raise NotImplementedError

    def hash(self, password: str) -> str:
        raise NotImplementedError

    def generate(self) -> str:
        raise NotImplementedError


class PasswordManager(PasswordProtocol):
    def __init__(self) -> None:
        self.context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def verify_and_update(
        self, plain_password: str, hashed_password: str
    ) -> Tuple[bool, str]:
        return self.context.verify_and_update(plain_password, hashed_password)

    def string_security_check(self, password):
        True

    def hash(self, password: str) -> str:
        return self.context.hash(password)

    def generate(self) -> str:
        return pwd.genword(length=12)


password_manager = PasswordManager()

from typing import Any, Dict, List, Optional

from datetime import datetime, timedelta

import jwt

from configs.settings import settings

print(settings.JWT_REFRESH_LIFETIME)


class JWT:

    lifetime_access: str = settings.JWT_REFRESH_LIFETIME
    lifetime_access: str = settings.JWT_ACCESS_LIFETIME
    secret: str = settings.JWT_SECRET_KEY
    algorithm: str = settings.JWT_ALGORITHM

    def encode_jwt(
        self, data: dict, lifetime_minutes: Optional[int] = None, token_type: str = None
    ) -> str:
        payload = {"data": data}
        if lifetime_minutes:
            expire = datetime.utcnow() + timedelta(minutes=lifetime_minutes)
            payload["exp"] = expire
        if token_type:
            payload["type"] = token_type
        else:
            payload["type"] = "access"

        return jwt.encode(payload, self.secret, algorithm=self.algorithm)

    def decode_jwt(
        self,
        encoded_jwt: str,
    ) -> Dict[str, Any]:
        return jwt.decode(
            encoded_jwt,
            self.secret,
            algorithms=self.algorithm,
        )

    def generate_two_tokens(
        self,
        data: dict,
    ) -> str:

        return (
            self.encode_jwt(token_type="access", data=data),
            self.encode_jwt(token_type="refresh", data=data),
        )

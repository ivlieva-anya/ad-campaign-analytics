from datetime import datetime, timezone
import bcrypt
from fastapi import Depends
from fastapi.security import APIKeyHeader
from jose import jwt, JWTError


from api_v1.users.managers import user_manager
from api_v1.users.models import AdminUser, RegularUser

SECRET_KEY = "super secret key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 10
REFRESH_TOKEN_EXPIRE_MINUTES = 15


class UserTokenIsNotValid(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.msgfmt = message

class UserService:

    @staticmethod
    def verify_password(plain_password, hashed_password)->bool:
        return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))

    @classmethod
    def authenticate_user(cls,username, password):
        user = user_manager.users.get(username)
        if not user or not cls.verify_password(password, user.password):
            return None
        return user

    @staticmethod
    def create_token(data, expires_delta):
        payload = data.copy()
        expire = datetime.now(timezone.utc) + expires_delta
        payload.update({"exp": expire})
        return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

    @classmethod
    def get_current_user(cls, token:str = Depends(APIKeyHeader(name="Authorization"))):
        username = cls.verify_token(token,"access")
        return user_manager.users.get(username)

    @staticmethod
    def verify_token(token:str, token_type:str):
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        current_token_type: str = payload.get("type")

        if current_token_type != token_type :
            raise UserTokenIsNotValid("Token is not valid")
        return payload.get("sub")

    @staticmethod
    def add(username, email, password, is_admin, permissions):
        if is_admin:
            user = AdminUser(username=username, email=email, password=password)
        else:
            user = RegularUser(username=username, email=email, password=password, permission=permissions)

        user_manager.add_user(user),

    @staticmethod
    def get_all():
        return user_manager.get_all_users()



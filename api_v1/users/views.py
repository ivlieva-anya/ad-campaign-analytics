from datetime import timedelta
from typing import List, Optional

import bcrypt
from fastapi import APIRouter, Depends, HTTPException
from fastapi.params import Query
from jose import JWTError
from starlette import status

from api_v1.users.models import AdminUser, RegularUser, PERMISSIONS
from api_v1.users.services import UserService, REFRESH_TOKEN_EXPIRE_MINUTES, ACCESS_TOKEN_EXPIRE_MINUTES, \
    UserTokenIsNotValid

users_router = APIRouter(prefix="/users", tags=["users"])

@users_router.post("")
def add_user(username:str,
             email:str,
             password:str,
             is_admin:bool,
             permissions: Optional[List[str]]=Query(
                default=None,
                title="Permissions",
                example=PERMISSIONS,
                enum=PERMISSIONS
    )):
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
    UserService.add(username=username, email=email, password=hashed_password, is_admin=is_admin, permissions=permissions)
    return {"username": f"User {username} added successfully"}

@users_router.get("")
def get_all_users():
    return UserService.get_all()

@users_router.get("/login")
def login(username:str,password:str):
    user = UserService.authenticate_user(username, password)
    if not user:
        from fastapi import HTTPException
        raise HTTPException(status_code=401, detail="Incorrect username or password")

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    refresh_token_expires = timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)

    access_token = UserService.create_token(data={"sub": user.username,"type":"access"}, expires_delta=access_token_expires)
    refresh_token = UserService.create_token(data={"sub": user.username, "type":"refresh"}, expires_delta=refresh_token_expires)/
    return {
        "access_token": access_token,
        "refresh_token": refresh_token
    }

@users_router.post("/refresh")
def refresh_access_token(token:str):
    try:
        username = UserService.verify_token(token,"refresh")
    except (UserTokenIsNotValid, JWTError) as err:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(err))

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = UserService.create_token(
        data={"sub": username,"type":"access"},
        expires_delta=access_token_expires
    )
    return {"access_token": access_token}

@users_router.get("/me")
def me(current_user = Depends(UserService.get_current_user)):
    return {"user":current_user.username}

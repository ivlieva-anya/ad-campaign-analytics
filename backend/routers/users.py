from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr

from .. import models, database, auth

user_router = APIRouter(
    prefix="/user",
    tags=["users"]
)

class UserBase(BaseModel):
    email: EmailStr
    username: str

class User(UserBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True

@user_router.get("/profile", response_model=User)
async def get_user_profile(current_user: models.User = Depends(auth.get_current_active_user)):
    return current_user 
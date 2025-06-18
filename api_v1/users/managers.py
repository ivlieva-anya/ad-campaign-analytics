from api_v1.users.models import BaseUser
from fastapi import HTTPException

class UserManager:
    def __init__(self):
        self.users = {
        }

    def add_user(self, user:BaseUser):
        if user.username in self.users:
            raise HTTPException(status_code=400, detail="Username already registered")
        self.users[user.username] = user
        return user


    def get_all_users(self):
        #return list(self.users.values())
        return [user.get_info() for user in self.users.values()]


user_manager = UserManager()
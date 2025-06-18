PERMISSIONS = ["View product", "Update product", "Add product", "Delite product"]

class BaseUser:


    def __init__(self, username, password, email, is_admin:bool, permissions):
        self.username = username
        self.password = password
        self.email = email
        self.is_admin = is_admin
        self.permission = permissions

    def get_info(self):
        return {
            "username" : self.username,
            "email" : self.email,
            "is_admin" : self.is_admin,
            "permission" : self.permission
        }


class AdminUser(BaseUser):
    def __init__(self, username, password, email):
        super().__init__(username, password, email, is_admin=True, permissions=PERMISSIONS)

class RegularUser(BaseUser):
    def __init__(self, username, password, email, permission):
        super().__init__(username, password, email, is_admin=False, permissions=permission)
from .user import User

class Admin(User):
    def __init__(self, userid, email, password, name):
        super().__init__(userid, email, password, name)
        self.role = "Admin"

    def manage_book(self):
        return True
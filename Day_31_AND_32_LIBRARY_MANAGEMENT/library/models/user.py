class User:
    def __init__(self, userid: int, email: str, password: str, name: str):
        self.userid = userid
        self.email = email
        self.password = password
        self.name = name
        self.role = "user"
        self.is_active = True

    def display_details(self):
        return {
            "userid": self.userid,
            "email": self.email,
            "name": self.name,
            "role": self.role,
            "is_active": self.is_active
        }

    def manage_book(self):
        return False

    def login_auth(self, password):
        return self.password == password
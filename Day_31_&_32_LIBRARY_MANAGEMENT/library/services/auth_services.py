from library.models import User, Admin

class AuthServices:
    def __init__(self):
        self.users = {}
        self.current_user = None

    def registerUser(self, name: str, email: str, password: str):
        new_user_id = len(self.users) + 1
        user_obj = User(new_user_id, email, password, name)
        self.users[new_user_id] = user_obj
        return f"User {name} registered successfully. ID: {new_user_id}"

    def registerAdmin(self, name: str, email: str, password: str):
        new_admin_id = len(self.users) + 1
        admin_obj = Admin(new_admin_id, email, password, name)
        self.users[new_admin_id] = admin_obj
        return f"Admin {name} registered successfully. ID: {new_admin_id}"

    def login(self, user_id, password):
        if user_id in self.users:
            user_obj = self.users[user_id]

            if not user_obj.login_auth(password):
                return False, "Incorrect password"

            if not user_obj.is_active:
                return False, "User is inactive"

            self.current_user = user_obj
            return True, "Login successful"

        return False, "User ID not found"

    def logout(self):
        self.current_user = None
        return "Logged out successfully"
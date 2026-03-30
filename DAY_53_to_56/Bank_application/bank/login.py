from database import DatabaseConfig

# login class implementation
class Login:
    def __init__(self, account:int, password:str):
        self.account = account 
        self.password = password

    def login(self):
        try:
            db_config = DatabaseConfig()
            cursor = db_config.cursor()

            # check weather the account is exists or not
            get_password_query ="""SELECT PASSWORD FROM ACCOUNTS
                                    WHERE ACCOUNT = %s;"""
            cursor.execute(get_password_query, (self.account,))
            db_password = cursor.fetchone()
            # check db password and verify
            if db_password and db_password[0] == self.password:
                return True
            else:
                return False

        except Exception as e:
            return f"Somthing Wrong in bank/login.py:{e}"

from database import DatabaseConfig


# create create new account class
class CreateAccount:
    def __init__(self, name, email, password, phone, balance):
        self.name =name
        self.email = email
        self.password = password
        self.phone = phone
        self.balance = balance

    def create_new_account(self):
        try:
            db_config = DatabaseConfig()
            cursor = db_config.cursor()

            # check user already exists or not
            check_user_query = """select * from users where email = %s;"""
            cursor.execute(check_user_query, (self.email,))
            if cursor.fetchone():
                cursor.close()
                db_config.close()
                return "User Email Already exists"
            # add new user data into users table
            add_user_query = """INSERT INTO USERS(USERNAME, EMAIL, PH) VALUES(%s, %s, %s);"""
            cursor.execute(add_user_query, (self.name, self.email, self.phone))
            db_config.commit()

            # get account number
            get_accountNO_query = """select account from users where email = %s;"""
            cursor.execute(get_accountNO_query, (self.email,))
            account_number = cursor.fetchone()[0]
            # add account and password to aaccounts table
            query = "INSERT INTO ACCOUNTS(ACCOUNT, PASSWORD, BALANCE) VALUES(%s, %s, %s);"
            cursor.execute(query, (account_number, self.password, self.balance))

            # add transaction in tranasctions table
            add_transcation_query = """INSERT INTO TRANSACTIONS(ACCOUNT, TRANSACTIONTYPE, AMOUNT)
                                        VALUES(%s, %s, %s);"""
            cursor.execute(add_transcation_query, (account_number, "CREDIT", self.balance))
            db_config.commit()
            cursor.close()
            db_config.close()

            return f"Successfully account created and your account number is {account_number}"
        except Exception as e:
            return f"Something wrong in bank/register.py: {e}"
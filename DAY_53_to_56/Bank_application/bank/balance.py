from database import DatabaseConfig

class Balance:
    def __init__(self, account:int):
        self.account = account

    def get_balance(self):
        try:
            db_config = DatabaseConfig()
            cursor = db_config.cursor()
            get_balance_query = "SELECT BALANCE FROM ACCOUNTS WHERE ACCOUNT = %s;"
            cursor.execute(get_balance_query, (self.account,))
            amount = cursor.fetchone()[0]
            return f"Your current balance is:{amount}"
        except Exception as e:
            return f"Something wrong in bank/balance.py: {e}"


from database import DatabaseConfig
from bank.utility import addTransaction

class Deposite:
    def __init__(self, account:int, amount:int):
        self.account =account
        self.amount = amount

    def make_deposite(self):
        try:
            db_config = DatabaseConfig()
            cursor = db_config.cursor()
            # get current balance
            current_balance_query = """SELECT BALANCE FROM ACCOUNTS WHERE ACCOUNT = %s;"""
            cursor.execute(current_balance_query, (self.account,))
            curr_amount = cursor.fetchone()[0]
            updated_amount = curr_amount + self.amount
            # update amount in table
            update_amount_query = """UPDATE ACCOUNTS SET BALANCE = %s WHERE ACCOUNT = %s;"""
            cursor.execute(update_amount_query, (updated_amount, self.account))
            # add transaction 
            addTransaction(account=self.account, transaction_type="CREDIT", trans_amount=self.amount)
            db_config.commit()
            cursor.close()
            db_config.close()
            return f"Successfully {self.amount} deposited and Current Balance is {updated_amount}"
        except Exception as e:
            return f"Something wrong in bank/deposite.py:{e}"
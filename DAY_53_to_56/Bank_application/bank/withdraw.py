from database import DatabaseConfig
from bank.utility import addTransaction

class Withdraw:
    def __init__(self, account:int, amount:int):
        self.account =account
        self.amount = amount

    def make_withdraw(self):
        try:
            db_config = DatabaseConfig()
            cursor = db_config.cursor()
            # get current balance
            current_balance_query = """SELECT BALANCE FROM ACCOUNTS WHERE ACCOUNT = %s;"""
            cursor.execute(current_balance_query, (self.account,))
            curr_amount = cursor.fetchone()[0]
            if curr_amount >= self.amount:
                updated_amount = curr_amount - self.amount
                # update amount in table
                update_amount_query = """UPDATE ACCOUNTS SET BALANCE = %s WHERE ACCOUNT = %s;"""
                cursor.execute(update_amount_query, (updated_amount, self.account))
                # add transaction 
                addTransaction(account=self.account, transaction_type="DEBIT", trans_amount=self.amount)
                db_config.commit()
                cursor.close()
                db_config.close()
                return f"Successfully {self.amount} withdrawal and Current Balance is {updated_amount}"
            else:
                return  "Insufficient amount"
        except Exception as e:
            return f"Something wrong in bank/withdraw.py:{e}"
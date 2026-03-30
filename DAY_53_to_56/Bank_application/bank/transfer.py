from database import DatabaseConfig
from bank.utility import addTransaction

class Transfer:
    def __init__(self, from_account:int,to_account:int, trans_amount:int):
        self.from_account =from_account
        self.to_account = to_account
        self.trans_amount = trans_amount

    def make_transfer(self):
        try:
            db_config = DatabaseConfig()
            cursor = db_config.cursor()
            # check to_account exists or not
            check_acccount_exists_query = "SELECT 1 FROM ACCOUNTS WHERE ACCOUNT = %s;"
            cursor.execute(check_acccount_exists_query, (self.to_account,))
            # IF TO_ACCOUNT EXISTS
            if cursor.fetchone():
                # get current balance
                current_balance_query = """SELECT BALANCE FROM ACCOUNTS WHERE ACCOUNT = %s;"""
                cursor.execute(current_balance_query, (self.from_account,))
                from_account_amount = cursor.fetchone()[0]
                cursor.execute(current_balance_query, (self.to_account,))
                to_account_amount = cursor.fetchone()[0]
                if from_account_amount >= self.trans_amount:
                    # first debit from from_account
                    from_account_updated_amount = from_account_amount - self.trans_amount
                    # update amount in table
                    update_amount_query = """UPDATE ACCOUNTS SET BALANCE = %s WHERE ACCOUNT = %s;"""
                    cursor.execute(update_amount_query, (from_account_updated_amount, self.from_account))
                    # add transaction 
                    addTransaction(account=self.from_account, transaction_type="DEBIT", trans_amount=self.trans_amount)
                    
                    ## Credit in to_account 
                   
                    to_account_updated_amount = to_account_amount + self.trans_amount
                    # update amount in table
                    cursor.execute(update_amount_query, (to_account_updated_amount, self.to_account))
                    # add transaction 
                    addTransaction(account=self.to_account, transaction_type="CREDIT", trans_amount=self.trans_amount)
 
                    db_config.commit()
                    cursor.close()
                    db_config.close()
                    return f"Successfully {self.trans_amount} transferd and Current Balance is {from_account_updated_amount}"
                else:
                    return  "Insufficient amount"
            else:
                return "Reciever Account not Exists"
        except Exception as e:
            return f"Something wrong in bank/Transfer.py:{e}"
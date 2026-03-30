from database import DatabaseConfig


class MiniStatement:
    def __init__(self, account):
        self.account =account

    def get_transactions(self):
        try:
            db_config = DatabaseConfig()
            cursor = db_config.cursor(dictionary=True)
            get_transactions_query = """SELECT * FROM TRANSACIONS WHERE ACCOUNT =%s
                                        ORDER BY TRANSACTIONTIME DESC 
                                        LIMIT 10;"""
            cursor.execute(get_transactions_query, (self.account,))
            records = cursor.fetchall()
            return records
        except Exception as e:
            return f"Something wrong in bank/ministatement.py:{e}"
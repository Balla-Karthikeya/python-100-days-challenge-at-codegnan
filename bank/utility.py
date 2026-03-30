from database import DatabaseConfig

# transaction record insertion 

def addTransaction(account:int, transaction_type:str, trans_amount:int):
    try:
        db_config = DatabaseConfig()
        cursor = db_config.cursor()

        trans_insert_query = """INSERT INTO TRANSACTIONS(ACCOUNT, TRANSACTIONTYPE, AMOUNT)
                                VALUES(%s,%s, %s);"""
        cursor.execute(trans_insert_query,(account, transaction_type, trans_amount))
        db_config.commit()
        cursor.close()
        db_config.close()
        return True
    except Exception as e:
        return f"Something wrong in bank/utitlity:{e}"
        
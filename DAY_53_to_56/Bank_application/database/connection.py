# import required modules
import mysql.connector as SQLC

def DatabaseConfig():
    connection = SQLC.connect(
        host = 'localhost',
        user = 'root',
        password = 'root', # your mysql workbenth password
        database = 'bank'
    )
    return connection
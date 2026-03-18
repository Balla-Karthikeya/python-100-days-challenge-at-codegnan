# import mysql connector 
import mysql.connector as SQLC

# database config
database_confi=SQLC.connect(
    host = 'localhost',
    user = 'root',
    password='root',
    database = 'bank' # mysql password 
)

# cursor object creation 
cursor = database_confi.cursor()

# creating database
# cursor.execute("CREATE DATABASE if not exists bank;")
# print("database is created")
# print(database_confi)
# print(cursor)
# query = """
# CREATE TABLE IF NOT EXISTS ACCOUNTS (
#     ACCOUNT_NO INT PRIMARY KEY,
#     PASSWORD VARCHAR(50)
# );
# """
# cursor.execute(query)
# print("Table Created")

# adding data into table 
# insert_data_into_table = """
# INSERT INTO ACCOUNTS(ACCOUNT_NO, PASSWORD)
# ALUES (%s, %s);
 # """

# cursor.execute(insert_data_into_table, (1234, 1234))
# print("Data inserted successfully")
# insert many records
# values = [(1235,1235),(1236,1236),(1237,1237)]
# cursor.executemany(insert_data_into_table, values)
# commiting in dayabase
# database_confi.commit()

 # get table data 
# cursor.execute('select * from accounts')
# print(cursor)

# # fetchall()
# print(cursor.fetchone())
# print(cursor.fetchall())

# get 1236 password 
cursor.execute('select password from accounts where account_no = %s', (1236,))
print(cursor.fetchone())


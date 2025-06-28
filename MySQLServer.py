from mysql.connector import connect, Error
from getpass import getpass

try:
    with connect(
        host = "localhost",
        user = input("Enter Username: "),
        password = getpass("Enter your password: "),
        database = "alx_book_store"
    ) as connection:
        print("Database 'alx_book_store' created successfully!")
except Error as e:
    print(e)
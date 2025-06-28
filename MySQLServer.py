import mysql.connector
from getpass import getpass

try:
    with mysql.connector.connect(
        host = "localhost",
        user = input("Enter Username: "),
        password = getpass("Enter your password: "),
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
except Error as e:
    print(e)
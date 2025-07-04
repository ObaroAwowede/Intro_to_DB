import mysql.connector
from getpass import getpass


book_store_tables = """
CREATE TABLE IF NOT EXISTS Books (
    book_id INT PRIMARY KEY,
    title VARCHAR(130) NOT NULL,
    author_id INT NOT NULL,
    price DOUBLE,
    publication_date DATE,
    FOREIGN KEY (author_id)
    REFERENCES Authors(author_id)
);

CREATE TABLE IF NOT EXISTS Authors (
    author_id INT PRIMARY KEY,
    author_name VARCHAR(215) NOT NULL  
);

CREATE TABLE IF NOT EXISTS Customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(215) NOT NULL,
    email VARCHAR(215) NOT NULL,
    address TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Orders (
    order_id INT PRIMARY KEY,
    customer_id INT NOT NULL,
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

CREATE TABLE IF NOT EXISTS Order_Details (
    orderdetailid INT PRIMARY KEY,
    order_id INT NOT NULL,
    book_id INT NOT NULL,
    quantity DOUBLE,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (book_id) REFERENCES Books(book_id)
);

CREATE TABLE IF NOT EXISTS customer (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(215) NOT NULL,
    email VARCHAR(215) NOT NULL,
    address TEXT NOT NULL
);

"""

description_of_books = """
SELECT
    COLUMN_NAME,
    COLUMN_TYPE,
    IS_NULLABLE,
    COLUMN_KEY,
    COLUMN_DEFAULT,
    EXTRA
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'alx_book_store'
    AND TABLE_NAME = 'Books'
ORDER BY ORDINAL_POSITION
"""

inserting_info_to_customer_table = """
INSERT INTO customer (customer_id,customer_name, email, address)
VALUES
    (1,"Cole Baidoo","cbaidoo@sandtech.com", "123 Happiness Ave.")
"""

multiple_insertions_to_customer_table = """
INSERT INTO customer (customer_id,customer_name, email, address)
VALUES
    (2,"Blessing Malik","bmalik@sandtech.com", "124 Happiness  Ave.")
    (3,"Obed Ehoneah","eobed@sandtech.com", "125 Happiness  Ave.")
    (4,"Nehemial Kamolu","nkamolu@sandtech.com", "126 Happiness  Ave.")
"""
try:
    with mysql.connector.connect(
        host = "localhost",
        user = input("Enter Username: "),
        password = getpass("Enter your password: "),
        database = "alx_book_store"
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
            for table in book_store_tables.strip().split(';'):
                table = table.strip()
                if not table:
                    continue
                cursor.execute(table + ';')
            connection.commit()
            print("Tables created successfully in this database")
               
        with open("task_2.sql", "w") as f:
            f.write(book_store_tables.lstrip())

        with open("task_3.sql", "w") as f:
            f.write("CREATE DATABASE IF NOT EXISTS alx_book_store;\n")
            f.write("USE alx_book_store;\n")
            f.write(book_store_tables.lstrip())
            f.write("\nSHOW TABLES;")
        
        with connection.cursor() as cursor:
                cursor.execute("SHOW TABLES")
                tables = cursor.fetchall()

                if not tables:
                    print(f"No tables found in database.")
                else:
                    print(f"Tables:")
                    for (table_name,) in tables:
                        print(f" - {table_name}")
                        
        with open("task_4.sql","w") as f:
            f.write("USE alx_book_store;\n")
            f.write(description_of_books.strip())
        with open("task_5.sql","w") as f:
            f.write("USE alx_book_store;\n")
            f.write(inserting_info_to_customer_table)
        with open("task_6.sql", "w") as f:
            f.write("USE alx_book_store")
            f.write(multiple_insertions_to_customer_table)
                
except mysql.connector.Error as e:
    print(e)
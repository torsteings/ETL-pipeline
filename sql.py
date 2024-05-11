import mysql.connector
from mysql.connector import Error
import pandas as pd

def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None # Closes any existing connection.
    try: # To handle any potential errors.
        connection = mysql.connector.connect(
        host=host_name,
        user=user_name,
        passwd=user_password,
        database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

# Default user name is root.
pw = "*****"
db = "school"
connection = create_db_connection("localhost", "root", pw, db)

def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")

# create_database_query = "CREATE DATABASE school"
# create_database(connection, create_database_query)

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

create_teacher_table = """
CREATE TABLE teacher (
    teacher_id INT PRIMARY KEY,
    first_name VARCHAR(40) NOT NULL,
    last_name VARCHAR(40) NOT NULL,
    language_1 VARCHAR(3) NOT NULL,
    language_2 VARCHAR(3),
    dob DATE,
    tax_id INT UNIQUE,
    phone_no VARCHAR(20)
    );
"""

connection = create_db_connection("localhost", "root", pw, db)
execute_query(connection, create_teacher_table)

create_client_table = """
CREATE TABLE client (
    client_id INT PRIMARY KEY,
    client_name VARCHAR(40) NOT NULL,
    address VARCHAR(60) NOT NULL,
    industry VARCHAR(20)
);
"""
connection = create_db_connection("localhost", "root", pw, db)
execute_query(connection, create_client_table)





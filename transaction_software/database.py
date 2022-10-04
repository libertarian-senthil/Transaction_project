"""
This module is used to interact with the datbase and perform operations on the database.
"""
import os
import re
from inspect import currentframe

from mysql.connector import connect
from mysql.connector.errors import ProgrammingError
from mysql.connector.connection_cext import CMySQLConnection

from utils.logs import database_error
from utils.generate_rand_num import generate_account_number
from utils.sql_statements import (
    SHOW_TABLES,
    SELECT_ALL_CUSOMTERS,
    INSERT_CUSTOMER
)

# Get the database username and password stored in the environment variables.
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASS')
DB = 'boi'  # database name is set to 'boi' by default.

def check_if_mysql_is_installed()->None:
    """
    Check for MySQL installation.
    """
    if os.system("mysql --version") == 1:
        database_error(msg="MySQL is not installed", line_no = currentframe().f_lineno) #type: ignore

def connect_to_database():
    """
    Connect with the boi database.
    """
    config = {
        "host"    :"localhost",
        "username": DB_USER,
        "password": DB_PASSWORD,
        "database": DB
        }
    try:
        return connect(**config)
    except ProgrammingError as e:
        if 'Unknown Database' in str(e):
            database_error(msg=f"'{DB}' database doesn't exists",line_no = currentframe().f_lineno) #type: ignore
            check_if_mysql_is_installed()

def disconnect_database(connection)->None:
    """
    Close the connection with boi Database.
    """
    connection.close()

def is_email(email:str)->bool:
    """
    Return True if it is email else return false.

    parameter:
    ----------
    email:str
        email is given as input.

    Return:
    -------
        Return true if it is email else return as false.
    """
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return True if (re.fullmatch(pattern,email)) else False

# TODO: complete the following functions.
# create bank accout
def create_account(debit_account_number:int, user_name:str, gender:str,    address:str, phone_number:str, email:str, aadhar_number:str,    account_type:str, balance:int, account_status:str = "active")->None:
    val= [debit_account_number, user_name, gender, address, phone_number, email, aadhar_number,account_type, balance, account_status]

    connection = connect_to_database()
    cursor = connection.cursor() # type:ignore
    cursor.execute(INSERT_CUSTOMER,val)
    connection.commit() # type:ignore

# perform transaction between two account.
def perform_transaction()->None:
    pass

# Update the account information.
def update_account_info()->None:
    pass

# delete an account information.
def remove_account()->None:
    pass

# Search account.
def search_account_info()->None:
    pass

# def View customer list.
def view_customer_list()->None:
    pass



# drive code
if __name__ == "__main__":
    pass

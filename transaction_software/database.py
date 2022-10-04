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
    INSERT_CUSTOMER,
    REMOVE_ACC,
    SEARCH_ACC
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

def connect_to_database()->object:
    """
    Connect with the boi database.

    Return:
    -------
        Returns the database connection object.
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

# TODO: comple the functions
# perfomr_transaction()
# update_account_info()
# view_customer_list()

def create_account(debit_account_number:int, user_name:str, gender:str,    address:str, phone_number:str, email:str, aadhar_number:str,    account_type:str, balance:int, account_status:str = "active")->None:
    """ Create a bank account

    Parameters:
    -----------
    debit_account_number:int
        the account number.
    user_name:str
        User name for creating an account.
    gender:str
        Idenfication of gender value is "M" or "F"
    address:str
        address for the account.
    phone_number:str
        phone number for the account .
    email:str
        email for the account.
    aadhar_number:str
        aadhar number for account
    account_type:str
        type of account either savings or current.
    balance:int
        account balance amount.
    account_status:str
        status of the account either active or inactive.

    Return: None
    """
    val= [debit_account_number, user_name, gender, address, phone_number, email, aadhar_number,account_type, balance, account_status]

    connection = connect_to_database()
    cursor = connection.cursor() # type:ignore
    cursor.execute(INSERT_CUSTOMER,val)
    connection.commit() # type:ignore
    connection.close() # type:ignore

# perform transaction between two account.
def perform_transaction()->None:
    pass

# Update the account information.
def update_account_info()->None:
    pass

# delete an account information.
def remove_account(debit_account_number:int)->None:
    """ Remove a bank account by using the debit_account_number
    Parameters:
    -----------
    debit_account_number:int
        the account number.
    """
    connection = connect_to_database()
    cursor = connection.cursor() #type:ignore
    val = [debit_account_number]
    cursor.execute(REMOVE_ACC,val)
    connection.commit() #type:ignore
    connection.close() #type:ignore


# Search account.
def search_account_info(debit_account_number:int)->tuple[bool,list]:
    """ Search account details and return a tuple of boolean(account is found) and list(customer details. if no detail exists return empty list)

    Parameters:
    -----------
    debit_account_number:int
        the account number.

    Return: tuple[bool,list]
    ------
        Tuple of boolean and a list.
        bool: account is found or not.
        list: customer details, if no detail exists return empty list.
    """
    connection = connect_to_database()
    cursor = connection.cursor() #type:ignore
    val = [debit_account_number]
    cursor.execute(SEARCH_ACC,val)
    customer = cursor.fetchone()
    if customer is not None:  # type: ignore
        return (True,customer)
    else:
        return (False, [])



# def View customer list.
def view_customer_list()->None:
    pass

# drive code
if __name__ == "__main__":
    pass

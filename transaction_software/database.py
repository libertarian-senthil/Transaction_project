"""
This module is used to interact with the datbase and perform operations on the database.
"""
import os
import re
import time
# from inspect import currentframe

from mysql.connector import connect
from mysql.connector.connection_cext import CMySQLConnection
from mysql.connector.errors import ProgrammingError

from utils.generate_rand_num import generate_account_number
# from utils.logs import database_error
from utils.sql_statements import (INSERT_CUSTOMER, REMOVE_ACC, SEARCH_ACC,
                                  SELECT_ALL_CUSOMTERS, SHOW_TABLES,
                                  UPDATE_ACC)

# Get the database username and password stored in the environment variables.
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASS')
DB = 'boi'  # database name is set to 'boi' by default.

def check_if_mysql_is_installed()->bool:
    """Check for MySQL Installation.

    Returns:
        bool: True if installed else false.
    """
    if os.system("mysql --version") == 1:
        # database_error(msg="MySQL is not installed", line_no = currentframe().f_lineno) #type: ignore
        print("Mysql is not installed on your system!")
        return False
    else:
        return True

def connect_to_database():
    """
    Connect with the boi database.

    Return:
    -------
        Returns the database connection object if connected else return flag value False.
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
        # if 'Unknown Database' in str(e):
        #     database_error(msg=f"'{DB}' database doesn't exists",line_no = currentframe().f_lineno) #type: ignore
        print("ERROR:",e,"\n")
        is_mysql_installed = check_if_mysql_is_installed()
        return is_mysql_installed

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

def create_account(debit_account_number:int, user_name:str, gender:str,    address:str, phone_number:str, email:str, aadhar_number:str,    account_type:str, balance:int, account_status:str = "active",*args, **kwargs)->bool:
    """Create an account.

    Args:
        debit_account_number (int): the account number.
        user_name (str): User name for creating an account.
        gender (str): Idenfication of gender value is "M" or "F".
        address (str): address for the account.
        phone_number (str): phone number for the account.
        email (str): email for the account.
        aadhar_number (str): aadhar number for account.
        account_type (str): type of account either savings or current.
        balance (int): account balance amount.
        account_status (str, optional): status of the account either active or inactive, Defaults to "active".

    Returns:
        bool: True if account created else false
    """
    try:
        val= [debit_account_number, user_name, gender, address, phone_number, email, aadhar_number,account_type, balance, account_status]

        connection = connect_to_database()
        cursor = connection.cursor() # type:ignore
        cursor.execute(INSERT_CUSTOMER,val)
        connection.commit() # type:ignore
        connection.close() # type:ignore
        return True
    except:
        return False

# perform transaction between two account.
def perform_transaction()->None:
    pass

# delete an account information.
def remove_account(debit_account_number:int)->bool:
    """Remove an account

    Args:
        debit_account_number (int): the account number.

    Returns:
        bool: True if account removed else false.
    """
    try:
        connection = connect_to_database()
        cursor = connection.cursor() #type:ignore
        val = [debit_account_number]
        cursor.execute(REMOVE_ACC,val)
        connection.commit() #type:ignore
        connection.close() #type:ignore
        return True
    except:
        return False

# Search account.
def search_account_info(debit_account_number:int)->tuple[bool,list]:
    """Search account details and return a tuple of boolean(account is found) and list(customer details. if no detail exists return empty list)

    Args:
        debit_account_number (int): the account number.

    Returns:
        tuple[bool,list]: tuple of bool and list. bool represent account found(True) or not found(False) and list represent the customer details.
    """
    connection = connect_to_database()
    cursor = connection.cursor() #type:ignore
    val = [debit_account_number]
    cursor.execute(SEARCH_ACC,val)
    customer = cursor.fetchone()
    connection.close() # type:ignore
    if customer is not None:  # type: ignore
        return (True,customer)
    else:
        return (False, [])



# def View customer list.
def view_customer_list()->None:
    pass

# Update the account information.
def update_account_info(**kwargs)->bool:
    """Update the account information

    Returns:
        bool: True if updated else False.
    """
    try:
        data = kwargs
        connection = connect_to_database()
        cursor= connection.cursor() #type: ignore
        val= (data['user_name'], data['gender'], data['address'],data['phone_number'], data['email'], data['aadhar_number'],data['debit_account_number'])
        cursor.execute(UPDATE_ACC,val)
        connection.commit() # type:ignore
        connection.close() # type:ignore
        return True
    except Exception as e:
        return False


# drive code
if __name__ == "__main__":
    pass

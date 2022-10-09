"""
This module is used to interact with the datbase and perform operations on the database.
"""
import os
import re
import time

from mysql.connector import connect
from mysql.connector.connection_cext import CMySQLConnection
from mysql.connector.errors import DatabaseError, ProgrammingError,IntegrityError

from utils.generate_rand_num import generate_account_number
from utils.sql_statements import (INSERT_CUSTOMER, REMOVE_ACC, SEARCH_ACC,
                                  SEARCH_ACC_WITH_UPI, SELECT_ALL_CUSOMTERS,
                                  SHOW_TABLES, UPDATE_ACC)

# from inspect import currentframe



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

# Search account.
def search_account_info(debit_account_number, upi_password=None, upi_match=False):
    """Search account details and return a tuple of boolean(account is found) and list(customer details. if no detail exists return empty list)

    Args:
        debit_account_number (int): the account number.
        upi_password (None): default is None.
        upi_match (bool): default is False.


    Returns:
        tuple[bool,list,int]: tuple of bool,list and bool.
            bool =  account found(True) or not found(False).
            list = represent the customer details.
            int = represent whether the given upi_password is a match(1) ot not(0). if upi_match is set to None then (-1).
                codes:
                    code 1 = found a match.
                    code 0 = not found a match.
                    code -1 = upi_match is False
                    code -2 = upi_match is True and upi_password is None.
    """
    connection = connect_to_database()
    cursor = connection.cursor() #type:ignore
    if upi_match is False:
        val = [debit_account_number]
        cursor.execute(SEARCH_ACC,val)
        customer = cursor.fetchone()
        connection.close() # type:ignore
        if customer is not None:  # type: ignore
            return (True,customer,-1)
        else:
            return (False, [],-1)
    elif upi_match is True and upi_password is None:
        return(False,[],-2)
    elif upi_match is True and upi_password is not None:
        val = [debit_account_number,upi_password]
        cursor.execute(SEARCH_ACC_WITH_UPI,val)
        customer = cursor.fetchone()
        connection.close() # type:ignore
        if customer is not None:  # type: ignore
            return (True,customer,1)
        else:
            return (False, [],0)
    else:
        print("ERROR: In database.py Check search_account_info()")

def create_account(**kwargs)->int:
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
        int: 1 for created, 0 for not created, -1 for already an account found.
    """
    try:
        data = kwargs
        connection = connect_to_database()
        cursor = connection.cursor() # type:ignore
        val = [data["debit_account_number"], data["user_name"], data["gender"], data["address"], data["phone_number"], data["email"], data["aadhar_number"], data["account_type"], data["balance"], data["account_status"], data["upi_password"]]
        cursor.execute(INSERT_CUSTOMER,val)
        connection.commit() # type:ignore
        connection.close() # type:ignore
        return 1
    except ProgrammingError as e:
        return 0
    except IntegrityError as e:
        return -1
    except DatabaseError as e:
        return 0



# perform transaction between two account.
def perform_transaction()->None:
    pass

# delete an account information.
def remove_account(debit_account_number:int, upi_password:str):  # type: ignore
    """Remove an account

    Args:
        debit_account_number (int): the account number.

    Returns:
        tuple(bool, int):
            bool = True if account removed else false.
            int = 1 if upi_password is correct, 0 if wrong, -1 if error occured.
    """
    try:
        connection = connect_to_database()
        cursor = connection.cursor() #type:ignore
        val = [debit_account_number, upi_password]
        cursor.execute(REMOVE_ACC,val)
        customer_found, customer,password_match_code = search_account_info(debit_account_number,upi_match=True, upi_password=upi_password)  # type: ignore
        connection.commit() #type:ignore
        connection.close() #type:ignore
        if password_match_code == -1:
            return(False, 0)
        elif password_match_code == 1:
            return(True, 1)
    except:
        return (False, -1)

# def View customer list.
def view_customer_list():
    connection = connect_to_database()
    cursor = connection.cursor() # type: ignore
    cursor.execute(SELECT_ALL_CUSOMTERS)
    customers_list = cursor.fetchall()
    return customers_list

def check_balance():
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

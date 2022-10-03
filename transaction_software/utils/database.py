"""
This module is used to interact with the datbase and perform operations on the database.
"""
import os
import re
from inspect import currentframe

from mysql.connector import connect
from mysql.connector.errors import ProgrammingError

from logs import database_error

# Get the database username and password stored in the environment variables.
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASS')
DB = 'boi'  # database name is set to 'boi' by default.

def check_if_mysql_is_installed()->None:
    if os.system("mysql --version") == 1:
        database_error(msg="MySQL is not installed", line_no = currentframe().f_lineno) #type: ignore

def connect_to_database()->object:
    try:
        bank_of_indians = connect(
        host="localhost",
        username= DB_USER,
        password= DB_PASSWORD,
        database= DB
        )
        return bank_of_indians.cursor()
    except ProgrammingError as e:
        if 'Unknown database' in str(e):
            database_error(msg=f"'{DB}' database doesn't exists",line_no = currentframe().f_lineno) #type: ignore
            check_if_mysql_is_installed()
    else:
        print("database connected successfully.")

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
def create_account()->None:
    pass

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
    cursor = connect_to_database()   # test code

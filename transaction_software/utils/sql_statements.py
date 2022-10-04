"""
This module contains SQL statements required to be use by mysql-connector
"""

SELECT_ALL_CUSOMTERS = "SELECT * FROM customer"
SHOW_TABLES = "SHOW TABLES"
INSERT_CUSTOMER = "INSERT INTO customer(debit_account_number, user_name, gender, address, phone_number, email, aadhar_number, account_type, balance, account_status) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"


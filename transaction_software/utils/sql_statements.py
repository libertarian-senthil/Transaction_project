"""
This module contains SQL statements required to be use by mysql-connector
"""

SELECT_ALL_CUSOMTERS = "SELECT user_name, debit_account_number FROM customer"
SHOW_TABLES = "SHOW TABLES"
INSERT_CUSTOMER = "INSERT INTO customer(debit_account_number, user_name, gender, address, phone_number, email, aadhar_number, account_type, balance, account_status, upi_password) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

REMOVE_ACC = "DELETE FROM customer where debit_account_number = %s and upi_password = %s"

SEARCH_ACC = "SELECT * FROM customer where debit_account_number = %s"
SEARCH_ACC_WITH_UPI = "SELECT * FROM customer where debit_account_number = %s and upi_password = %s"
UPDATE_ACC = "UPDATE customer SET user_name = %s, gender = %s, address = %s, phone_number = %s, email =  %s, aadhar_number =%s where debit_account_number = %s"

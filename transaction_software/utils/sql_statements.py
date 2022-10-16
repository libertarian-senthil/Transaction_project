"""
This module contains SQL statements required to be use by mysql-connector
"""

SELECT_ALL_CUSOMTERS = "SELECT user_name, debit_account_number FROM customer"
INSERT_CUSTOMER = "INSERT INTO customer(debit_account_number, user_name, gender, address, phone_number, email, aadhar_number, account_type, balance, account_status, upi_password) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

INSERT_DELETED_CUSTOMER = "INSERT INTO deleted_account_info(debit_account_number, upi_password, user_name, gender, address phone_number, email, aadhar_number, account_type, account_status, balance) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

REMOVE_ACC = "DELETE FROM customer where debit_account_number = %s and upi_password = %s"

SEARCH_ACC = "SELECT * FROM customer where debit_account_number = %s"
SEARCH_ACC_WITH_UPI = "SELECT * FROM customer where debit_account_number = %s and upi_password = %s"
UPDATE_ACC = "UPDATE customer SET user_name = %s, gender = %s, address = %s, phone_number = %s, email =  %s, aadhar_number =%s where debit_account_number = %s"
UPDATE_AMT = "UPDATE customer SET balance = %s where debit_account_number = %s"
INSERT_TRANS_DATA = "INSERT INTO transaction_table(trans_id, debit_account_number ,credit_account_number, trans_amt) values (%s, %s, %s, %s)"

TURN_OFF_FK = "SET FOREIGN_KEY_CHECKS=0"
TURN_ON_FK = "SET FOREIGN_KEY_CHECKS=1"

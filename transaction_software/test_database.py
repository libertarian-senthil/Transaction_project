import os
import random
import string
import unittest

from mysql.connector.errors import ProgrammingError

from database import (check_if_mysql_is_installed, create_account,
                      remove_account, connect_to_database,is_email, search_account_info, update_account_info)

# Variables generating the
debit_account_number = int('113121'+str(random.randint(0,9999999999)))
upi_password = random.choice(seq=string.ascii_letters) + str(random.randint(0,9999))
user_name = random.choice(seq=["aabid","aabida","aachal","aadesh","aadil","aadish","aaditya","aaenab","aafreen","aafrin","aaftaab","aaftab","aagand","aahim","aajad","aajiv","aakanksha","aakar","aakas","aakash"])
gender = random.choice(["M","F"])
phone_number = random.randint(0,9999999999)
aadhar_number = random.randint(0,9999999999)
email = ''.join(random.choice(string.ascii_letters) for x in range(7)) + "@gmail.com"
savings_type = random.choice(["savings", "current"])

num = random.randint(0,1000000)


class TestDatabase(unittest.TestCase):

    def setUp(self) -> None:
        self.data = {
    "debit_account_number": debit_account_number,
    "user_name"           : user_name,
    "gender"              : gender,
    "address"             : "address",
    "phone_number"        : phone_number,
    "aadhar_number"       : aadhar_number,
    "account_type"        : savings_type,
    "email"               : email,
    "account_status"      : "active",
    "balance"             : num ,
    "upi_password"        : upi_password}
        self.email = "libertarian@.com"
        self.update_data = {
            "user_name"           : user_name,
            "gender"              : gender,
            "address"             : "address",
            "phone_number"        : phone_number,
            "email"               : email,
            "aadhar_number"       : aadhar_number,
            "debit_account_number": debit_account_number}

    def test_create_account(self):
        self.assertEqual(create_account(**self.data), 1) # test for account creation
        self.assertNotEqual(create_account(**self.data), 0) # database error or programmer error fduring account creation
        self.assertEqual(create_account(**self.data), -1) # test for duplicate account identification

    def test_remove_account(self):

        removed, code = remove_account(debit_account_number, upi_password)  # type: ignore
        self.assertEqual((removed, code), (True, 1)) # test for successful removal.
        self.assertNotEqual((removed, code), (False, 0)) # test for failed removal due to incorrect password
        self.assertNotEqual((removed, code), (False, -1)) # test for error occurred  during the account removal

    def test_check_if_mysql_is_installed(self):
        self.assertEqual(check_if_mysql_is_installed(), True)
        self.assertNotEqual(check_if_mysql_is_installed(), False)

    def test_connec_to_database(self):
        self.assertNotEqual(connect_to_database(),ProgrammingError)  # type: ignore
    def test_is_email(self):
        self.assertEqual(is_email(email), True)
        self.assertEqual(is_email(self.email), False)
    def search_account_info(self):
        found, customer, code = search_account_info(debit_account_number)  # type: ignore
        self.assertEqual(found, True)
        self.assertEqual(code, 1)

    def test_update_account_info(self):
        self.assertEqual(update_account_info(**self.update_data), True)
        self.assertNotEqual(update_account_info(**self.update_data), False)

if __name__ =="__main__":
    unittest.main()


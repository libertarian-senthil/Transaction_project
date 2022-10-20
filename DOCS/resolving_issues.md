# 1. Solution to the Issues faced

>**Note:** This document illustrates the issues(errors, Exceptions, etc.,) raised during the development of this project(software).

    References to the terms used in the documentation

    DATE                  -> Refers to the date of issue found or encountered.
    ISSUE                 -> Brief message about the encountered issue.
    RESOLUTION            -> Solutions applied to resolve the issue.
    COMMIT MSG REFERENCE  -> Issues raised or found to be exists after this commit message.

* **DATE:** *`05-10-2022`*
  * **ISSUE:** Met with Exception in [`transaction_software\database.py`][1] update_account_information.
  * **RESOLUTION:** Ran multiple debugging session and found that the key *aadhar_number* was mispelled as *aadhar*

* **DATE:** *`05-10-2022`*
  * **ISSUE:** Met with DatabaseError in [`transaction_software\database.py`][1] update_account_information.
  * **RESOLUTION:** instead of passing the list tried to pass the dictionary object which caused the error.

* **DATE:** *`16-10-2022`*
  * **ISSUE:** Met with TypeError in [`transaction_software\main_cli.py`][2] in getting the sender balance from database.
  * **RESOLUTION:** Noticed that balance value returned was found to be string type so it was typcast to int.
  * **COMMIT MSG REFERENCE:** "Needs debug"

* **DATE:** *`16-10-2022`*
  * **ISSUE:** Met with TypeError in [`transaction_software\main_cli.py`][2] in getting the sender balance from database.
  * **RESOLUTION:** Noticed that balance value returned was found to be string type so it was typcast to int.
  * **COMMIT MSG REFERENCE:** "Needs debug"

* **DATE:** *`16-10-2022`*
  * **ISSUE:** Met with IntegrityError in [`transaction_software\database.py`][1] in removing a account from customer table.
  * **RESOLUTION:** The issue was due to [Error code 1451][Error_1451] and was rectified by turning off the foreign key check initially after the removal of the account it was turned on back.
  * **COMMIT MSG REFERENCE:** "Needs debug"

* **DATE:** *`16-10-2022`*
  * **ISSUE:** Met with IntegrityError in [`transaction_software\database.py`][1] in removing a account from customer table.
  * **RESOLUTION:** Not yet found.
  * **COMMIT MSG REFERENCE:** "New Bug"

<!-- links -->
[1]: ../transaction_software/database.py
[2]: ../transaction_software/main_cli.py

[Error_1451]: https://dev.mysql.com/doc/mysql-errors/8.0/en/server-error-reference.html#error_er_row_is_referenced_2

# 1. Solution to the Issues faced

* **Date:** *`05-10-2022`*
  * **ISSUE:** Met with Exception in [`transaction_software\database.py`][1] update_account_information.
  * **Resolution:** Ran multiple debugging session and found that the key *aadhar_number* was mispelled as *aadhar*

* **Date:** *`05-10-2022`*
  * **ISSUE:** Met with DatabaseError in [`transaction_software\database.py`][1] update_account_information.
  * **Resolution:** instead of passing the list tried to pass the dictionary object which caused the error.

*
<!-- links -->
[1]: ../transaction_software/database.py

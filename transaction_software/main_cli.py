"""
Main command line interface to interact with the user and the software. All the operations to be performed are listed and called the needed functions and methods to accomplish the tasks.
"""

import os
import time
from database import create_account, is_email
from utils.generate_rand_num import generate_account_number

def _display_main()->None:
    """
    Display the user
    """
    while True:
        # To be cleared after the UI is developed.
        # Clear the terminal screen in linux, Mac and in windows.
        os.system("cls" if os.name =="nt" else "clear")

        print("""\
<<Welcome to Bank of Indians>>

1. Create an Account.
2. Perform a Transaction.
3. Update an Acccount Information.
4. Delete an Account.
5. Search an Account Information.
6. View Customer's List.
7. Exit.
""")
        try:
            user_choice = int(input("Please Enter your choice: "))
            # Create Account.
            if user_choice == 1:
                # Get and Check email.
                email = input("Enter email: ")
                if is_email(email) is False:
                    print("Entered invalid email")
                    time.sleep(3.0)
                    continue

                debit_account_number = generate_account_number()
                user_name = input("Enter user_name: ")
                gender = input("Enter gender(M/F): ").capitalize()
                if gender not in ["M","F"]:
                    print("Invalid gender input")
                    time.sleep(3.0)
                    continue
                address = input("Enter address: ")
                phone_number = int(input("Enter phone_number: "))
                aadhar_number = int(input("Enter aadhar_number: "))
                account_type = input("Enter account_type: "),
                balance = int(input("Enter account balance: "))
                create_account(debit_account_number, user_name, gender, address, phone_number,email, aadhar_number, account_type, balance) #type: ignore
                break
            elif user_choice == 2:
                pass
            elif user_choice == 3:
                pass
            elif user_choice == 4:
                pass
            elif user_choice == 5:
                pass
            elif user_choice == 6:
                pass
            elif user_choice == 7: # exit the program
                print("\nProgram terminated...\n")
                break
            else:
                print("Invalid Choice...")
        except ValueError as e:
            print("Invalid input",e)
            time.sleep(3.0)




if __name__ == "__main__":
    _display_main()

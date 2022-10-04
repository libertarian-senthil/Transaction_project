"""
Main command line interface to interact with the user and the software. All the operations to be performed are listed and called the needed functions and methods to accomplish the tasks.
"""

import os
import time
from database import create_account, is_email, remove_account, search_account_info, update_account_info
from utils.generate_rand_num import generate_account_number
from mysql.connector.errors import IntegrityError

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
                account_type = input("Enter account_type: ")
                balance = int(input("Enter account balance: "))
                create_account(debit_account_number, user_name, gender, address, phone_number,email, aadhar_number, account_type, balance) #type: ignore
                print("Account created successfully...")
                time.sleep(3.0)
                continue
            elif user_choice == 2:
                pass
            elif user_choice == 3:
                acc_num = int(input("Enter Account number: "))
                update_account_info(acc_num)
                print("Account updated successfully...")
                time.sleep(3.0)
                continue

            # Delete an account
            elif user_choice == 4:
                account_number = int(input("Enter the account number: "))
                remove_account(account_number)
                print("Account removed successfully...")
                time.sleep(3.0)
                continue
            # Search account information
            elif user_choice == 5:
                acc_num = int(input("Enter account number: "))
                flag, customer = search_account_info(acc_num)
                if flag is not False:
                    # print("\nAccount number: "customer[0],"\nAccount holder: ",customer[1],f"{customer[1]}'s gender: ",customer[2],"")
                    pass
                else:
                    print("No customers found!")
            elif user_choice == 6:
                pass
            elif user_choice == 7: # exit the program
                print("\nProgram terminated...\n")
                break
            else:
                print("Invalid Choice...")
        except ValueError as e:
            print("Invalid input\nError message:",e)
            time.sleep(3.0)
        except IntegrityError as e:
            print("Already an account exists\nError message:",e)




if __name__ == "__main__":
    _display_main()

"""
Main command line interface to interact with the user and the software. All the operations to be performed are listed and called the needed functions and methods to accomplish the tasks.
"""

import os
import time
from database import create_account, is_email, remove_account, search_account_info, update_account_info, view_customer_list
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
                upi_password = input("Enter upi_password(8 alphanumberic character): ")
                gender = input("Enter gender(M/F): ").capitalize()
                if gender not in ["M","F"]:
                    print("Invalid gender input!")
                    time.sleep(3.0)
                    continue
                address = input("Enter address: ")
                phone_number = int(input("Enter phone_number: "))
                aadhar_number = int(input("Enter aadhar_number: "))
                account_type = input("Enter account_type(savings/current): ")
                if gender not in ["M","F"]:
                    print("Invalid account type!")
                    time.sleep(3.0)
                    continue
                balance = int(input("Enter account balance: "))
                data = {
                    "debit_account_number": debit_account_number,
                    "user_name"           : user_name,
                    "gender"              : gender,
                    "address"             : address,
                    "phone_number"        : phone_number,
                    "aadhar_number"       : aadhar_number,
                    "account_type"        : account_type,
                    "email"               : email,
                    "account_status"      : "active",
                    "balance"             : balance,
                    "upi_password"        : upi_password
                }
                creation_status = create_account(**data)
                if creation_status is True:
                    print("Account created successfully...")
                    time.sleep(3.0)
                    continue
                else:
                    print("Account creation failed...")
                    time.sleep(3.0)
                    continue
            elif user_choice == 2:
                pass

            # Update an Acccount Information.
            elif user_choice == 3:
                debit_account_number = int(input("Enter Account number: "))
                flag, customer, code = search_account_info(debit_account_number)  # type: ignore
                if flag is not False: # acccount is found logic.
                    user_name = input("Enter username: ")
                    gender = input("Enter Gender(M/F): ")
                    address = input("Enter address: ")
                    phone_number = input("Enter phone number: ")
                    aadhar_number = input("Enter aadhar number: ")
                    while True:
                        email = input("Enter E-Mail: ")
                        if is_email(email) is False:
                                    print("Entered invalid email!")
                                    time.sleep(3.0)
                                    continue
                        else:
                            break
                    data = {
                        "user_name"           : user_name,
                        "gender"              : gender,
                        "address"             : address,
                        "phone_number"        : phone_number,
                        "email"               : email,
                        "aadhar_number"       : aadhar_number,
                        "debit_account_number": debit_account_number
                    }
                    update_status = update_account_info(**data)
                    if update_status == True:
                        print("Account updated successfully...")
                        time.sleep(3.0)
                        continue
                    else:
                        print(f"ERROR: Updation failed!",)
                else:
                    print(f"INFO: {debit_account_number} account is not found!\n updation failed!")
                    time.sleep(3.0)
                    continue

            # Delete an account
            elif user_choice == 4:
                account_number = int(input("Enter the account number: "))
                upi_password = input("Enter upi_password: ")
                remove_status, wrong_password = remove_account(account_number, upi_password)  # type: ignore
                if remove_status is True:
                    print("Account removed successfully...")
                    time.sleep(3.0)
                    continue
                else:
                    print("Account removal failed...")
                    time.sleep(3.0)
                    continue
            # Search account information
            elif user_choice == 5:
                acc_num = int(input("Enter account number: "))
                flag, customer ,code= search_account_info(acc_num)  # type: ignore
                if flag is not False:
                    print(f"""
Account holder's details

Account number        : {customer[0]}
Account holder        : {customer[2]}
Gender                : {customer[3]}
Address               : {customer[4]}
Contact number        : {customer[5]}
E-mail                : {customer[6]}
Aadhar number         : {customer[7]}
Account type          : {customer[8]}
Account status        : {customer[9]}
Account balance       : Rs.{customer[10]}/-
""")
                    choice = input("\nTo go back to main menu press Y or N to exit the program: ").capitalize()
                    if choice == "Y":
                        continue
                    elif choice == "N":
                        print("\nProgram terminated...")
                        break
                else:
                    print("No customers found!")

            # View customer list
            elif user_choice == 6:
                customer_list = view_customer_list()
                print()
                for i, customer in enumerate(customer_list):  # type: ignore
                    print(str(i+1)+")",customer[0],"->",customer[1])
                choice = input("\nTo go back to main menu press Y or N to exit the program: ").capitalize()
                if choice == "Y":
                    continue
                elif choice == "N":
                    print("\nProgram terminated...")
                    break
                else:
                    print("\nInvalid input!")
                    time.sleep(3.0)
                    continue
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

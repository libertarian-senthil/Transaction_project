"""
Main command line interface to interact with the user and the software. All the operations to be performed are listed and called the needed functions and methods to accomplish the tasks.
"""

import os
import time

from mysql.connector.errors import IntegrityError

from database import (create_account, is_email, perform_transaction,
                      remove_account, search_account_info, update_account_info,
                      view_customer_list)
from utils.generate_rand_num import generate_account_number, generate_trans_id


def display_main() -> None:
    """
    Display the user
    """
    while True:
        # To be cleared after the UI is developed.
        # Clear the terminal screen in linux, Mac and in windows.
        os.system("cls" if os.name == "nt" else "clear") # nosec B605

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
            user_choice = int(input("Please Enter your choice: ").strip())
            # Create Account.
            if user_choice == 1:
                # Get and Check email.
                email = input("Enter email: ").strip()
                if is_email(email) is False:
                    print("Entered invalid email")
                    time.sleep(3.0)
                    continue

                debit_account_number = generate_account_number()
                user_name = input("Enter user_name: ").strip()
                upi_password = input(
                    "Enter upi_password(8 alphanumberic character): ").strip()
                gender = input("Enter gender(M/F): ").capitalize().strip()
                if gender not in ["M", "F"]:
                    print("Invalid gender input!")
                    time.sleep(3.0)
                    continue
                address = input("Enter address: ").strip()
                phone_number = int(input("Enter phone_number: ").strip())
                aadhar_number = int(input("Enter aadhar_number: ").strip())
                account_type = input("Enter account_type(savings/current): ").strip()
                if gender not in ["M", "F"]:
                    print("Invalid account type!")
                    time.sleep(3.0)
                    continue
                balance = int(input("Enter account balance: ").strip())
                data = {
                    "debit_account_number": debit_account_number,
                    "user_name": user_name,
                    "gender": gender,
                    "address": address,
                    "phone_number": phone_number,
                    "aadhar_number": aadhar_number,
                    "account_type": account_type,
                    "email": email,
                    "account_status": "active",
                    "balance": balance,
                    "upi_password": upi_password
                }
                creation_status = create_account(**data)
                if creation_status == 1:
                    print("Account created successfully...")
                    time.sleep(3.0)
                    continue
                else:
                    print("Account creation failed...")
                    time.sleep(3.0)
                    continue
            # Perform transaction
            elif user_choice == 2:
                # sender side input details.
                sender_acc_number = int(input("Enter your account number:").strip())
                sender_upi_numeber = input("Enter your UPI password:")
                is_sender, sender_detail, password_match = search_account_info(
                    debit_account_number= sender_acc_number, upi_password=sender_upi_numeber,
                    upi_match= True)  # type: ignore
                if password_match == 0:
                    print("Pasword doesn't match the account!!...")
                    time.sleep(3.0)
                    continue
                # receiver side input details.
                receiver_acc_number = int(input("Enter Receiver account number:").strip())
                is_receiver, receiver_detail, password_match = search_account_info(
                    receiver_acc_number)  # type: ignore
                if is_sender is True and is_receiver is True:
                    while True:
                        t_amount = int(input("Enter the amount:").strip())
                        sender_balance = int(sender_detail[10])
                        receiver_balance = receiver_detail[10]
                        if t_amount > sender_balance:
                            print("Insufficent funds!")
                            opt = input(
                                "\nTo exit program Press 'q': ").strip().upper()
                            if opt == 'Q':
                                quit()
                            continue
                        elif t_amount <= sender_balance:
                            trans_id = generate_trans_id()
                            # step 6
                            data = {
                                'sender_balance': sender_balance,
                                't_amount': t_amount,
                                'sender_acc_number': sender_acc_number,
                                'receiver_balance': receiver_balance,
                                'receiver_acc_number': receiver_acc_number,
                                'trans_id': trans_id
                            }
                            flag = perform_transaction(**data)
                            if flag == 0 :
                                print("Transaction Unsuccessful")
                                time.sleep(3.0)
                                continue
                            elif flag == 1:
                                print("Transaction Successful")
                                time.sleep(3.0)
                                break
                        elif t_amount < 0:
                            print("Invalid fund amount!")
                            time.sleep(3.0)
                            continue
                    continue
                else:
                    if is_receiver is False and is_sender is True:
                        print(
                            f"The Account:{receiver_acc_number} is not found to be exists...")
                        time.sleep(3.0)
                        continue
                    elif is_receiver is True and is_sender is False:
                        print(
                            f"The Account:{search_account_info} is not found to be exists...")
                        time.sleep(3.0)
                        continue
                    else:
                        print("Both the accounts doesn't exists..")
                        time.sleep(3.0)
                        continue

            # Update an Acccount Information.
            elif user_choice == 3:
                debit_account_number = int(input("Enter Account number: ").strip())
                flag, customer, code = search_account_info(
                    debit_account_number)  # type: ignore
                if flag is not False:  # acccount is found logic.
                    user_name = input("Enter username: ").strip()
                    gender = input("Enter Gender(M/F): ").strip()
                    address = input("Enter address: ").strip()
                    phone_number = input("Enter phone number: ").strip()
                    aadhar_number = input("Enter aadhar number: ").strip()
                    while True:
                        email = input("Enter E-Mail: ").strip()
                        if is_email(email) is False:
                            print("Entered invalid email!")
                            time.sleep(3.0)
                            continue
                        else:
                            break
                    data = {
                        "user_name": user_name,
                        "gender": gender,
                        "address": address,
                        "phone_number": phone_number,
                        "email": email,
                        "aadhar_number": aadhar_number,
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
                    print(
                        f"INFO: {debit_account_number} account is not found!\n updation failed!")
                    time.sleep(3.0)
                    continue

            # Delete an account
            elif user_choice == 4:
                account_number = int(input("Enter the account number: ").strip())
                upi_password = input("Enter upi_password: ").strip()
                remove_status, wrong_password = remove_account(
                    account_number, upi_password)  # type: ignore
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
                acc_num = int(input("Enter account number: ").strip())
                flag, customer, code = search_account_info(
                    acc_num)  # type: ignore
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
                    choice = input(
                        "\nTo go back to main menu press Y or N to exit the program: ").strip().capitalize()
                    if choice == "Y":
                        continue
                    elif choice == "N":
                        print("\nProgram terminated...")
                        break
                else:
                    print("No customers found!")
                    time.sleep(3.0)
            # View customer list
            elif user_choice == 6:
                customer_list = view_customer_list()
                print()
                for i, customer in enumerate(customer_list):  # type: ignore
                    print(str(i+1)+")", customer[0], "->", customer[1])
                choice = input(
                    "\nTo go back to main menu press Y or N to exit the program: ").strip().capitalize()
                if choice == "Y":
                    continue
                elif choice == "N":
                    print("\nProgram terminated...")
                    break
                else:
                    print("\nInvalid input!")
                    time.sleep(3.0)
                    continue
            elif user_choice == 7:  # exit the program
                print("\nProgram terminated...\n")
                break
            else:
                print("Invalid Choice...")
        except ValueError as e:
            print("Invalid input\nError message:", e)
            time.sleep(3.0)
        except IntegrityError as e:
            print("Already an account exists\nError message:", e)


if __name__ == "__main__":
    display_main()

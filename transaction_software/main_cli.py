"""
Main command line interface to interact with the user and the software. All the operations to be performed are listed and called the needed functions and methods to accomplish the tasks.
"""

import os

from utils.database import create_account

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
        user_choice = int(input("Please Enter your choice: "))
        if user_choice == 1: # Create Account.
            create_account()
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


if __name__ == "__main__":
    _display_main()

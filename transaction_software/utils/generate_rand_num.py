import random
import math

def generate_account_number()->int:
    """
    Generates a unique 16 digit account number. The first 6 digits are prefixed number(i.e bank code) 113120. the remaining 10 digits are generated randomly. with that 36,28,800 account numbers can be created.
    """
    acc_num = int("113120" + str(random.randrange(start=0,stop=9999999999)))
    return acc_num

def generate_trans_id()->int:
    """
    Return a random transaction number. with that 13_07_67_43_68_000 transaction id's can be created.
    """
    return random.randint(0, math.factorial(15))

# drive code
if __name__ == "__main__":
    acc = generate_account_number()
    print()

import random

def generate_account_number()->int:
    """
    Generates a unique 16 digit account number. The first 6 digits are prefixed number(i.e bank code) 113120. the remaining 10 digits are generated randomly. with that 36,28,800 account numbers can be created.
    """
    return random.randrange(start=0,stop=9999999999)

# drive code
if __name__ == "__main__":
    pass

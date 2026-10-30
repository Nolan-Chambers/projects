"""
Author: Amelie Chambers
Initiated: 10/29/2026
Finalized: hopefully soon

Random password generator that allows for a password of length >= 8 characters
to be made.
Options include having a combination of letters, numbers, and special chars,
but does not have to include all three.

Yay!
"""

import secrets, string, time


def main():
    print('Welcome to password generator!')
    time.sleep(0.4)
    password = read_length()
    password = ask_letters(password)
    password = ask_nums(password)
    password = ask_misc(password)
    print('Ta-da! Here is your password!'/n password)



class makePassword:

    def __init__(self):
        self.password = ""
        self.length = 8
        

    def setLength(self, length: int):
        self.length = length

    def getPassword(self):
        return self.password

    def addLetters(self, amount: int):
        """Adds desired amount of letters"""
        for i in range(amount):
            self.password += secrets.choice(string.ascii_letters())

    def addNums(self, amount: int):
        """Adds desired amount of numbers"""
        for i in range(amount):
            self.password += secrets.choice(string.digits())

    def addMisc(self, amount: int):
        """Adds desired amount of miscellaneous chars"""
        for i in range(amount):  
            self.password += secrets.choice(string.punctuation())


def read_length() -> str:
    """
    Reads user input for desired password length and initiates password.

    Args: None
    Returns: password, str
    """
    not_valid = True
    while not_valid:
        len_choice = input('How long should your password be? >> ').strip()
        if len_choice.isnumeric():
            password = password.makePassword(int(len_choice))
            not_valid = False
        else:
            print('Invalid entry. Please retry.')
            time.sleep(0.3)
            continue
    return password


def ask_letters(password: str) -> str:
    """
    Gathers user input on desired amount of letters and appends them to password.

    Args: password, str
    Returns: password, str
    """
    l_choice = input('Start by adding letters? [Y/N] >> ').strip().upper()
    if l_choice == 'Y':
        amount = int(input('How many? >> ').strip())
        return password.addLetters(amount)


def ask_nums(password: str) -> str:
    """
    Gathers user input on desired amount of numbers and appends them to password.
    
    Args: password, str
    Returns: password, str
    """
    n_choice = input('Add numbers? [Y/N] >> ').strip().upper()
    if n_choice == 'Y':
        amount = int(input('How many? >> ').strip())
        return password.addNums(amount)


def ask_misc(password: str) -> str:
    """
    Gathers user input on desired amount of miscellaneous characters and appends them to password.
    
    Args: password, str
    Returns: password, str
    """
    m_choice = input('Add special characters? [Y/N] >> ').strip().upper()
    if m_choice == 'Y':
        amount = int(input("How many? >> ").strip())
        return password.addMisc(amount)

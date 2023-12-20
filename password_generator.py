# Author: Sreelakshmi Odatt Venu
# Date Created: 19/12/2023

import string
import random

# defining a function random_password
def random_password():
    required_length = 12
    while True:
        # try - except block for checking whether the user entered the minimum value for the password length
        try:
            random_password = int(input("Enter the desired password length, not less than 12 characters: "))
            if random_password < required_length:
                print("Password length must be at least 12 characters.")
            else:
                break
        except ValueError as e:
            print(e)

    # prompting the user whether they want the upper case, lower case, etc. in their password
    lower_case = input("Would you like lower case values (y/n)? : ").lower() == "y"
    upper_case = input("Would you like upper case values (y/n)? : ").lower() == "y"
    integer_value = input("Would you like integer or numeric values (y/n)? : ").lower() == "y"
    characters = input("Would you like any characters or symbolic values (y/n)? : ").lower() == "y"
    
    password_values = ""
    password_values = password_values + "ABCDEFGHIJKLMNOPQRSTUVWXYZ" if upper_case else ""
    password_values = password_values +  "abcdefghijklmnopqrstuvwxyz" if lower_case else ""
    password_values = password_values +  "0123456789" if integer_value else ""
    password_values = password_values + string.punctuation if characters else ""


    if not password_values:
        print("Please accept one of the character types.")
        return None

    password = ''.join(random.choice(password_values) for _ in range(random_password))
    return password

if __name__ == "__main__":
    random_password = random_password()
    if random_password:
        print(" ")
        print("Here is the password:", random_password)







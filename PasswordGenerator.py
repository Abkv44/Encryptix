# -*- coding: utf-8 -*-

import random
import string
import sys

def generate_strong_password(length=16, allowed_chars=None):
    # Define a common set of allowed characters, excluding potentially restricted ones
    default_allowed_chars = string.ascii_letters + string.digits + "!@#$%&*"

    # Use provided allowed characters if specified
    if allowed_chars:
        char_pool = allowed_chars
    else:
        char_pool = default_allowed_chars

    # Ensure at least one character from each category (lowercase, uppercase, digits, symbols)
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice("!@#$%&*")
    ]
    password.extend(random.choice(char_pool) for _ in range(length - 4))

    # Shuffle the password for increased randomness
    random.shuffle(password)

    # Join the characters into a string
    return ''.join(password)

def generate_easy_password(length=4):
    return ''.join(random.choice(string.digits) for _ in range(length))

def generate_medium_password(length=6):
    allowed_chars = string.ascii_letters + string.digits

    # Ensure at least one uppercase, one lowercase, and one digit
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits)
    ]
    password.extend(random.choice(allowed_chars) for _ in range(length - 3))

    random.shuffle(password)
    return ''.join(password)


def generate_Ulength_password():
    length = int(input("Enter length(Minimum 4)\n"))
    if length < 4:
        print("length should be >= 4")
    else:
        print("your password:", generate_easy_password(length), "\nStrength - low")
        print("Your password:", generate_medium_password(length), "\nStrength - medium")
        print("Your password:", generate_strong_password(length), "\nStrength - strong")
    
def main():
    print("Enter Password strength: ")
    print("1. Easy to remember and short")
    print("2. Moderate strength")
    print("3. Strong password")
    print("4. Quit")
    print("5. For User defined length")

    try:
        user_choice = int(input("Choose (1-5): "))
        if user_choice == 1:
            print("Your Password:", generate_easy_password())
        elif user_choice == 2:
            print("Your Password:", generate_medium_password())
        elif user_choice == 3:
            print("Your Password:", generate_strong_password())
        elif user_choice == 4:
            sys.exit()
        elif user_choice == 5:
            generate_Ulength_password()
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 4.")



def ask():
    ask1 = "Generate password?\nEnter (y/n)"
    ask2 = "Generate password again?\nEnter (y/n)"
    count = 0
    while True:
        if count == 0:
            user = input(ask1)
        else:
            user = input(ask2)
        if user == "y":
            main()
        else:
            print("Thanks for your response!")
            break
        count=1
    
if __name__ == "__main__":
    ask()
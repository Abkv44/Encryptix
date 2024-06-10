# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 11:22:16 2024

@author: Abk
"""
def multiply(x, y):
    """Multiplies two numbers and prints the result."""
    result = x * y
    print(f"{x} x {y} = {result}")  # No rounding by default

def subtract(x, y):
    """Subtracts one number from another and prints the result."""
    result = x - y
    print(f"{x} - {y} = {result}")  # No rounding by default

def divide(x, y):
    """Divides one number by another and prints the result, handling division by zero."""
    if y == 0:
        print("Error: Division by zero!")
    else:
        result = x / y
        print(f"{x} ÷ {y} = {result}")

def add(x, y):
    """Adds two numbers and prints the result."""
    result = x + y
    print(f"{x} + {y} = {result}")  # No rounding by default

def Simple_calculator():
    """A simple calculator program that performs addition, subtraction, division, and multiplication."""

    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            break  # Exit loop if input is valid
        except ValueError:
            print("Invalid input! Please enter numbers.")

    print("1. Addition")
    print("2. Subtraction")
    print("3. Division(÷)")
    print("4. Multiplication(x)")

    while True:  # Loop for input validation (choice)
        try:
            choice = int(input("Choose operation (1-4): "))
            if 1 <= choice <= 4:
                break  # Exit loop if choice is valid
            else:
                print("Invalid choice! Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input! Please enter a number.")

    # Call the appropriate function based on user's choice
    match choice:
        case 1:
            add(num1, num2)
        case 2:
            subtract(num1, num2)
        case 3:
            divide(num1, num2)
        case 4:
            multiply(num1, num2)

if __name__ == "__main__":
    Simple_calculator()


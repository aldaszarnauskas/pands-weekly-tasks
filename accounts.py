#!/usr/bin/env python3

# Ask the user to enter an account number larger than 4 digits
# Conditions for the input: > than four digits and it contains only digits.
acc = input("Please enter an account number larger than 4 digits: ")

# Calculate how many digits are in the account number
acc_length = len(acc)

# Check if the input contains only digits
is_digit = acc.isdigit()

# Check if the user input complies with the conditions.
# Correspondigly, if it does not comply with conditions, print and explanation why it does not comply.
if (acc_length < 5) & (not is_digit): # Checks if > 5 values and contains only digits
    print("The account number has to be larger than 4 digits and it must contain only digits")
elif (acc_length < 5) & is_digit: # Checks if > 5 values
    print("The account number has to be larger than 4 digits")
elif (acc_length >= 5) & (not is_digit): # Checks if the input contains only digits
    print("The account number must contain only digits")
# The input complies with conditions 
else:
    # Calculates how many digits except the last four you have to convert to X
    x_length = acc_length - 4
    # Gets the last four digits
    last_four = acc[-4:]
    # prints the account number in xs, except the last four digits 
    print(f'{"X" * x_length}{last_four}')


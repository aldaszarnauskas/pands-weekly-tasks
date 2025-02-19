#!/bin/env python3

# Ask for the user input
val = input("Enter any positive integer: ")
# Convert the user input from a string to an integer
val = int(val)

# Define a collatz app
# Collatz app uses recursive programming

def collatz(val):
    # print(val) # Gives computation's history
    
    if val == 1:
        return 1

    # Check if the value is divisible by 2
    # if yes, divide by two and input back to the program
    if val % 2 == 0:
        return collatz(val / 2)
    
    # Otherwise, multiply val by 3 add 1 
    # And input back to the program
    else:
        return collatz(val*3 + 1)


print(collatz(val))

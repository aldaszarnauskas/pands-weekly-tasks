#!/bin/env python3

# Ask for the user input
val = input("Enter any positive integer: ")
# Convert the user input from a string to an integer
val = int(val)

# Define a collatz app

def collatz(val):
    history = val # Gives computation's history

    # Terminate the program when val = 1
    if val == 1:
        return history

    # Check if the value is divisible by 2
    # if yes, divide by two and input back to the program
    if val % 2 == 0:
        return collatz(val / 2)
    
    # Otherwise, multiply val by 3 and add 1 
    # And input back to the program
    else:
        return collatz(val*3 + 1)

collatz(val)

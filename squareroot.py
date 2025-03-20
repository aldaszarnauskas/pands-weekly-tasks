#!/bin/env python3

# Prompt a user to input a positive integer
aninput = input("Enter a positive number: ")
# Convert the input to a float
aninput = float(aninput)


# Th formula to calculate the square root: 
# root = 0.5 * (x + (aninput / x))
# x = aninput for aninput > 0, i.e. to solve x*x = aninput

# Define an x
x = aninput
# Define the # of counts for the while loop
count = 0

# Continue the while loop until either one of the conditions is False
while ((x * x != aninput) and (count < 1000)):
    # Perform calculations based on the formula above
    x = 0.5 * (x + (aninput/x))
    
    # Track the # of iterations of the while loop
    count += 1
    
# Print the square root of the input
print(f"The square root of {int(aninput)} is ≈ {round(x, 5)}.")

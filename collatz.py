# Prompt the user to give an integer
val = input("Enter any positive integer: ")


# Define a collatz program
# Collatz program takes integer as the input and performs computations.
# If the input is even, the program divides it by two,
# if it is odd, multiplies it by three and adds one.
# The program terminates when the value is one and outputs computations history
def collatz(val, history=[]):
    
    # Convert the val into integer
    # so that the output would have nice integer values.
    val = int(val)
    
    # Gather compution's history
    history = history + [val]
    
    
    # Terminate the program when val = 1
    if val == 1:
        return history

    # Check if the value is divisible by 2
    # if yes, divide by two and input back to the program
    if val % 2 == 0:
        return collatz(val / 2, history)
    
    # Otherwise, multiply val by 3 and add 1 
    # And input back to the program
    else:
        return collatz(val*3 + 1, history)


print(collatz(val))

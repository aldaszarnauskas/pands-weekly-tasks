# Prints an empty string to space out the output text
print("")
# Prompts the user to enter a numerical value
value1 = input("Enter amount 1(in cent): ")
print("")
# Prompts the user to enter a second numerical value
value2 = input("Enter amount 2(in cent): ")

# Converts users inputs to floats because
# input() converts inputs to a string
value1_fl = float(value1)
value2_fl = float(value2)

# Adds up both values
cents = value1_fl + value2_fl
# Divides by 100 and rounds to two decimal places
euros = round(cents / 100, 2) 

# Prints out the value in euros
print(f'''
The sum of these is €{euros} 
''')

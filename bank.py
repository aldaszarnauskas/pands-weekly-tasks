print("")
value1 = input("Enter amount1(in cent): ")
print("")
value2 = input("Enter amount2(in cent): ")

value1_fl = float(value1)
value2_fl = float(value2)

cents = value1_fl + value2_fl
euros = round(cents / 100, 2) 

print(f'''
The sum of these is €{euros} 
''')
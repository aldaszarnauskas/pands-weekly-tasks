#!/bin/env python3

aninput = input("Enter a positive number: ")
aninput = float(aninput)
# root = 0.5 * (X + (N / X))
# x = a for a > 0, i.e. to solve x2 = a
x = aninput
count = 0

while ((x * x != aninput) and (count < 1000)):
  x = 0.5 * (x + (aninput/x))
  count += 1
print(f"The square root of {aninput} is ≈ {round(x, 5)}.")

#!/usr/bin/env python3

from datetime import date
from datetime import datetime

# Import packahes
from datetime import date
from datetime import datetime

# Define the days of the weekday and weekend
weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekend = ["Saturday", "Sunday"]

# Obtain the day of the week that is ATM
dt = date.today()
day = dt.strftime("%A")

# Print if it is weekday or weekend
if day in weekday:
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is the weekend, yay!")

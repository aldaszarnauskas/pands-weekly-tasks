#!/bin/env python3

# sys helps to retrieve arguments given on a command line
import sys


# Assumptions:
# (1) one argument on a command line given
# (2) as a .txt file
# (3) and a text file is not empty


# (1) Check if only one argument was given on command line
if (len(sys.argv) == 1) & (len(sys.argv) >= 3):
    print("Please specify one text file")

# (2) Check if the argument is in a .txt format
elif sys.argv[1][-4:] != ".txt":
    print("Only text files are accepted")

else:
    # The file name is the second value in sys.argv object
    aninput = sys.argv[1]
    # Reads in the text file
    with open(aninput, "r") as file:
        # Stores a text file in the content object
        content = file.read().strip()

        # (3) Check if the text file is not empty, else exit()
        if len(content) == 0:
            print("Your text file is empty. Please be creative and add some text!")

        else:
            # Counts the # of es in the text file
            print(content.count("e"))


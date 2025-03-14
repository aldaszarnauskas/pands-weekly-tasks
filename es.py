#!/bin/env python3

#!/bin/env python3

import sys

# Assumptions: only .txt files given a string format, es.py accepts one argument (no less or more)
# sys.arg contains the arguments given on a command line
# Check if 1 argument is given
if len(sys.argv) == 1:
    print("Please specify a text file")
elif len(sys.argv) > 2:
    print("es.py takes in just one argument")



# Check if the argument is given in a string format
elif type(sys.argv[1]) != str:
    print("Only filenames in string format are accepted")

# Check if a text file is given
elif sys.argv[1][-4:] != ".txt":
    print("Only text files are accepted")

else:
    # The file name is the second value in sys.argv object
    aninput = sys.argv[1]
    # Reads in the text file
    with open(aninput, "r") as file:

        # Stores a text file in the content object
        content = file.read()
        # Counts the # of es in the text file
        print(content.count("e"))


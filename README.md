# Weekly Assignment Submissions for the Programming and Scripting
In this repository, you can find Aldas Zarnauskas weekly submissions for the Programming and Scripting module.
There are 8 submissions in total. 

## Explanation of each submission

### The begining of the World
1. helloworld.py prints "Hello World"

### Add two inputs
2. bank.py prompts the user to enter twice an amount in cents and outputs the sum of those two values expressed as euros.

### Convert the digits, except the last four, of your account number into Xs
3. accounts.py prints out an account number expressed as Xs, except the last four values.
The program firtsly prompts the user to enter an account number. The requirements for an account number are (1)it contains only digits and (2) it must be longer than 4 digits. Secondly, it checks if the input meets the requirements and outputs and alert message if it does not meet the requirements. Otherwise, it outputs the input as Xs, except the last four digits.

### Recursive programming, my head is still dizzy from the recursive loop
4. collatz.py program takes integer as the input and performs computations. If the input is even, the program divides it by two, if it is odd, multiplies it by three and adds one. The program terminates when the input is one and outputs computations history.
The program uses recursive programming principle where the program recursively transforms the input and inputs it back to the program until a certain condition is met. In this case, the program terminates when the input is equal to 1.

### What is  the day of the week?
5. weekday.py prints out a certain phrase depending if it's weekday or weekday when the program is run.

### Calculating a square root
6. squareroot.py calculates or approximates the square root of a given integer. The square root is calculated based on Newton's method: 
- root = 0.5 * (x + (aninput / x)); x = aninput for aninput > 0, i.e. to solve x*x = aninput.  
This formula is used iteratively approximate the square root where the output of calculations is placed back into the equation until an exact or a good approximation of a square root is obtained. We terminate such computation until an exact square root is obtained or until 1000 iterations have passed, thus, obtaining an approximation of a square root.


### How many Es do you have in your file?
7. es.py retrieves the # of e in a text file. This program is executable on the command line. The program has 3 assumptions to work: 
- (1) only one argument on a command line given 
- (2) the argument specifies directory of a .txt file
- (3) and a text file is not empty
If any of those assumptions are not met, the program gives a corresponding error message.
If all assumptions are met, the program counts the number of e in the text file and outputs the count.


### Lets Plot some math!
8. plottask.py plots  
- a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
- and a plot of the function  h(x)=x3 in the range 0 to 10, 
on one set of axes and saves the result as figure.png

# License
No license

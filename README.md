# Weekly Assignment Submissions for the Programming and Scripting
In this repository, you can find Aldas Zarnauskas weekly submissions for the Programming and Scripting module. 

## Explanation of each submission

### The begining of the World
1. helloworld.py prints "Hello World"

### A simple addition
2. bank.py prompts the user to enter twice an amount in cents and outputs the sum of those two values expressed as euros.

### How to make the account # incognito
3. accounts.py prints out an account number expressed as Xs, except the last four values.
The program firtsly prompts the user to enter an account number. The requirements for an account number are (1)it contains only digits and (2) it must be longer than 4 digits. Secondly, it checks if the input meets the requirements and outputs and alert message if it does not meet the requirements. Otherwise, it outputs the input as Xs, except the last four digits.

### Recursive programming, my head is still dizzy from the recursive loop
4. collatz.py program takes integer as the input and performs computations. If the input is even, the program divides it by two, if it is odd, multiplies it by three and adds one. The program terminates when the input is one and outputs computations history.
The program uses recursive programming principle where the program recursively transforms the input and inputs it back to the program until a certain condition is met. In this case, the program terminates when the input is equal to 1.

### What is  the day of the week?
5. weekday.py prints out a certain phrase depending if it's weekday or weekday when the program is run.

### Calculating a square root
6. squareroot.py takes integer as the input and outputs the square root of it or the approximation of the square root. The program uses Newton's method to calculate the square root which is: root = 0.5 * (x + (aninput / x)); x = aninput for aninput > 0, i.e. to solve x*x = aninput. This formula not necessarily gives the right answer on the first go. It iteratively performs calculations until x*x=aninput or it reaches the 1000 iterations. If x*x=aninput, then the program gives the exact square root. If the program terminates when it performs this calculations for 1000 iterations, then, the program gives the approximations of the square root.

### How many Es do you have in your file?
7. es.py should be activate on a command line. It takes a text file as the first and the only argument. The program also checks if arguments were given. It outputs an error message if: (1) no arguments were given, (2) more than one argument was given, (3) not a text file was given

# License
No license

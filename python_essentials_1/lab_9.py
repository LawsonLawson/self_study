'''
Scenario
The continue statement is used to skip the current block and move ahead to the
next iteration, without executing the statements inside the loop.

It can be used with both the while and for loops.

Your task here is very special: you must design a vowel eater! Write a program
that uses:

a for loop;
the concept of conditional execution (if-elif-else)
the continue statement.
Your program must:

ask the user to enter a word;
use user_word = user_word.upper() to convert the word entered by the user to
upper case; we'll talk about the so-called string methods and the upper()
method very soon - don't worry;
use conditional execution and the continue statement to "eat" the following
vowels A, E, I, O, U from the inputted word;
print the uneaten letters to the screen, each one of them on a separate line.
Test your program with the data we've provided for you.


Test data
Sample input: Gregory

Expected output:

G
R
G
R
Y
Sample input: abstemious

Expected output:

B
S
T
M
S
Sample input: IOUEA

Expected output:
'''
# store up the list of vowels
vowels = ['I', 'E', 'O', 'U', 'A']

# propmpt user for input
user_word = input("Input Sample: ").upper()

# iterate over the user_input
for letter in user_word:

    # check to see in a vowel is encountered, if yes, skip it
    if letter not in vowels:
        print(letter)  # print anything else apart from a vowel

'''
Or we could implement it this way :


user_input = input("Input Sample: ")
for letter in user_input:
    if letter == 'A' or letter == 'O' or letter == 'U' or letter == 'E' or \
            letter == 'I':
        continue
    else:
        print(letter)
'''

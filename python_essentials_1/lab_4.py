'''
Scenario
Spathiphyllum, more commonly known as a peace lily or white sail plant, is one
of the most popular indoor houseplants that filters out harmful toxins from
the air. Some of the toxins that it neutralizes include benzene, formaldehyde,
and ammonia.

Imagine that your computer program loves these plants. Whenever it receives
an input in the form of the word Spathiphyllum, it involuntarily shouts to the
console the following string: "Spathiphyllum is the best plant ever!"


Write a program that utilizes the concept of conditional execution, takes a
string as input, and:

prints the sentence "Yes - Spathiphyllum is the best plant ever!" to the screen
if the inputted string is "Spathiphyllum" (upper-case)
prints "No, I want a big Spathiphyllum!" if the inputted string is
"spathiphyllum" (lower-case)
prints "Spathiphyllum! Not [input]!" otherwise. Note: [input] is the string
taken as input.

Test your code using the data we've provided for you. And get yourself a
Spathiphyllum, too!


Test Data
Sample input: spathiphyllum

Expected output: No, I want a big Spathiphyllum!

Sample input: pelargonium

Expected output: Spathiphyllum! Not pelargonium!

Sample input: Spathiphyllum

Expected output: Yes - Spathiphyllum is the best plant ever!
'''
uppercase_input = "Spathiphyllum"
lowercase_input = "spathiphyllum"

_input = input("Sample input: ")

if _input == uppercase_input:
    print("Yes - {} is the best plan ever!".format(uppercase_input))
elif _input == lowercase_input:
    print("No, I want big {}!".format(uppercase_input))
else:
    if _input == "":
        print("Oh come on, you cannot enter an empty string")
    else:
        print("{}! Not {}!".format(uppercase_input, _input))

'''
Scenario
A junior magician has picked a secret number. He has hidden it in a variable
named secret_number. He wants everyone who run his program to play the Guess
the secret number game, and guess what number he has picked for them. Those who
don't guess the number will be stuck in an endless loop forever! Unfortunately,
he does not know how to complete the code.

Your task is to help the magician complete the code in the editor in such a way
so that the code:

will ask the user to enter an integer number;
will use a while loop;
will check whether the number entered by the user is the same as the number
picked by the magician. If the number chosen by the user is different than
the magician's secret number, the user should see the message "Ha ha! You're
stuck in my loop!" and be prompted to enter a number again. If the number
entered by the user matches the number picked by the magician, the number
should be printed to the screen, and the magician should say the following
words: "Well done, muggle! You are free now."
The magician is counting on you! Don't disappoint him.

Code in the editor :

secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
'''
secret_number = 777

print(
        """
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
try:
    while True:
        user_input = int(input("Guess the number: "))
        if user_input == secret_number:
            print("{}\nWell done, muggle! You are free now".format(user_input))
            exit()
        else:
            print("Ha ha! You're stuck in my loop!")
except ValueError:
    print("A secret number is what you are guessing, I not sure what you are\
 thinking ...")

'''
Test 5:
Write a Python program that:

Asks the user to input their age.
If the input is a valid integer, convert it and print a message stating the
user's age next year (increment by 1). If the input is not an integer
(e.g., a string or float), print a message indicating the input is invalid.
Example interaction:

plaintext
Copy code
Enter your age: 25
Next year, you will be 26.
'''
# prompt the user for their age
try:
    user_age = int(input("Enter your age: "))
    new_user_age = user_age + 1
    print(f"Next year, you will be {new_user_age}")
except ValueError:
    print("input is invalid")

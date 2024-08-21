'''
Test 2:
Write a Python function that accepts two integer values from a user, adds
them, and prints the result. Then, multiply the two values and print the
result, but the multiplication should be formatted as a decimal number with
two decimal places.

Example input:

plaintext
Copy code
Enter the first number: 3
Enter the second number: 5
Expected output:

plaintext
Copy code
The sum of 3 and 5 is 8
The product of 3 and 5 is 15.00
'''
first_number = int(input("Enter the first number: "))
second_number = int(input("Please enter the second number: "))

_sum = first_number + second_number
_product = float(first_number * second_number)

print("The sum of {} and {} is {}".format(first_number, second_number, _sum))
print("The product of {} and {} is {:.2f}".format(first_number, second_number,
      _product))

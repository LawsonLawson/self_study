'''
Test 6:
Write a program that accepts two numbers from the user
(they can be integers or floats). It should:

Calculate their sum, difference, and product.
Display the results in a formatted manner where each value is right-aligned in
a width of 10 spaces.
Example input:

plaintext
Copy code
Enter first number: 5
Enter second number: 2
Expected output:

plaintext
Copy code
Sum:              7
Difference:       3
Product:         10
'''
try:
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))

    _sum = first_number + second_number
    _difference = first_number - second_number
    _product = first_number * second_number

    print("Sum: {:>10}".format(_sum))
    print("Difference: {:>10}".format(_difference))
    print("Product: {:>10}".format(_product))
except ValueError:
    print("invalid input")

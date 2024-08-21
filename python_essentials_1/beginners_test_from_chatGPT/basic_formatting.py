'''
Test 1:
Write a Python program that prints the following sentence using string
formatting:

"Hello, my name is Alice, and I am 25 years old."

You should format the string using both:

f-strings
str.format()
'''
name = "Alice"
age = '25'
print(f'Hello, my name is {name},', 'and I am {} years old.'.format(age))

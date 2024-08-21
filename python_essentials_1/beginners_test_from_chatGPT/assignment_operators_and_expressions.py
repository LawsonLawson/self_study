'''
Test 4:
Given the following expression:

python
Copy code
x = 10
y = 4
z = x + y * 2 - y ** 2
What is the value of z? Explain why the value of z is what it is by breaking
down the order of operations.
'''
x = 10
y = 4
z = x + y * 2 - y ** 2
print(f"if x = 10 and y = 4, expression 'x + y * 2 - y ** 2' is {z} because\n")
print(f"\n In the order of precedence: (y ** 2) will get evaluated first\
 resulting in 16. So the expression now becomes 10(x) + 4(y) * 2 - 16. from\
 here, (4(y) * 2) will get evaluated next resulting in 8. so the expresssion\
 now becomes 10(x) +  8 - 16. 10 + 8 is 18 hence - 18 - 16 is 2")

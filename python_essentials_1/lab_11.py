'''
Scenario
In 1937, a German mathematician named Lothar Collatz formulated an intriguing
hypothesis (it still remains unproven) which can be described in the following
way:

take any non-negative and non-zero integer number and name it c0;
if it's even, evaluate a new c0 as c0 ÷ 2;
otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;
if c0 ≠ 1, skip to point 2.
The hypothesis says that regardless of the initial value of c0, it will always
go to 1.

Of course, it's an extremely complex task to use a computer in order to prove
the hypothesis for any natural number
(it may even require artificial intelligence), but you can use Python to check
some individual numbers. Maybe you'll even find the one which would disprove
the hypothesis.


Write a program which reads one natural number and executes the above steps as
long as c0 remains different from 1. We also want you to count the steps
needed to achieve the goal. Your code should output all the intermediate values
of c0, too.

Hint: the most important part of the problem is how to transform Collatz's idea
into a while loop - this is the key to success.

Test your code using the data we've provided.

Test Data

Sample input: 15

Expected output:

46
23
70
35
106
53
160
80
40
20
10
5
16
8
4
2
1
steps = 17
Sample input: 16

Expected output:

8
4
2
1
steps = 4
Sample input: 1023

Expected output:

3070
1535
4606
2303
6910
3455
10366
5183
15550
7775
23326
11663
34990
17495
52486
26243
78730
39365
118096
59048
29524
14762
7381
22144
11072
5536
2768
1384
692
346
173
520
260
130
65
196
98
49
148
74
37
112
56
28
14
7
22
11
34
17
52
26
13
40
20
10
5
16
8
4
2
1
steps = 62
'''
# for naming convention's sake, I am going to assume c0 as user_input
# we prompt the user for the input
try:
    user_input = int(input("Sample input: "))

    # should the user enter negative or zero interger, print error message
    # and exit
    if user_input <= 0:
        print("Please enter a non-negative or non-zero integer number")
        exit()

    # we keep track of the steps
    steps_taken = 0

    # we only execute this block so long as user_input isn't 1, once
    # it becomes 1, we stop
    while user_input != 1:

        # we check if the user_input is odd and handle it accordingly
        if user_input % 2 != 0:
            user_input = (3 * user_input) + 1
            steps_taken += 1
            print(int(user_input))

        # otherwise, it is even ...
        else:
            user_input /= 2
            steps_taken += 1
            print(int(user_input))
    print("steps = ", steps_taken)
except ValueError:
    print("Please enter a valid interger")

'''
Scenario
There once was a hat. The hat contained no rabbit, but a list of five numbers:
1, 2, 3, 4, and 5.

Your task is to:

write a line of code that prompts the user to replace the middle number in
the list with an integer number entered by the user (Step 1)
write a line of code that removes the last element from the list (Step 2)
write a line of code that prints the length of the existing list (Step 3).
'''
# step 1
hat = [1, 2, 3, 4, 5]

# print existing list
print("original list:\n {}".format(hat))
try:
    # prompt the user for a number
    user_input = int(input("Please enter a number: "))

    # replace the middle number with what the user entered
    hat[2] = user_input

    # print modified list
    print("list after the middle number was modified with user\
input: \n{}".format(hat))

# step 2

    # remove the last element from the list
    del hat[-1]

    # print modified list
    print("list after the last element was deleted:\n {}".format(hat))

# step 3

    # print the lenght of the existing list

    length_of_list = len(hat)

    print("Length of list: {}".format(length_of_list))
except ValueError:
    print("Enter a valid integer")

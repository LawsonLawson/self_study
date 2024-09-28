try:
    my_list = []
    for count in range(5):

        # prompt user for a list of numbers
        number = int(input("Please enter the numbers: "))
        my_list.append(number)
    total = 0
    for _count in my_list:
        total = total + _count
    print(total)

    # print(my_list)
except ValueError:
    print("Please enter a valid number")

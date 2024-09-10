try:
    my_list = []
    for count in range(1, 6):

        number = int(input(f"Enter number {count}: "))
        my_list.append(number)
        my_list.sort()
    for nums in my_list:
        print(nums)
except ValueError:
    print("Please enter a valid integer...")


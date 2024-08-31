user_input = input("Sample input: ").upper()

vowels = ['I', 'U', 'O', 'A' , 'E']
for letter in user_input:
    if letter == 'I' or letter == 'U' or letter == 'A' or letter == 'E' or letter == 'O':
        continue
    else:
        print(letter)

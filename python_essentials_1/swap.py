age = 55
house_number = 13

print(age, house_number)

auxilliary = age
age = house_number
house_number = age

print(age, house_number)

age, house_number = house_number, age

print(age, house_number)

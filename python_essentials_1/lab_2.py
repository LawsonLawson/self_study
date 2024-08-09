'''
This simple program converts miles to kilometers and vice versa
'''

# prompt user for the unit measure
measure = float(input(" >>> Enter measure: "))

# ask user what unit the measure they entered is
unit = input(" >>> Unit (K) for kilograms and (M) for miles: ")

# check for units and convert respectitvely

# for miles to kilometeres
if unit.upper() == "M":
    measure_in_kilometers = round((1.60934 * measure), 2)
    print("{} miles is {} kilometers".format(measure, measure_in_kilometers))


# for kilometers to miles
elif unit.upper() == "K":
    measure_in_miles = round((measure / 1.60934), 2)
    print("{} kilometers is {} miles".format(measure, measure_in_miles))

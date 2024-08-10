'''
Scenario
Your task is to prepare a simple code able to evaluate the end time of a period
of time, given as a number of minutes (it could be arbitrarily large). The
start time is given as a pair of hours (0..23) and minutes (0..59). The result
has to be printed to the console.

For example, if an event starts at 12:17 and lasts 59 minutes, it will end
at 13:16.

Don't worry about any imperfections in your code - it's okay if it accepts an
invalid time - the most important thing is that the code produce valid results
for valid input data.

Test your code carefully. Hint: using the % operator may be the key to success.

Test Data
Sample input:
12
17
59

Expected output: 13:16


Sample input:
23
58
642

Expected output: 10:40


Sample input:
0
1
2939

Expected output: 1:0
'''
# We prompt the user for the starting time
start_time_hour = int(input(" >>> Starting time (Hour mark): "))
start_time_minute = int(input(" >>> Starting time (Minute mark): "))

# We prompt the user for the duration
duration_time_hour = int(input(" >>> Duration time (Hour mark): "))
duration_time_minute = int(input(" >>> Duration time (Minute mark): "))

# Now we compute the ending time based on the start and duration time
end_time_hour = start_time_hour + duration_time_hour
end_time_minute = start_time_minute + duration_time_minute

# Handle minute overflow
if end_time_minute >= 60:
    end_time_minute = end_time_minute - 60
    end_time_hour = end_time_hour + 1

# Handle hour overflow (24-hour clock)
if end_time_hour >= 24:
    end_time_hour = end_time_hour - 24

print("If the function begins at {}:{} and last for a during of {}:{}, it will end at {}:{}".format(start_time_hour, start_time_minute, duration_time_hour, duration_time_minute, end_time_hour, end_time_minute))

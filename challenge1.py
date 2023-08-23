def time_converter():
    #checks if the last two characters of time string are equal to "am"
    if TIME_IN_12_HOUR_CLOCK_SYSTEM[-2:] == "am":
        #nested if checks if time is exactly equal to 12:00am
        if TIME_IN_12_HOUR_CLOCK_SYSTEM[:2] == "12":
            return "The time in the 24-hour clock system is 00:00hrs."
        else:
            return "The time in the 24-hour clock system is " + TIME_IN_12_HOUR_CLOCK_SYSTEM[:-2] + "hrs."
#checks if last two characters of time string are equal to pm
    elif TIME_IN_12_HOUR_CLOCK_SYSTEM[-2:] == "pm":
        if TIME_IN_12_HOUR_CLOCK_SYSTEM[:2] == "12":
            return "The time in the 24-hour clock system is 12:00hrs."
            #if previous is not met,this calculates time in 24hrs
        else:
            return "The time in the 24-hour clock system is " + str(12 + int(TIME_IN_12_HOUR_CLOCK_SYSTEM[:2])) + TIME_IN_12_HOUR_CLOCK_SYSTEM[2:-2] + "hrs."

    else:
        return "Try again."
#user input
TIME_IN_12_HOUR_CLOCK_SYSTEM = input("What is your time?")
#printing the result
print(time_converter())

def time_converter():
    if TIME_IN_12_HOUR_CLOCK_SYSTEM[-2:] == "am":
        if TIME_IN_12_HOUR_CLOCK_SYSTEM[:2] == "12":
            return "The time in the 24-hour clock system is 00:00hrs."
        else:
            return "The time in the 24-hour clock system is " + TIME_IN_12_HOUR_CLOCK_SYSTEM[:-2] + "hrs."

    elif TIME_IN_12_HOUR_CLOCK_SYSTEM[-2:] == "pm":
        if TIME_IN_12_HOUR_CLOCK_SYSTEM[:2] == "12":
            return "The time in the 24-hour clock system is 12:00hrs."
        else:
            return "The time in the 24-hour clock system is " + str(12 + int(TIME_IN_12_HOUR_CLOCK_SYSTEM[:2])) + TIME_IN_12_HOUR_CLOCK_SYSTEM[2:-2] + "hrs."

    else:
        return "Try again."

TIME_IN_12_HOUR_CLOCK_SYSTEM = input("What is your time?")
print(time_converter())

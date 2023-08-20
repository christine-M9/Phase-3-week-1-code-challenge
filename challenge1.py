def convert_to_24_hour(hour, minute, time):
    if time == "pm" and hour != 12:
        hour += 12
    elif time == "am" and hour == 12:
        hour = 0
        
    return f"{hour:02}{minute:02}"


print(convert_to_24_hour(12, 30, "am"))  # (place the time to be converted e.g (12, 30, "am")
print(convert_to_24_hour(12, 30, "pm"))  #(place the time to be converted e.g (12, 30, "pm")

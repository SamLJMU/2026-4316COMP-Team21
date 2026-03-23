# Converts string to military time
# Example: 10:30 PM -> 1350 (minutes)
def string_time_to_minutes(time: str) -> int:
    hour = int(time[:2])
    minute = int(time[3:5])
    meridiem = time[-2:]

    if(meridiem == "PM"):
        hour += 12
    
    return (hour * 60) + minute
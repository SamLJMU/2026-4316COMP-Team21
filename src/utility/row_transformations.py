# Convert string time (e.g. "4:30 AM", "10:30 PM") to minutes
def string_time_to_minutes(time: str) -> int:
    if not isinstance(time, str):
        return None

    try:
        time = time.strip()
        time_part, meridiem = time.split(" ")

        hour_str, minute_str = time_part.split(":")

        hour = int(hour_str)
        minute = int(minute_str)

        # Convert to 24-hour format
        if meridiem == "PM" and hour != 12:
            hour += 12
        elif meridiem == "AM" and hour == 12:
            hour = 0

        return hour * 60 + minute

    except Exception:
        return None  # fallback for bad data

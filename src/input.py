from utility.console_print import print_info, print_warning, print_success, clear_console
from classes.constants import ANSIColors, TimeframesEnum
from utility.general import get_year_min_and_max, get_min_and_max_dates, get_countries_list
from pandas import Period, to_datetime
from datetime import date

# Prompts user to enter an integer within range min and max inclusive
def input_integer(prompt, min, max) -> int:
    exit = False
    user_input = 0
    while not exit:
        user_input = input(ANSIColors.color_str(prompt, ANSIColors.BLUE))
        # try catch Integer only
        try: 
            user_input = int(user_input)
            if(user_input >= min and user_input <= max):
                exit = True
            else:
                print_warning(f"Only values between {min} and {max} inclusive are allowed")
        except ValueError as except_msg:
            print_warning("Only numerical integers are allowed as input. Please try again")
    return user_input

# Asks user whether they want to filter by country or not
def input_filter_by_country() -> int:
    print_info("Filter by country ?")
    options = ["No", "Yes"]

    for index, option in enumerate(options):
        print(f"{index}: {option}")

    choice = input_integer("Input: ", 0, len(options) - 1)
    return bool(choice)

# Prompts user to enter a country, if input is not within countries list reject it and prompt again
def input_country(prompt: str, err_msg: str) -> str:
    accepted_input = get_countries_list()
    exit = False
    user_input = ""
    while not exit:
        user_input = input(ANSIColors.color_str(prompt, ANSIColors.BLUE))
        user_input = user_input.upper()
        if(user_input in accepted_input):
            exit = True
        else:
            print_warning(err_msg)
    
    return user_input

def input_month(prompt: str, min=1, max=12) -> int:
    print_info(f"Month range available: {min} - {max}")
    return input_integer(prompt, min, max)

def input_year(prompt: str) -> int:
    min_date, max_date = get_min_and_max_dates()
    print_info(f"Year range available: {min_date.year} - {max_date.year}")
    return input_integer(prompt, min_date.year, max_date.year)

def input_full_date(prompt: str, comparison_date: date, lower_expected = False) -> date:
    user_input = None
    pd_date_format = "%d-%m-%Y"
    text_date_format = "DD-MM-YYYY"
    while True:
        user_input = input(ANSIColors.color_str(prompt, ANSIColors.BLUE)).strip()
        try:
            date_input = to_datetime(user_input, format=pd_date_format).date()

            if(date_input < comparison_date and lower_expected):
                print_warning(f"ERROR: date input should not be earlier than {comparison_date}.")
            elif(date_input > comparison_date and not lower_expected):
                print_warning(f"ERROR: date input should not be later than {comparison_date}.")
            else:
                return date_input
        except:
            print_warning(f"ERROR: input should be in format {text_date_format}")

# Returns a tuple consisting of the starting timestamp and ending timestamp
# Example output -> ("2025-01-01", "2025-12-31")
def input_timeframe(prompt: str) -> tuple:
    
    # Step 1. Input timeframe filter
    exit = False
    timeframe_input = None
    timeframe_values = set(item.value for item in TimeframesEnum)

    while not exit:
        try:
            # Print Options
            print("Timeframe available for filtering")
            for t in TimeframesEnum:
                print(f"{t.value}: {t.name}")

            # Get Input
            colored_prompt = ANSIColors.color_str(prompt, ANSIColors.BLUE)
            timeframe_input = input(colored_prompt)
            timeframe_input = int(timeframe_input)

            if(timeframe_input in timeframe_values):
                timeframe_input = TimeframesEnum(timeframe_input)
                exit = True
            else:
                print_warning(f"Invalid value enterred. Only {timeframe_values} are allowed.")
        except ValueError:
            print_warning("Only integers are allowed as input. Please try again")

    # Step 2. Get date data based on timeframe entered
    min_date, max_date = get_min_and_max_dates()

    match(timeframe_input):
        case TimeframesEnum.YEAR:
            year = input_year("Year: ")
            return (f"{year}-01-01",
                    f"{year}-12-31")
        
        case TimeframesEnum.MONTH:
            year = input_year("Year: ")

            # Get minimum and maximum dates for that year
            min, max = get_year_min_and_max(year)
            month = input_month("Month: ", min.month, max.month)

            # Get last day for that month (27-31)
            timestamp = Period(f"{year}-{month}", "M").end_time
            last_date = timestamp.day

            return (f"{year}-{month}-01",
                    f"{year}-{month}-{last_date}")
        
        case TimeframesEnum.FULL_DATE:
            while True:
                # validate start is not earlier than min, and similar for end
                start_date = input_full_date("Start Date: ", min_date, lower_expected=True)
                end_date = input_full_date("End Date: ", max_date, lower_expected=False)

                # validate start < end
                if(start_date > end_date):
                    print_warning("ERROR: Start date should be earlier than End Date.")
                else:
                    return (f"{start_date.year}-{start_date.month}-{start_date.day}",
                            f"{end_date.year}-{end_date.month}-{end_date.day}")

        case TimeframesEnum.NONE:
            return (f"{min_date.year}-{min_date.month}-{min_date.day}",
                    f"{max_date.year}-{max_date.month}-{max_date.day}")
        
        case _:
            raise Exception(f"Unhandled Timeframe Type: {timeframe_input}")    

def input_pollution_type(prompt: str) -> str:
    air_quality_column = "air_quality_"
    particle_types = ["PM2.5", "PM10"]

    print_info("Pollution Types available: ")
    for index, particle in enumerate(particle_types):
        print(f"{index}: {particle}")

    user_choice = input_integer(prompt, 0, len(particle_types) - 1)
    particle_chosen = particle_types[user_choice]

    return f"{air_quality_column}{particle_chosen}"
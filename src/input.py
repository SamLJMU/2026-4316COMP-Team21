from utility.console_print import print_info, print_warning, print_success, clear_console
from classes.constants import ANSIColors, TimeframesEnum
from pandas import Period

# Prompts user to enter an integer within range min and max inclusive
def getIntegerRange(prompt, min, max) -> int:
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

# Prompts user to enter a country, if input is not within accepted_input reject it and prompt again
def input_country(prompt: str, accepted_input: list, err_msg: str) -> str:
    exit = False
    user_input = ""
    while not exit:
        user_input = input(ANSIColors.color_str(prompt, ANSIColors.BLUE))
        user_input = user_input.capitalize()
        if(user_input in accepted_input):
            exit = True
        else:
            print_warning(err_msg)
    
    return user_input

def input_month(prompt: str) -> int:
    return getIntegerRange(prompt, 1, 12)

def input_year(prompt: str) -> int:
    # TODO Get min and max year from dataset instead of it being hardcoded
    return getIntegerRange(prompt, 2024, 2026)

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
    # TODO Handle month missing. i.e December 2026, January 2024, etc...
    match(timeframe_input):
        case TimeframesEnum.YEAR:
            year = input_year("Year: ")
            return (f"{year}-01-01",
                    f"{year}-12-31")
        
        case TimeframesEnum.MONTH:
            year = input_year("Year: ")
            month = input_month("Month: ")

            timestamp = Period(f"{year}-{month}", "M").end_time
            last_date = timestamp.day

            return (f"{year}-{month}-01",
                    f"{year}-{month}-{last_date}")
        
        case TimeframesEnum.FULL_DATE:
            raise NotImplementedError

        case TimeframesEnum.NONE:
            raise NotImplementedError
        
        case _:
            raise Exception(f"Unhandled Timeframe Type: {timeframe_input}")    

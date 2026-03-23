from utility.console_print import print_info, print_warning, print_success
from classes.constants import ANSI_Colors

# Prompts user to enter an integer within range min and max inclusive
def getIntegerRange(prompt, min, max) -> int:
    exit = False
    user_input = 0
    while not exit:
        user_input = input(ANSI_Colors.color_str(prompt, ANSI_Colors.BLUE))
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
def getCountryInput(prompt: str, accepted_input: list, err_msg: str) -> str:
    exit = False
    user_input = ""
    while not exit:
        user_input = input(ANSI_Colors.color_str(prompt, ANSI_Colors.BLUE))
        user_input = user_input.capitalize()
        if(user_input in accepted_input):
            exit = True
        else:
            print_warning(err_msg)
    
    return user_input

def getMonthInput(prompt: str) -> int:
    return getIntegerRange(prompt, 1, 12)
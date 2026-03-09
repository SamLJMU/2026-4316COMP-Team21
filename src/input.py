# Prompts user to enter an integer within range min and max inclusive
def getIntegerRange(prompt, min, max):
    exit = False
    user_input = ""
    while not exit:
        user_input = input(prompt)
        # try catch Integer only
        try: 
            user_input = int(user_input)
            if(user_input >= min and user_input <= max):
                exit = True
            else:
                print(f"Only values between {min} and {max} inclusive are allowed")
        except ValueError as except_msg:
                print("Only numerical integers are allowed as input. Please try again")
    return user_input
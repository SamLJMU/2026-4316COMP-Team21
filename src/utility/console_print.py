from classes.constants import ANSIColors
import os

# Print utility functions
def print_info(msg):
    print(f"{ANSIColors.BLUE}{msg}{ANSIColors.ENDC}")

def print_warning(msg):
    print(f"{ANSIColors.YELLOW}{msg}{ANSIColors.ENDC}")

def print_success(msg):
    print(f"{ANSIColors.GREEN}{msg}{ANSIColors.ENDC}")

# Clears console output
def clear_console():
    os.system("cls")
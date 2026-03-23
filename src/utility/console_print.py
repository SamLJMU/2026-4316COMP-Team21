from classes.constants import ANSI_Colors
import os

# Print utility functions
def print_info(msg):
    print(f"{ANSI_Colors.BLUE}{msg}{ANSI_Colors.ENDC}")

def print_warning(msg):
    print(f"{ANSI_Colors.YELLOW}{msg}{ANSI_Colors.ENDC}")

def print_success(msg):
    print(f"{ANSI_Colors.GREEN}{msg}{ANSI_Colors.ENDC}")

# Clears console output
def clear_console():
    os.system("cls")
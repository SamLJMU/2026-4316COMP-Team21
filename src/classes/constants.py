from enum import Enum

class ANSIColors:
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

    def color_str(str, color):
        return f"{color}{str}{ANSIColors.ENDC}"


class TimeframesEnum(Enum):
    NONE = 0
    YEAR = 1
    MONTH = 2
    FULL_DATE = 3

from enum import Enum

class MenuOptions:
    EXIT = 0
    DAYLIGHT_HOURS = 1
    AIR_QUALITY = 2
    AIR_QUALITY_BY_COUNTRY = 3
    AVG_TEMP_BY_COUNTRY = 4
    TEMP_TO_FEELS_LIKE = 5

class ANSIColors:
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    def color_str(str, color):
        return f"{color}{str}{ANSIColors.ENDC}"

class TimeframesEnum(Enum):
    NONE = 0
    YEAR = 1
    MONTH = 2
    FULL_DATE = 3
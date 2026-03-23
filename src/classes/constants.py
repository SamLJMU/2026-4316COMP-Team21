class MenuOptions:
    EXIT = 0
    DAYLIGHT_HOURS = 1
    AIR_QUALITY = 2
    AIR_QUALITY_BY_COUNTRY = 3
    AVG_TEMP_BY_TIMEZONE = 4
    AVG_TEMP_BY_COUNTRY = 5

class ANSI_Colors:
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    def color_str(str, color):
        return f"{color}{str}{ANSI_Colors.ENDC}"
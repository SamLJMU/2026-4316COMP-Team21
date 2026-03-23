from input import getIntegerRange
from classes.file_io import FileIO
from classes.constants import MenuOptions
from visualisations.matthieu.visualisation import air_quality_over_time
from visualisations.riccardo.visualisation_riccardo import daylight_hours
from classes.constants import ANSI_Colors
from utility.console_print import clear_console

def main():
    FileIO.read_file()
    display_main_menu()

def display_main_menu():
    
    running = True

    while running:

        menu_name = ANSI_Colors.color_str("-- Weather Menu --", ANSI_Colors.GREEN)
        print(menu_name)
        print(f"{MenuOptions.DAYLIGHT_HOURS}: Daylight Hours by Country over Time")
        print(f"{MenuOptions.AIR_QUALITY}: Air Quality by Country over Time")
        print(f"{MenuOptions.EXIT}: Exit")

        selectedIndex = getIntegerRange("Choose your option: ", 0, 4)

        match selectedIndex:

            case MenuOptions.DAYLIGHT_HOURS:
                daylight_hours()

            case MenuOptions.AIR_QUALITY:
                air_quality_over_time()

            case MenuOptions.EXIT:
                running = False
        
        # Clear console before next iteration and on exit
        clear_console()



main()
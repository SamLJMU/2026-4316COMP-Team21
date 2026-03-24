from input import getIntegerRange
from classes.file_io import FileIO
from classes.constants import MenuOptions
from visualisations.matthieu.visualisation import air_quality_over_time # might wanna update the name of this function to be more specific to the visualisation it creates
from visualisations.riccardo.visualisation_riccardo import daylight_hours
from visualisations.guinness.guinness_vis import air_quality_by_country_over_time
from visualisations.joseph.joseph_vis import avg_temp_by_country_over_time
from classes.constants import ANSIColors
from utility.console_print import clear_console

def main():
    FileIO.read_file()
    display_main_menu()

def display_main_menu():
    
    running = True

    while running:

        menu_name = ANSIColors.color_str("-- Weather Menu --", ANSIColors.GREEN)
        print(menu_name)
        print(f"{MenuOptions.DAYLIGHT_HOURS}: Daylight Hours by Country over Time")
        print(f"{MenuOptions.AIR_QUALITY}: Air Quality by Temperature over Time")
        print(f"{MenuOptions.AIR_QUALITY_BY_COUNTRY}: Air Quality by Country over Time")
        print(f"{MenuOptions.AVG_TEMP_BY_COUNTRY}: Average Temperature by Timezone over Time")
        print(f"{MenuOptions.EXIT}: Exit")

        selectedIndex = getIntegerRange("Choose your option: ", 0, 4)

        match selectedIndex:

            case MenuOptions.DAYLIGHT_HOURS:
                daylight_hours()

            case MenuOptions.AIR_QUALITY:
                air_quality_over_time()
                
            case MenuOptions.AIR_QUALITY_BY_COUNTRY:
                air_quality_by_country_over_time()

            case MenuOptions.AVG_TEMP_BY_COUNTRY:
                avg_temp_by_country_over_time()

            case MenuOptions.EXIT:
                running = False
        
        # Clear console before next iteration and on exit
        clear_console()



main()
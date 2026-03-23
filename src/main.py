from input import getIntegerRange
from classes.file_io import FileIO
from classes.constants import MenuOptions
from visualisations.matthieu.visualisation import air_quality_over_time # might wanna update the name of this function to be more specific to the visualisation it creates
from visualisations.riccardo.visualisation_riccardo import daylight_hours
from visualisations.guinness.guinness_vis import air_quality_by_country_over_time

def main():
    FileIO.read_file()
    # print(FileIO.dataset_df.dtypes)
    display_main_menu()

def display_main_menu():
    while True:
        print("+" + "-"*15 + "+")
        print("| Weather Menu: |")
        print("+" + "-"*15 + "+")
        print(f"\n{MenuOptions.DAYLIGHT_HOURS}: Daylight Hours by Country over Time")
        print(f"{MenuOptions.AIR_QUALITY}: Air Quality vs Temperature over Time")
        print(f"{MenuOptions.AIR_QUALITY_BY_COUNTRY}: Air Quality by Country over Time")
        # print("Option 4: [ADD LATER]") 
        print(f"\n{MenuOptions.EXIT}: Exit")

        selectedIndex = getIntegerRange("\nChoose your option: \n================== > ", 0, 3)

        match selectedIndex:

            case MenuOptions.DAYLIGHT_HOURS:
                daylight_hours()

            case MenuOptions.AIR_QUALITY:
                air_quality_over_time()
            
            case MenuOptions.AIR_QUALITY_BY_COUNTRY:
                air_quality_by_country_over_time()

            case MenuOptions.EXIT:
                print("Exiting program...")
                break


main()
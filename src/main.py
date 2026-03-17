from input import getIntegerRange
from classes.file_io import FileIO
from classes.constants import MenuOptions
from visualisations.matthieu.visualisation import air_quality_over_time
from visualisations.riccardo.visualisation_riccardo import daylight_hours

def main():
    FileIO.read_file()
    # print(FileIO.dataset_df.dtypes)
    display_main_menu()

def display_main_menu():
    
    print("Weather Menu:")
    print(f"{MenuOptions.DAYLIGHT_HOURS}: Daylight Hours by Country over Time")
    print(f"{MenuOptions.AIR_QUALITY}:  Air Quality by Country over Time")
    print("Option 3: [ADD LATER] ")

    selectedIndex = getIntegerRange("Choose your option: ", 1, 4)

    match selectedIndex:

        case MenuOptions.DAYLIGHT_HOURS:
            daylight_hours()

        case MenuOptions.AIR_QUALITY:
            air_quality_over_time()


main()
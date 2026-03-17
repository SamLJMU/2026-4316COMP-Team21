from input import getIntegerRange
from classes.file_io import FileIO
from classes.constants import Constants
from visualisations.matthieu.visualisation import air_quality_over_time
from visualisations.riccardo.visualisation_riccardo import daylight_hours

def main():
    FileIO.read_file()
    # print(FileIO.dataset_df.dtypes)
    display_main_menu()

def display_main_menu():
    
    print("Weather Menu:")
    print(f"{Constants.DAYLIGHT_HOURS}: Daylight Hours by Country over Time")
    print(f"{Constants.AIR_QUALITY}:  Air Quality by Country over Time")
    print("Option 3: [ADD LATER] ")

    selectedIndex = getIntegerRange("Choose your option: ", 1, 4)

    match selectedIndex:

        case Constants.DAYLIGHT_HOURS:
            daylight_hours()

        case Constants.AIR_QUALITY:
            air_quality_over_time()

        case Constants.PLACEHOLDER_3:
            print("3")

        case Constants.PLACEHOLDER_4:
            print("4")
    

main()
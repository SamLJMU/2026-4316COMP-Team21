from input import getIntegerRange
from classes.file_io import FileIO
from classes.constants import Constants
from visualisations.matthieu.visualisation import question_example
#from visualisations.riccardo.visualisation_riccardo import daylight_hours

def main():
    FileIO.read_file()
    print(FileIO.dataset_df.dtypes)
    #daylight_hours()
    question_example()
    display_main_menu()

def display_main_menu():
    
    print("Weather Menu:")
    print("Option 1: [ADD LATER] ")
    print("Option 2: [ADD LATER] ")
    print("Option 3: [ADD LATER] ")

    selectedIndex = getIntegerRange("Choose your option: ", 1, 4)

    match selectedIndex:

        case Constants.PLACEHOLDER_1:
            print("1")

        case Constants.PLACEHOLDER_2:
            print("2")

        case Constants.PLACEHOLDER_3:
            print("3")

        case Constants.PLACEHOLDER_4:
            print("4")
    

main()
from input import getIntegerRange

from classes.constants import Constants


def main():

    display_main_menu()

def display_main_menu():
    
    menu_option = ""

    while menu_option not in ["1","2","3",]:
        print("Weather Menu:")
        print("Option 1: [ADD LATER] ")
        print("Option 2: [ADD LATER] ")
        print("Option 3: [ADD LATER] ")
        menu_option = input("Choose your option: ")

        if menu_option not in ["1","2","3",]:
            print("Invalid choice - Type your option again: ")

    
    selectedIndex = getIntegerRange("", 1, 4)

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
from input import getIntegerRange
from constants import Constants

def main():
    displayMainMenu()

def displayMainMenu():

    print("Weather Menu")
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
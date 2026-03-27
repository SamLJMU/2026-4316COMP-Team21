from input import getIntegerRange
from classes.file_io import FileIO
from utility.console_print import clear_console, print_line
from classes.visualisations_manager import VisualisationManager

def main():
    FileIO.read_file()
    
    # Load singleton
    vis_manager = VisualisationManager()
    vis_manager.load()

    display_main_menu(vis_manager)

def display_main_menu(vis_manager: VisualisationManager):
    running = True

    while running:

        vis_manager.displayOptions()

        selectedIndex = getIntegerRange("Choose your option: ", vis_manager.min_option, vis_manager.max_option)
        if selectedIndex == vis_manager.min_option:
            clear_console()
            break

        vis_manager.callChosenOption(selectedIndex)
        
        # Clear console before next iteration
        clear_console()



main()
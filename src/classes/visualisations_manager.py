import json
from classes.visualisation import Visualisation
from function_mapping import function_map
from classes.constants import ANSIColors
from utility.console_print import print_line, print_error

class VisualisationManager(object):
    _instance = None
    __EXIT_VALUE__ = 0

    # Singleton
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(VisualisationManager, cls).__new__(cls)
            # Initialisation
            cls._instance._visualisations = {}
            cls._instance._min_option = cls.__EXIT_VALUE__
            cls._instance._max_option = cls.__EXIT_VALUE__
        
        return cls._instance

    def load(self):
        with open('visualisation_config.json') as f:
            json_visualisations = json.load(f)
            assert(type(json_visualisations) is list)

            start_index = self.min_option + 1
            for idx, v in enumerate(json_visualisations, start_index):

                # Error checking
                if v['key'] not in function_map:
                    print_error(f"No mapping for '{v['key']}' in function_map, ensure keys match in visualisation_config.json and function_mapping.py")
                    raise KeyError(f"No function mapped to this key in function_mapping.py. Key: `{v['key']}`")

                visualisation_obj = Visualisation(v['msg'], function_map[v['key']])
                self._visualisations[idx] = (visualisation_obj)
                self._max_option = idx
            
            self._visualisations[self.min_option] = Visualisation("Exit", lambda: ())

    def displayOptions(self):
        menu_name = ANSIColors.color_str("-- Weather Menu --", ANSIColors.GREEN)
        print(menu_name)
        for key, value in self._visualisations.items():
            print(f"{key}: {value.message}")

        print_line()

    def callChosenOption(self, key):
        self._visualisations[key].run()

    @property
    def min_option(self):
        return self._min_option
    
    @property
    def max_option(self):
        return self._max_option
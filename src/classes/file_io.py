import pandas as pd
from utility.row_transformations import string_time_to_minutes
from utility.console_print import print_info, print_success, clear_console


class FileIO:
    # Private dataset static variable can either be None or a DataFrame object
    dataset_df: None | pd.DataFrame = None

    @classmethod
    def read_file(cls):
        # Allows time periods to be passed to plotting functions
        pd.plotting.register_matplotlib_converters()

        # Loads dataset
        print_info("Loading Dataset...")
        cls.dataset_df = pd.read_csv("dataset/GlobalWeatherRepository.csv")
        print_success("Dataset Loaded.")

        print_info("Processing Dataset...")
        cls.dataset_df["last_updated_date_time"] = pd.to_datetime(cls.dataset_df["last_updated_epoch"], unit='s')
        cls.dataset_df["sunrise_time"] = cls.dataset_df["sunrise"].apply(string_time_to_minutes)
        cls.dataset_df["sunset_time"] = cls.dataset_df["sunset"].apply(string_time_to_minutes)
        cls.dataset_df["country"] = cls.dataset_df["country"].apply(str.upper)
        print_success("Dataset Processed.")
        clear_console()

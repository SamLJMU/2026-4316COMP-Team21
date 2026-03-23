import pandas as pd
from utility.row_transformations import string_time_to_minutes

class FileIO:
    # Private dataset static variable can either be None or a DataFrame object
    dataset_df: None | pd.DataFrame = None

    def read_file():
        # Allows time periods to be passed to plotting functions
        pd.plotting.register_matplotlib_converters()

        # Loads dataset
        FileIO.dataset_df = pd.read_csv("dataset/GlobalWeatherRepository.csv")
        FileIO.dataset_df["last_updated_date_time"] = pd.to_datetime(FileIO.dataset_df["last_updated_epoch"], unit='s')
        FileIO.dataset_df["sunrise_time"] = FileIO.dataset_df["sunrise"].apply(string_time_to_minutes)
        FileIO.dataset_df["sunset_time"] = FileIO.dataset_df["sunset"].apply(string_time_to_minutes)
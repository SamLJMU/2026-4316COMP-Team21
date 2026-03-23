import pandas as pd
from utility.row_transformations import string_time_to_minutes

class FileIO:
    
    dataset_df: None | pd.DataFrame = None

    def read_file():
        FileIO.dataset_df = pd.read_csv(
            "dataset/GlobalWeatherRepository.csv",
            skipinitialspace=True
        )
        FileIO.dataset_df.columns = FileIO.dataset_df.columns.str.strip()
        FileIO.dataset_df["last_updated_date_time"] = pd.to_datetime(
            FileIO.dataset_df["last_updated_epoch"], unit='s'
        )
        FileIO.dataset_df["sunrise_time"] = FileIO.dataset_df["sunrise"].apply(string_time_to_minutes)
        FileIO.dataset_df["sunset_time"] = FileIO.dataset_df["sunset"].apply(string_time_to_minutes)
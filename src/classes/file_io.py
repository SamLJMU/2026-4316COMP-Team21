import pandas as pd

class FileIO:
    # Private dataset static variable can either be None or a DataFrame object
    dataset_df: None | pd.DataFrame = None

    def read_file():
        FileIO.dataset_df = pd.read_csv("dataset/GlobalWeatherRepository.csv")
from classes.file_io import FileIO
from utility.console_print import print_warning
from datetime import date


# Return tuple of minimum date and maximum date from dataset for a specific year
def get_year_min_and_max(year: int) -> tuple[date, date]:

    date_col = "last_updated_date_time"
    df = FileIO.dataset_df[[date_col]]
    df = df.loc[
        (df[date_col] >= f"{year}-01-01") & (df[date_col] < f"{year + 1}-01-01")
    ]
    return (df[date_col].min().date(), df[date_col].max().date())


# Return tuple of minimum and maximum date in dataset
def get_min_and_max_dates() -> tuple[date, date]:
    date_col = "last_updated_date_time"
    df = FileIO.dataset_df[[date_col]]
    return (df[date_col].min().date(), df[date_col].max().date())

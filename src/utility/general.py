from classes.file_io import FileIO
from utility.console_print import print_warning

# Returns tuple of minimum date and maximum date from dataset for a specific year
def get_year_min_and_max(year: int) -> tuple:
    print_warning("WARNING: Developer Testing required for data on year-01-01 at midnight, same for 31 dec at 11:59!")

    date_col = "last_updated_date_time"
    df = FileIO.dataset_df[[date_col]]
    df = df.loc[(df[date_col] >= f"{year}-01-01") & (df[date_col] < f"{year + 1}-01-01")]
    return (df[date_col].min(), df[date_col].max())
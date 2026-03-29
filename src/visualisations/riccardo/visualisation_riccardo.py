from classes.file_io import FileIO
from utility.row_transformations import string_time_to_minutes
import matplotlib.pyplot as mpl
from matplotlib.ticker import FuncFormatter
import matplotlib.dates as mdates
import pandas as pd
import matplotlib.ticker as ticker
from input import input_country

def minutes_to_military(total_minutes, tick_number):
    hours = int(total_minutes // 60)
    minutes = int(total_minutes % 60)
    return f"{hours:02d}:{minutes:02d}"

def daylight_hours():
    # Get dataset
    df = FileIO.dataset_df[["country", "last_updated", "sunrise", "sunset"]]

    # prompt user for name of country (filter), validate input
    # print("Filter")
    # TODO
    country = input_country()

    # process data per name of country (filter)
    # TODO
    filtered_df = df[df["country"] == country]
    filtered_df["last_updated"] = pd.to_datetime(filtered_df["last_updated"])
    filtered_df = filtered_df.loc[(filtered_df["last_updated"] > "2025-1-1")]
    filtered_df = filtered_df[filtered_df["last_updated"].dt.day == 1]

    daylight_minutes_list = []
    dates = []

    for _, row in filtered_df.iterrows():                             #ask matthieu
        sunset_minutes = string_time_to_minutes(row["sunset"])
        sunrise_minutes = string_time_to_minutes(row["sunrise"])
        
        daylight_minutes = sunset_minutes - sunrise_minutes    #TODO convert to military time to display in labels#
        
        daylight_minutes_list.append(daylight_minutes)
        dates.append(row["last_updated"])
        
    print(dates)

    # Ask for sorting
    # TODO

    # Ask for sort order
    print("Sort Order")
    # TODO

    # Sort data
    # TODO df.sort_values()

    # Visualise via matplotlib
    # TODO filter or group data, else visualization will slow program
    fig, ax = mpl.subplots()
    ax.plot(dates, daylight_minutes_list)

    ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))
    ax.yaxis.set_major_formatter(mpl.FuncFormatter(minutes_to_military))
    
    ax.set_xlabel("Date")
    ax.set_ylabel("Daylight Hours")
    ax.set_title(f"Daylight Hours in {country}")

    mpl.xticks(dates, rotation=45)
    mpl.show()
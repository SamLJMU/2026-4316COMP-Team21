from classes.file_io import FileIO
import matplotlib.pyplot as mpl
import pandas as pd
from input import input_country, input_timeframe

def air_quality_over_time():
    # Get dataset
    df = FileIO.dataset_df[["country", "last_updated_date_time", "air_quality_PM2.5"]]

    # Filter Input
    country = input_country("Enter a country name: ", df["country"].to_list(), "Country not found. Try again")
    timeframe = input_timeframe("Desired timeframe filter: ")
    print(timeframe[1])

    # Process data per filter
    df = df[df["country"] == country]
    df = df.loc[(df["last_updated_date_time"] >= timeframe[0]) & (df["last_updated_date_time"] <= timeframe[1])]

    # print(df.head)

    # period = df.last_updated_date_time.dt.to_period("M")
    # s = df.groupby(period)["air_quality_PM2.5"].mean()

    # Converts series to dataframe
    # df = s.to_frame()

    # Converts PeriodIndex to DateTimeIndex, for plotting conversion
    # df.index = df.index.to_timestamp()

    # Ask for sorting
    # TODO

    # Ask for sort order
    # TODO

    # Sort data
    # TODO df.sort_values()

    # Visualise via matplotlib
    fig, ax = mpl.subplots()
    # ax.plot(df.index, df["air_quality_PM2.5"])
    ax.plot(df["last_updated_date_time"], df["air_quality_PM2.5"])
    mpl.show()
from classes.file_io import FileIO
import matplotlib.pyplot as mpl
import pandas as pd

def air_pressure_and_percipitation():
    # Get dataset
    df = FileIO.dataset_df[["country", "last_updated_date_time", "pressure_in", "precip_mmW"]]

    # Filter Input
    country = getCountryInput("Enter a country name: ", df["country"].to_list(), "Country not found. Try again")

    # Process data per filter
    df = df[df["country"] == country]
    df = df.loc[(df["last_updated_date_time"] >= "2024-01-01")]

    period = df.last_updated_date_time.dt.to_period("M")
    s = df.groupby(period)["pressure_in"].mean()

    # Converts series to dataframe
    df = s.to_frame()

    # Converts PeriodIndex to DateTimeIndex, for plotting conversion
    df.index = df.index.to_timestamp()

    # Ask for sorting
    # TODO

    # Ask for sort order
    # TODO

    # Sort data
    # TODO df.sort_values()

    # Visualise via matplotlib
    fig, ax = mpl.subplots()
    ax.plot(df.index, df["air_quality_PM2.5"])
    mpl.show()
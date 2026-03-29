from classes.file_io import FileIO
import matplotlib.pyplot as mpl
import pandas as pd
from input import input_country, input_timeframe


def temperature_celsius_to_feels_like_celsius():
    # Filter Input
    df = FileIO.dataset_df[
        [
            "temperature_celsius",
            "feels_like_celsius",
            "last_updated_date_time",
            "country",
        ]
    ]
    # Get country from user
    country = input_country()
    timeframe = input_timeframe("Desired timeframe: ")
    # Process data per filter
    df = df[df["country"] == country]
    df["last_updated_date_time"] = pd.to_datetime(df["last_updated_date_time"])
    df = df.loc[(df["last_updated_date_time"] >= timeframe[0]) & (df["last_updated_date_time"] <= timeframe[1])]

    # Visualise via matplotlib
    fig, ax = mpl.subplots()
    ax.plot(df["last_updated_date_time"], df["temperature_celsius"], label="Temperature")
    ax.plot(df["last_updated_date_time"], df["feels_like_celsius"], label="Feels Like")
    ax.legend()
    mpl.show()

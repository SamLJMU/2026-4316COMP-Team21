from classes.file_io import FileIO
import matplotlib.pyplot as mpl
import pandas as pd
from input import input_country, input_timeframe


def Wind_mph_to_gust_mph():
    # Filter Input
    df = FileIO.dataset_df[
        ["wind_mph", "gust_mph", "last_updated_date_time", "country"]
    ]

    # Get country from user
    country = input_country()
    timeframe = input_timeframe("Desired timeframe:")

    # Process data per filter
    df = df[df["country"] == country]
    df["last_updated_date_time"] = pd.to_datetime(df["last_updated_date_time"])
    df = df.loc[(df["last_updated_date_time"] >= timeframe[0]) & (df["last_updated_date_time"] <= timeframe[1])]

    # Visualise via matplotlib
    fig, ax = mpl.subplots()
    ax.plot(df["last_updated_date_time"], df["wind_mph"], label="Wind Speed")
    ax.plot(df["last_updated_date_time"], df["gust_mph"], label="Gust")
    ax.legend()
    mpl.show()

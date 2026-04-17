from classes.file_io import FileIO
import matplotlib.pyplot as mpl
import pandas as pd
from input import input_country


def Wind_mph_to_gust_mph():
    # Filter Input
    df = FileIO.dataset_df[["wind_mph", "gust_mph", "last_updated_date_time", "country"]]
    # Filter Input
    country = input_country(
        "Enter a country name: ",
        "Country not found. Try again",
    )

    # Process data per filter
    df = df[df["country"] == country]
    df = df.loc[(df["last_updated_date_time"] >= "2024-01-01")] #revert

    # Visualise via matplotlib
    fig, ax = mpl.subplots()
    ax.plot(df["last_updated_date_time"], df["wind_mph"], label="Wind Speed")
    ax.plot(df["last_updated_date_time"], df["gust_mph"], label="Gust")
    ax.legend()
    

    mpl.show()

from classes.file_io import FileIO
import matplotlib.pyplot as mpl
import pandas as pd
from input import input_country


def Wind_mph_to_gust_mph():
    # Filter Input
    df = FileIO.dataset_df[["wind_mph", "gust_mph", "last_updated ", "country"]]
    # Filter Input
    country = input_country(
        "Enter a country name: ",
        "Country not found. Try again",
    )

    # Process data per filter
    df = df[df["country"] == country]
    df = df.loc[(df["last_updated"] >= "2024-01-01")]

    # Visualise via matplotlib
    fig, ax = mpl.subplots()
    ax.plot(df["last_updated"], df["wind_mph"], label="Wind Speed")
    ax.plot(df["last_updated"], df["gust_mph"], label="Gust")
    ax.legend()
    
    mpl.show()

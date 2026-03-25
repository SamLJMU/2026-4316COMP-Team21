from classes.file_io import FileIO
import matplotlib.pyplot as mpl
import pandas as pd
from input import input_country


def temperature_celsius_to_feels_like_celsius():
    # Filter Input
    df = FileIO.dataset_df[
        ["temperature_celsius", "feels_like_celsius", "last_updated ", "country"]
    ]
    # Filter Input
    country = input_country(
        "Enter a country name: ",
        "Country not found. Try again",)

    # Process data per filter
    df = df[df["country"] == country]
    df = df.loc[(df["last_updated"] >= "2024-01-01")]

    # Visualise via matplotlib
    fig, ax = mpl.subplots()
    ax.plot(df["last_updated"], df["temperature_celsius"], label="Temperature")
    ax.plot(df["last_updated"], df["feels_like_celsius"], label="Feels Like")
    ax.legend()
    mpl.show()

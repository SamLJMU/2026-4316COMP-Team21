import pandas as pd
import matplotlib.pyplot as plt
from classes.file_io import FileIO
from input import input_country, input_timeframe


def humidity_vs_cloud_over_time():
    # Import relevant dataset columns
    df = FileIO.dataset_df[["cloud", "humidity", "last_updated_date_time", "country"]]

    # Get user filter inputs
    country = input_country()
    timeframe = input_timeframe("Filter by timeframe: ")

    # Filter data by country
    df = df[df["country"] == country].copy()

    # Filter data by timeframe
    df["last_updated_date_time"] = pd.to_datetime(df["last_updated_date_time"])
    timeframe_start, timeframe_end = pd.to_datetime(timeframe[0]), pd.to_datetime(
        timeframe[1]
    )
    df = df.loc[
        (df["last_updated_date_time"] >= timeframe_start)
        & (df["last_updated_date_time"] <= timeframe_end)
    ]

    # If more than 3 months, ask user if to show data monthly instead
    timescale = "Daily"
    days_diff = (timeframe_end - timeframe_start).days
    if days_diff > 90:
        user_choice = input(
            f"Your chosen timeframe is {days_diff} days. Would you like to view monthly averages instead of daily? (Y/N): "
        ).upper()
        if user_choice in ["Y", "YES"]:
            df = (
                df.set_index("last_updated_date_time")
                .resample("ME")
                .mean(numeric_only=True)
                .reset_index()
            )
        timescale = "Monthly"

    # Graph visualistaion
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.plot(
        df["last_updated_date_time"], df["cloud"], label="Cloud Coverage", marker="o"
    )
    ax.plot(df["last_updated_date_time"], df["humidity"], label="Humidity", marker="o")

    ax.set_xlabel("Date")
    ax.xaxis.grid(True)
    ax.set_ylabel("%")
    ax.yaxis.grid(True)

    ax.set_title(f"{timescale} Humidity vs. Cloud Coverage in {country}")
    ax.legend()
    fig.autofmt_xdate()
    plt.tight_layout()
    plt.show()

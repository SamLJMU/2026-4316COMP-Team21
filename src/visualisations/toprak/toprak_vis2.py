import pandas as pd
import matplotlib.pyplot as plt
from classes.file_io import FileIO
from input import input_country, input_timeframe


def cloud_vs_feels_like_temp_over_time():
    # Import relevant dataset columns
    df = FileIO.dataset_df[
        [
            "cloud",
            "feels_like_celsius",
            "feels_like_fahrenheit",
            "last_updated_date_time",
            "country",
        ]
    ]

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
        if user_choice not in ["N", "NO"]:
            if user_choice not in ["Y", "YES"]:
                print(
                    "Input not recognised. Going with the recommended option of monthly."
                )
            df = (
                df.set_index("last_updated_date_time")
                .resample("ME")
                .mean(numeric_only=True)
                .reset_index()
            )
            timescale = "Monthly"

    # Unit user choice
    unit_choice = input(f"Would you prefer Celsius or Fahrenheit? (C/F): ").upper()

    # Graph visualistaion
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.plot(
        df["last_updated_date_time"],
        df["cloud"],
        label="Cloud Coverage (%)",
        marker="o",
    )

    if unit_choice not in ["F", "FAHRENHEIT"]:
        if unit_choice not in ["C", "CELSIUS"]:
            print("Input not recognised. Going with the recommended option of Celsius.")
        ax.plot(
            df["last_updated_date_time"],
            df["feels_like_celsius"],
            label="Feels-Like Temperature (°C)",
            marker="o",
        )
    else:
        ax.plot(
            df["last_updated_date_time"],
            df["feels_like_fahrenheit"],
            label="Feels-Like Temperature (°F)",
            marker="o",
        )

    ax.set_xlabel("Date")
    ax.xaxis.grid(True)
    ax.yaxis.grid(True)

    ax.set_title(f"{timescale} Cloud Coverage vs. Feels Like Temperature in {country}")
    ax.legend()
    fig.autofmt_xdate()
    plt.tight_layout()
    plt.show()

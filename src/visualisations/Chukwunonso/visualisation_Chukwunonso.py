from classes.file_io import FileIO
import matplotlib.pyplot as mpl
import pandas as pd
from input import input_country


def input_country():
    all_countries = sorted(FileIO.dataset_df["country"].unique().tolist())

    while True:
        print("\nAvailable countries:")
        for country in all_countries:
            print(f"  - {country}")

        user_input = input("Enter a country name: ").strip()

        matches = [c for c in all_countries if user_input.lower() in c.lower()]

        if len(matches) == 1:
            print(f"Selected: {matches[0]}")
            return matches[0]

        elif len(matches) > 1:
            print(f"\nDid you mean one of these?")
            for country in matches:
                print(f"  - {country}")
            user_input = input("Enter a country name: ").strip()

            exact = [c for c in matches if c.lower() == user_input.lower()]
            if exact:
                print(f"Selected: {exact[0]}")
                return exact[0]

        else:
            print("Country not found. Try again")


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
    
    # Process data per filter
    df = df[df["country"] == country]
    df = df.loc[(df["last_updated_date_time"] >= "2024-01-01")]

    # Visualise via matplotlib
    fig, ax = mpl.subplots()
    ax.plot(
        df["last_updated_date_time"], df["temperature_celsius"], label="Temperature"
    )
    ax.plot(df["last_updated_date_time"], df["feels_like_celsius"], label="Feels Like")
    ax.legend()
    mpl.show()

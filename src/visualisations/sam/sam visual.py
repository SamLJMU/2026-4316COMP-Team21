from classes.file_io import FileIO
import matplotlib.pyplot as mpl
import pandas as pd
from input import input_country

def air_pressure_and_percipitation():
    # Get dataset
    df = FileIO.dataset_df[["country", "last_updated_date_time", "pressure_in", "precip_mmW"]]

    # Filter Input
    def input_country():
     all_countries = sorted(FileIO.dataset_df["country"].unique().tolist())

     while True:
        print("For a list of countries press 1 or input the country name straight away instead")
        if user_input("1"):
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
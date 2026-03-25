# Wind Speed over x time for y country
from classes.file_io import FileIO
import pandas as pd
import matplotlib.pyplot as plt
import os


def plot_wind_speed(dataset, targetCountry):
    # Checks whether the target country and the dataset country is the same, and then the rows that pass the filter
    # create a new table that is stored in here
    countryData = dataset[dataset['country'].str.lower() == targetCountry.lower()].copy()

    if countryData.empty:
        print("Error: There is no data found for " + targetCountry)
        return
    
    countryData = countryData.sort_values(by='last_updated_date_time')
    
    fig, ax = plt.subplots(figsize=(10, 5))
    
    ax.plot(
        countryData['last_updated_date_time'],
        countryData['wind_kph'],
        marker='o',
        linestyle='-',
        color="#8b0e0e",
        label=f"{targetCountry.title()} Wind Speed"
    )

    ax.set_title(f"Wind Speed Over Time: {targetCountry.title()}", fontsize=14, pad=15)
    ax.set_xlabel("Date", fontsize=12)
    ax.set_ylabel("Wind Speed (km/h)", fontsize=12)

    ax.xaxis.grid(True, linestyle='--', alpha=0.7)
    ax.yaxis.grid(True, linestyle='--', alpha=0.7)
    plt.xticks(rotation=45)
    ax.legend()
    
    plt.tight_layout()
    plt.show()


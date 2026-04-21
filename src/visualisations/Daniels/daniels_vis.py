# Wind Speed over x time for y country
from input import input_country, input_timeframe
from classes.file_io import FileIO
from utility.console_print import print_warning
import pandas as pd
import matplotlib.pyplot as plt
import os

# Function to prompt the user for data such as number of countries and what countries
def userdata_wind_speed():
    dataset = FileIO.dataset_df

    if dataset is None:
        print("Error: Dataset couldn't be loaded/found")
        return
    
    print("\n Wind Speed over Time (per country) \n ")
    
    # Keep asking for dates until there the filtered dataset isn't empty
    while True:
        start_date, end_date = input_timeframe("Select a timeframe for the graph: ")
        start_dt = pd.to_datetime(start_date) 
        end_dt = pd.to_datetime(end_date)

        # Filters the whole database to just these dates
        date_filtered_dataset = dataset[
            (dataset['last_updated_date_time'] >= start_dt) & 
            (dataset['last_updated_date_time'] <= end_dt)
        ]

        if date_filtered_dataset.empty:
            print_warning(f"Dataset has no data between {start_date} and {end_date}")
        else:
            break

    while True:
        try:
            country_number = int(input("How many countries do you want in your graph: "))
            if country_number > 0:
                break
            else:
                print_warning("ERROR: Enter a number greater than 0 ")
        except ValueError:
            print_warning("ERROR: Enter an integer")
        
    selected_countries = []

    for i in range(country_number):
        while True:
            print (f"Enter Country #{i + 1} out of {country_number}: ")
            user_country = input_country()
            if user_country in selected_countries:
                print_warning(f"{user_country} has already been input in the country list \n")
            else:
                selected_countries.append(user_country)
                break

    plot_wind_speed(date_filtered_dataset, selected_countries, start_date, end_date)
            
# Function to make the graph
def plot_wind_speed(dataset, country_list, start_date, end_date):
    fig, ax = plt.subplots(figsize=(10, 5))

    for country in country_list:
        # Grabs the data associated with the country that you've chosen
        # Makes sure both comparisons are in lowercase just for better reliability
        countryData = dataset[dataset['country'].str.lower() == country.lower()].copy()

        if countryData.empty:
            continue

        countryData = countryData.sort_values(by='last_updated_date_time')
    
        ax.plot(
            countryData['last_updated_date_time'],
            countryData['wind_kph'],
            marker='o',
            linestyle='-',
            label=f"{country.title()} Wind Speed"
        )

    
    title_countries = ", ".join(country_list)
    ax.set_title(f"Wind Speed from ({start_date} to {end_date}): \n {title_countries}", fontsize=14, pad=15)
    ax.set_xlabel("Date", fontsize=12)
    ax.set_ylabel("Wind Speed (km/h)", fontsize=12)

    ax.xaxis.grid(True, linestyle='--', alpha=0.7)
    ax.yaxis.grid(True, linestyle='--', alpha=0.7)
    plt.xticks(rotation=45)
    ax.legend()
    
    plt.tight_layout()
    plt.show()


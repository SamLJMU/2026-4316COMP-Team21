from classes.file_io import FileIO
from utility.row_transformations import string_time_to_minutes
import matplotlib.pyplot as mpl
import matplotlib.dates as mdates
import pandas as pd
import matplotlib.ticker as ticker
from input import input_country

def minutes_to_military(total_minutes, tick_number):
    hours = int(total_minutes // 60)
    minutes = int(total_minutes % 60)
    return f"{hours:02d}:{minutes:02d}"

# visualise daylight hours over time by country
def daylight_hours():
    # Get dataset
    df = FileIO.dataset_df[["country", "last_updated", "sunrise", "sunset"]]
    df["country"] = df["country"].str.strip().str.title()

    # prompt user for name of country (filter), validate input
    # print("Filter")
    # TODO
    country = input_country()

    # process data per name of country (filter)
    filtered_df = df[df["country"] == country]
    filtered_df["last_updated"] = pd.to_datetime(filtered_df["last_updated"])
    filtered_df = filtered_df.loc[(filtered_df["last_updated"] >= "2025-1-1")]
    filtered_df = filtered_df[filtered_df["last_updated"].dt.day == 1]

    if compare_countries == True:
        filtered_df_2 = df[df["country"] == country_2]
        filtered_df_2["last_updated"] = pd.to_datetime(filtered_df_2["last_updated"])
        filtered_df_2 = filtered_df_2.loc[(filtered_df_2["last_updated"] > "2025-1-1")]
        filtered_df_2 = filtered_df_2[filtered_df_2["last_updated"].dt.day == 1]



    daylight_minutes_list = []
    daylight_minutes_list_2 = []
    dates = []

    # prepare data for visualisation
    for _, row in filtered_df.iterrows():
        sunset_minutes = string_time_to_minutes(row["sunset"])
        sunrise_minutes = string_time_to_minutes(row["sunrise"])
        
        daylight_minutes = sunset_minutes - sunrise_minutes
        
        daylight_minutes_list.append(daylight_minutes)

    if compare_countries == True:
        for _, row in filtered_df_2.iterrows():
            sunset_minutes = string_time_to_minutes(row["sunset"])
            sunrise_minutes = string_time_to_minutes(row["sunrise"])
            
            daylight_minutes = sunset_minutes - sunrise_minutes
            
            daylight_minutes_list_2.append(daylight_minutes)

    # Visualise via matplotlib
    fig, ax = mpl.subplots()
    ax.plot(filtered_df["last_updated"], daylight_minutes_list, color = 'blue', label = country, marker = 'o')
    if compare_countries == True:
        ax.plot(filtered_df["last_updated"], daylight_minutes_list_2, color = 'red', label = country_2, marker = 'o')

    ax.yaxis.set_major_formatter(mpl.FuncFormatter(minutes_to_military))
    ax.yaxis.set_major_locator(ticker.MaxNLocator(nbins=15))
    ax.xaxis.set_major_locator(ticker.MaxNLocator(nbins=20))
    
    ax.set_xlabel("Date")
    ax.set_ylabel("Daylight Hours shown as hh:mm")

    if compare_countries == True:
        ax.set_title(f"Daylight Hours in {country} compared to {country_2}")
    else:
        ax.set_title(f"Daylight Hours in {country}")

    ax.legend()

    mpl.xticks(filtered_df["last_updated"], rotation=45)
    mpl.show()
from classes.file_io import FileIO
import matplotlib.pyplot as mpl
import matplotlib.dates as mdates
import pandas as pd
import matplotlib.ticker as ticker

def format_moon_illumination(illumination_percentage, tick_number):
    return f"{illumination_percentage:.0%}"

# visualise moon illumination over time by country
def moon_illumination():
    # Get dataset
    df = FileIO.dataset_df[["country", "last_updated", "moon_illumination"]]
    df["country"] = df["country"].str.strip().str.title()

    country = "Italy"
    country_2 = "United Kingdom"
    compare_countries = False

    # prompt user for name of country (filter), validate input
    while True:
        country_selection = input("Choose a country, make sure to type the name correctly!\n")
        if country_selection.strip().title() in df["country"].values:
            country = country_selection.strip().title()
            print(f"You selected: {country}")
            break
        else:
            print("Country not found, have you typed the name correctly?")
 
    # prompt user for name of second country (filter), validate input
    while True:
        answer = input("Would you like to choose a second country to compare the results?\n")
        if answer.upper() == "YES" or answer.upper() == "Y":
            country_selection_2 = input("Choose a second country, make sure to type the name correctly!\n")
            if country_selection_2.strip().title() in df["country"].values:
                country_2 = country_selection_2.strip().title()
                compare_countries = True
                print(f"I will compare {country} and {country_2}")
                break
            else:
                print("Country not found, have you typed the name correctly?")
        elif answer.upper() == "NO" or answer.upper() == "N":
            print(f"Perfect, I will only show you the moon illumination of {country}\n")
            break
        else:
            print("Error, was there a typo? Make sure to type either \"Yes\" or \"No\"\n")

    # process data per name of country (filter)
    filtered_df = df[df["country"] == country]
    filtered_df["last_updated"] = pd.to_datetime(filtered_df["last_updated"])
    filtered_df = filtered_df.loc[(filtered_df["last_updated"] > "2026-1-1")]

    if compare_countries == True:
        filtered_df_2 = df[df["country"] == country_2]
        filtered_df_2["last_updated"] = pd.to_datetime(filtered_df_2["last_updated"])
        filtered_df_2 = filtered_df_2.loc[(filtered_df_2["last_updated"] > "2026-1-1")]


    moon_illumination_list = []
    moon_illumination_list_2 = []
    dates = []

    # prepare data for visualisation
    for _, row in filtered_df.iterrows():
        dates.append(row["last_updated"])
        moon_illumination_list.append(row["moon_illumination"])

    if compare_countries == True:
        for _, row in filtered_df_2.iterrows():
            moon_illumination_list_2.append(row["moon_illumination"])

     # Visualise via matplotlib
    fig, ax = mpl.subplots()
    ax.plot(dates, moon_illumination_list, color = 'blue', label = country, marker = 'o')
    if compare_countries == True:
        ax.plot(dates, moon_illumination_list_2, color = 'red', label = country_2, marker = 'o')

    ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))   #test different intervals
    ax.yaxis.set_major_formatter(mpl.FuncFormatter(format_moon_illumination))
    
    ax.set_xlabel("Date")
    ax.set_ylabel("Moon Illumination")

    if compare_countries == True:
        ax.set_title(f"Moon Illumination in {country} compared to {country_2}")
    else:
        ax.set_title(f"Moon Illumination in {country}")

    ax.legend()

    mpl.xticks(dates, rotation=45)
    mpl.show()
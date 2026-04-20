from classes.file_io import FileIO
import matplotlib.pyplot as mpl
import matplotlib.dates as mdates
import pandas as pd
import matplotlib.ticker as ticker
from input import input_country

def format_moon_illumination(illumination_percentage, tick_number):
    return f"{illumination_percentage}%"

# visualise moon illumination over time by country
def moon_illumination():
    # Get dataset
    df = FileIO.dataset_df[["country", "last_updated", "moon_illumination"]]

    country = input_country()

    # process data per name of country (filter)
    filtered_df = df[df["country"] == country]
    filtered_df["last_updated"] = pd.to_datetime(filtered_df["last_updated"])
    filtered_df = filtered_df.loc[(filtered_df["last_updated"] >= "2026-1-1")]

    # Visualise via matplotlib
    fig, ax = mpl.subplots()
    ax.plot(filtered_df["last_updated"], filtered_df["moon_illumination"], color = 'blue', label = country, marker = 'o')

    ax.xaxis.set_major_locator(ticker.MaxNLocator(nbins=25))
    ax.yaxis.set_major_formatter(mpl.FuncFormatter(format_moon_illumination))
    
    ax.set_xlabel("Date")
    ax.set_ylabel("Moon Illumination")

    ax.set_title(f"Moon Illumination in {country}")

    ax.legend()

    mpl.xticks(rotation=45)
    mpl.show()
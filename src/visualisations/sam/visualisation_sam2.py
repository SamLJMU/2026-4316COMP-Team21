from classes.file_io import FileIO
import matplotlib.pyplot as mpl
import pandas as pd
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from input import input_country, input_timeframe

def daylight_and_percipitation():
    
    # filter input
    df = FileIO.dataset_df[["country", "last_updated_date_time", "sunrise", "sunset", "precip_mm"]].copy()

    df["last_updated_date_time"] = pd.to_datetime(df["last_updated_date_time"])
    
    df['sunrise_dt'] = pd.to_datetime(df['sunrise'], format='%I:%M %p', errors='coerce')
    df['sunset_dt'] = pd.to_datetime(df['sunset'], format='%I:%M %p', errors='coerce')
    df['daylight_hours'] = (df['sunset_dt'] - df['sunrise_dt']).dt.total_seconds() / 3600

    # user inputs
    country = input_country()
    timeframe = input_timeframe("Desired timeframe: ")
    
    df = df[df["country"] == country]
    df = df.loc[(df["last_updated_date_time"] >= "2024-01-01")]
    
    period = df.last_updated_date_time.dt.to_period("M")
    df_grouped = df.groupby(period)[["daylight_hours", "precip_mm"]].mean()

    df_grouped.index = df_grouped.index.to_timestamp()

    # matplotlib visualisation
    fig, ax1 = mpl.subplots(figsize=(12, 6))
    ax1.plot(df_grouped.index, df_grouped["daylight_hours"], color='tab:orange', label="Daylight Hours", marker=".")
    ax1.set_xlabel("Date")
    ax1.set_ylabel("Daylight (Hours)", color='tab:orange')
    ax1.tick_params(axis='y', labelcolor='tab:orange')
    ax1.xaxis.grid(True)
    ax1.yaxis.grid(True)
    
    ax2 = ax1.twinx()  
    ax2.plot(df_grouped.index, df_grouped["precip_mm"], color='tab:blue', label="Precipitation (mm)", marker=".")
    ax2.set_ylabel("Precipitation (mm)", color='tab:blue')
    ax2.tick_params(axis='y', labelcolor='tab:blue')
    ax2.fill_between(df_grouped.index, df_grouped["precip_mm"], 0, color='tab:blue', alpha=0.1)
    
    ax1.set_title(f"Daylight Hours and Precipitation in {country} ({timeframe})")
    fig.legend(loc="upper right", bbox_to_anchor=(1,1), bbox_transform=ax1.transAxes)
    
    fig.autofmt_xdate()
    mpl.tight_layout()
    mpl.show()

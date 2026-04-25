from classes.file_io import FileIO
import matplotlib.pyplot as mpl
import pandas as pd
from input import input_country, input_timeframe

def air_pressure_and_percipitation():
    
    df = FileIO.dataset_df[["country", "last_updated_date_time", "pressure_in", "precip_mm"]]

  
   # def input_country():
    # all_countries = sorted(FileIO.dataset_df["country"].unique().tolist())

     #while True:
      #  print("For a list of countries press 1 or input the country name straight away instead")
       # if user_input("1"):
        # print("\nAvailable countries:")
         #for country in all_countries:
          #  print(f"  - {country}")

       # user_input = input("Enter a country name: ").strip()

       # matches = [c for c in all_countries if user_input.lower() in c.lower()]

       # if len(matches) == 1:
        #    print(f"Selected: {matches[0]}")
        #    return matches[0]

       # elif len(matches) > 1:
         #    print(f"\nDid you mean one of these?")
       # for country in matches:
        #        print(f"  - {country}")
       # user_input = input("Enter a country name: ").strip()

       # exact = [c for c in matches if c.lower() == user_input.lower()]
       # if exact:
        #        print(f"Selected: {exact[0]}")
         #       return exact[0]

       # else:
        #    print("Country not found. Try again")

    country = input_country()
    timeframe = input_timeframe("Desired timeframe: ")
    
   # df = df[df["country"] == country]
    #df = df.loc[(df["last_updated_date_time"] >= "2024-01-01")]

    period = df.last_updated_date_time.dt.to_period("M")
    s = df.groupby(period)["pressure_in"].mean()

    # converts series to dataframe
    df = s.to_frame()

    
    df.index = df.index.to_timestamp()

    
    # visualise in matplotlib
    fig, ax = mpl.subplots(figsize=(12, 6))
    ax.plot(df.index, df["pressure_in"], label="Air Pressure", marker=".")
    ax.plot(df.index, df["precip_mm"], label="Precipitation Milimeters", marker=".")
    ax.fill_between(df["last_updated_date_time"], df["pressure_in"], df["precip_"], alpha=0.2)
    ax.set_title("Pressure to precipitation Like by Month per Country")
    ax.set_xlabel("Date")
    ax.set_ylabel("precipitation mm")
    ax.legend()
    ax.xaxis.grid(True)
    ax.yaxis.grid(True)
    fig.autofmt_xdate()
    mpl.tight_layout()
    mpl.show()
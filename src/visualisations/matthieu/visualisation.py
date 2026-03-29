from classes.file_io import FileIO
import matplotlib.pyplot as mpl
import numpy as np
from input import input_country, input_timeframe

def air_quality_over_time():
    # Get dataset
    df = FileIO.dataset_df[["country", "last_updated_date_time", "air_quality_PM2.5", "temperature_celsius"]]

    # Filter Input
    country = input_country("Enter a country name: ", "Country not found. Try again")
    timeframe = input_timeframe("Desired timeframe filter: ")

    # Process data per filter
    df = df[df["country"] == country]
    df = df.loc[(df["last_updated_date_time"] >= timeframe[0]) & (df["last_updated_date_time"] <= timeframe[1])]

    # Group data
    # TODO
    # period = df.last_updated_date_time.dt.to_period("M")
    # s = df.groupby(period)["air_quality_PM2.5"].mean()

    # Converts series to dataframe
    # df = s.to_frame()

    # Converts PeriodIndex to DateTimeIndex, for plotting conversion
    # df.index = df.index.to_timestamp()

    # Visualise via matplotlib
    fig, ax = mpl.subplots()

    # Scatter plot
    ax.scatter(df["temperature_celsius"], df["air_quality_PM2.5"], color="g")
    
    # Line of best fit
    x = df["temperature_celsius"]
    y = df["air_quality_PM2.5"]
    ax.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), color="r")

    # Window settings
    window_width = 10
    window_height = 8
    fig.canvas.manager.set_window_title("Air Pollution relation to Temperature (C)")
    fig.set_figwidth(window_width)
    fig.set_figheight(window_height)
    
    # Graph settings
    mpl.title("Air Pollution relations to Temperature Levels")
    mpl.xlabel("Temperature (Celcius)")
    mpl.ylabel("Air Quality (µg/m3)")
    
    # Display
    mpl.show()
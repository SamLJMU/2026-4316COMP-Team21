from classes.file_io import FileIO
import matplotlib.pyplot as mpl
import numpy as np
from input import (
    input_country, 
    input_timeframe, 
    input_pollution_type, 
    input_filter_by_country
)
from utility.console_print import print_line
from classes.graph_labels import GraphLabels

def air_pollution_relations():
    # Filter Input
    print_line()
    pollution_type = input_pollution_type("Pollution type: ")

    print_line()
    country = input_country()

    print_line()
    timeframe = input_timeframe("Desired timeframe filter: ")

    # Get dataset
    temperature_column = "temperature_celsius"
    wind_speed_column = "wind_mph"
    df = FileIO.dataset_df[["country", "last_updated_date_time", pollution_type, temperature_column, wind_speed_column]]

    # Process data per filter
    df = df[df["country"] == country]
    df = df.loc[(df["last_updated_date_time"] >= timeframe[0]) & (df["last_updated_date_time"] <= timeframe[1])]

    # Visualise via matplotlib
    fig, (ax, ax_) = mpl.subplots(2)

    # Label usage
    quality_type_label = pollution_type.removeprefix("air_quality_")

    # Air Quality per temperature measurements
    ax = mpl.subplot(2, 1, 1)
    x = df[temperature_column]
    y = df[pollution_type]
    labels = GraphLabels(f"Air Pollution {quality_type_label} relations to Temperature Levels", "Temperature (Celcius)", "Air Quality (µg/m3)")
    plot_scatter(ax, x, y, scatter_color="g", line_color="r", labels=labels)

    # Air Quality per wind speed measurements
    ax = mpl.subplot(2, 1, 2)
    x = df[wind_speed_column]
    y = df[pollution_type]
    labels = GraphLabels(f"Air Pollution {quality_type_label} relations to Wind Speed", "Wind Speed (mph)", "Air Quality (µg/m3)")
    plot_scatter(ax, x, y, scatter_color="y", line_color="r", labels=labels)

    # Window settings
    window_width = 10
    window_height = 6
    fig.canvas.manager.set_window_title("Air Pollution relation to Temperature (C) and Wind Speed")
    fig.set_figwidth(window_width)
    fig.set_figheight(window_height)
    fig.tight_layout()
    
    # Display
    mpl.show()

def plot_scatter(ax: mpl.Axes, x, y, scatter_color = "g", line_color = "r", labels: GraphLabels | None = None ):

    # Scatter plot
    ax.scatter(x, y, color=scatter_color)
    
    # Line of best fit
    ax.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), color=line_color)

    # Graph settings
    if(type(labels) is GraphLabels):
        mpl.title(labels.title, loc="left")
        mpl.xlabel(labels.x_label)
        mpl.ylabel(labels.y_label)
    ax.xaxis.grid()
    ax.yaxis.grid()
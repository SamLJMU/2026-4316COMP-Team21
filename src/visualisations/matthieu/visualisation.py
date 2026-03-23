from classes.file_io import FileIO
import matplotlib.pyplot as mpl

def air_quality_over_time():
    # Get dataset
    df = FileIO.dataset_df[["country", "last_updated", "air_quality_PM2.5", "sunrise", "sunrise_time"]]

    print(df.head())

    # Ask for filter
    # print("Filter")
    # TODO
    country = "Argentina"

    # process data per filter
    # TODO
    df = df[df["country"] == country]
    df = df.loc[(df["last_updated"] >= "2026-01-01")]

    # Ask for sorting
    # TODO

    # Ask for sort order
    print("Sort Order")
    # TODO

    # Sort data
    # TODO df.sort_values()

    # Visualise via matplotlib
    fig, ax = mpl.subplots()
    ax.plot(df["last_updated"], df["air_quality_PM2.5"])
    mpl.show()
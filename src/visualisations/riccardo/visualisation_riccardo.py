from classes.file_io import FileIO
import matplotlib.pyplot as mpl

def daylight_hours():
    # Get dataset
    df = FileIO.dataset_df["country", "last_updated", "sunrise", "sunset"]

    # prompt user for name of country (filter), validate input
    # print("Filter")
    # TODO
    country = "Italy"
    while True:
        country_selection = input("Choose a country, make sure to type the name correctly!\n")
        if country_selection.lower() in df["country"].lower().values:
            country = country_selection
            print(country)
            break
        else:
            print("Country not found, have you typed the name correctly?")

    # process data per name of country (filter)
    # TODO
    df = df[df["country"] == country]
    df = df.loc[(df["last_updated"] > "2025-1-1")]

    # Ask for sorting
    # TODO

    # Ask for sort order
    print("Sort Order")
    # TODO

    # Sort data
    # TODO df.sort_values()

    # Visualise via matplotlib
    # TODO filter or group data, else visualization will slow program
    fig, ax = mpl.subplots()
    ax.plot(df["last_updated"], df["sunrise"], df["sunset"])
    mpl.show()
from classes.file_io import FileIO
import matplotlib.pyplot as mpl

def question_example():
    # Get dataset
    df = FileIO.dataset_df[["country", "temperature_celsius"]]

    # Ask for filter
    # print("Filter")
    # TODO

    # process data per filter
    # TODO

    # Ask for sorting
    # TODO

    # Ask for sort order
    print("Sort Order")
    # TODO

    # Sort data
    # TODO df.sort_values()

    # Visualise via matplotlib
    # TODO filter or group data, else visualization will slow program
    # fig, ax = mpl.subplots()
    # ax.plot(df["country"], df["temperature_celsius"])
    # mpl.show()
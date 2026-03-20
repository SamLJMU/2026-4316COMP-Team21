## Functionality

The application should allow the user to visualise data as graphs and filter information
in order to gain useful insights into weather patterns across the globe.

## Requirements

The requirements are:

1) An easy to use, user-friendly menu that allows users to operate the application:
    - Add setting to display Metric or Imperial units by default
2) Ability to accept a variety of user inputs without errors (error validation):
    - Allow user to input paramaters to filter results
3) Outputs:
    - different graphs providing different insights into the data
    - Minimum, Maximum and Average Values for key columns
    - Unit conversion (e.g. Celsius to Fahreneit, mph to kmh)

## Queries

- Temperature change over time country
- Wind Speed over time by country
- Precipitation over time by country
- Temperature by Time Zone
- Weather Condition percentage by country (Sunny, Rainy, etc.)
- Wind Direction by country + possible relation with temperature
- Humidity over time by country
- Relation between Temperature and Feels like Temperature
- Air quality by country
- Sunrise and sunset time by country/latitude

## Accessing dataset within program

- Use the `FileIO` static class from `file_io.py` and get the `dataset_df` property.

``` python

    # Dataframe of dataset
    df = FileIO.dataset_df

    # Getting countries and temperature dataframe
    df = df[["countries", "temperature_celsius"]]

```

# File Structure

__> dataset__

Contains the dataset file(s) that will be loaded into the program for analysis

__> src__

Contains all the source code (i.e classes, functions, etc...)

__> src/classes__

Contains all files that declare and implement classes

__> src/main.py__

Is the main entry point of the program

# Python Modules Explained

> With the exception of main.py and files in src/visualisations, you are not expected to work on the other source files, this is mainly to make it easier to understand their uses.

- __main.py__
    
    Entry point of the program. Should run this script for the application to start.

- __input.py__
    
    Utility module used for input validation

### Classes

- __file_io.py__
    
    Defines a class with a static method used to load the dataset and access it via the `dataset_df` static variable.

    i.e : `FileIO.dataset_df`

- __constants.py__

    Defines constants, notable the `MenuOptions` class with static properties to make menu options more manageable and readable

    i.e of access: `MenuOptions.DAYLIGHT_HOURS` is just a constant for `1` (last updated: 20/03/2026)

### Visualisations

Collection of folders for each team member.

Each of those should contain at least __1 file__ declaring a function that fetches data from the `dataset_df` DataFrame and produce a graph via `matplotlib`

### Additional Notes

> Every module can be imported by specifying their directory followed by the file name. So if we were to import the `FileIO` class into a source file, `from classes.file_io import FileIO` can be written in the source file where we want to use it. As you can see `classes` is the directory and `file_io` is the file name, hence `classes.file_io` importing the class `FileIO`.
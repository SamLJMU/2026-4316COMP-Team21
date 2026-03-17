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
# Functionality

The application should allow the user to visualise data as graphs and filter information
in order to gain useful insights into weather patterns across the globe.

# How to run the program

1. Run the `main.py` file.

2. Select an option from the menu.

3. Input the information requested

4. Once a visualisation opens, you can close it and the main menu will re-appear.

5. Select another option, until you want to exit by entering the number associated with the `Exit` option.

# Requirements

The requirements are:

1) An easy to use, user-friendly menu that allows users to operate the application:
    - Add setting to display Metric or Imperial units by default
2) Ability to accept a variety of user inputs without errors (error validation):
    - Allow user to input paramaters to filter results
3) Outputs:
    - different graphs providing different insights into the data
    - Minimum, Maximum and Average Values for key columns
    - Unit conversion (e.g. Celsius to Fahreneit, mph to kmh)

# Queries

- Temperature change over time country
- Wind Speed over time by country
- Precipitation over time by country
- Average Temperature vs Average Humidity by Time Zone
- Weather Condition percentage by country (Sunny, Rainy, etc.)
- Wind Direction by country + possible relation with temperature
- Humidity over time by country
- Relation between Temperature and Feels like Temperature
- Average Air quality vs Average Wind Speed by country
- Sunrise and sunset time by country/latitude
- Daily Maximum UV Index over Time by Country
- Humidity vs. Cloud Coverage by Country over Time
- Cloud Coverage vs. Feels Like Temperature by Country over Time (inverse relation)

# Branches

`main` is the master branch of the repository, eventually most, if not all of the branches will merge onto it.

__Every__ team member has a branch named after themselves, they should push their progress only to that branch to avoid having `out-of-sync` or `overwrite` issues.

The basic workflow is:

1. Be on your named branch. __NOT `main`__
2. Merge `main` __onto__ your branch, so as to have the most up-to-date code
3. Commit your work on that named branch

A team member will have the role of merging the other branches onto main.

> Note: If you cannot see the branches on VS Code, click on the 3 dots next to refresh and select `Fetch`. After that you should be able to select the branches you could not see.

# Accessing dataset within program

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

__> src/visualisations__

Contains all the visualizations and data processing source code for the graphs of each team member

__> src/utility__

Contains all the functions that are not core functionalities of the program, but used to carry out specific or repetitive tasks

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

### Utilities

- __console_print.py__

    Defines functions to print specific kind of output, such as information, warning, success, etc... in a colored manner.

- __row_transformations.py__

    Defines functions that can be applied to a specific column(s) to convert or compute values.

    Think of them as excel formulas

### Visualisations

Collection of folders for each team member.

Each of those should contain at least __1 file__ declaring a function that fetches data from the `dataset_df` DataFrame and produce a graph via `matplotlib`

### How to add a visualisation

1. Go to `visualisation_config.json`

Add an object with properties `key` and `msg` for your visualisation.

`key` would be the key to a function (more on that in a bit)

`msg` would be the message displayed in the menu for this visualisation

2. Go to `src/function_mapping.py`

Change `function_map` dictionary, and write as key the `key` you specified in Step 1, and as value assign your function for your visualisation.

> Note not to add the `()` when assigning the value, as it needs to hold the function name, not the `return` value of the function which would usually be void or `None` anyways.

__Example:__

`visualisation_config.json`
``` json
[
    ...,
    {
        "key": "test_key",
        "msg": "This is a test"
    },
    ...
]
```

`src/function_mapping.py`
``` python
from visualisations.example.visualisation import test_visualisation

function_map = {
    ...,
    'test_key': test_visualisation,
    ...
}
```

### Additional Notes

> Every module can be imported by specifying their directory followed by the file name. So if we were to import the `FileIO` class into a source file, `from classes.file_io import FileIO` can be written in the source file where we want to use it. As you can see `classes` is the directory and `file_io` is the file name, hence `classes.file_io` importing the class `FileIO`.

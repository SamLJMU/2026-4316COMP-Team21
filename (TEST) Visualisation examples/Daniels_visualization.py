# Wind Speed over x time for y country

import pandas as pd
import matplotlib.pyplot as plt

def plot_wind_speed(dataset, targetCountry):
    # Checks whether the target country and the dataset country is the same, and then the rows that pass the filter
    # create a new table that is stored in here
    countryData = dataset[dataset['country'].str.lower() == targetCountry.lower()].copy()

    if countryData.empty:
        print("Error: There is no data found for " + targetCountry)
        return
    
    fig, ax = plt.subplots(figsize=(10, 5))
    
    ax.plot(
        countryData['last_updated'],
        countryData['wind_kph'],
        marker='o',
        linestyle='-',
        color='#ff7f0e',
        label=f"{targetCountry.title()} Wind Speed"
    )

    ax.set_title(f"Wind Speed Over Time: {targetCountry.title()}", fontsize=14, pad=15)
    ax.set_xlabel("Date", fontsize=12)
    ax.set_ylabel("Wind Speed (km/h)", fontsize=12)

    ax.xaxis.grid(True, linestyle='--', alpha=0.7)
    ax.yaxis.grid(True, linestyle='--', alpha=0.7)
    plt.xticks(rotation=45)
    ax.legend()
    
    plt.tight_layout()
    plt.show()

# So that the code doesn't actually run when imported
if __name__ == "__main__":
    print("Testing with fake data")

    mockData = {
            'last_updated': [
                # United Kingdom Dates (Randomized times)
                '2023-10-01 02:15', '2023-10-01 09:42', '2023-10-01 16:05',
                '2023-10-02 01:30', '2023-10-02 10:11', '2023-10-02 14:55',
                '2023-10-03 04:22', '2023-10-03 13:40', '2023-10-03 21:15',
                '2023-10-04 06:50', '2023-10-04 11:33', '2023-10-04 18:05',
                
                # Brazil Dates (Randomized times)
                '2023-10-01 04:10', '2023-10-01 11:25', '2023-10-01 19:50',
                '2023-10-02 05:45', '2023-10-02 12:15', '2023-10-02 20:30',
                '2023-10-03 02:05', '2023-10-03 09:55', '2023-10-03 16:40',
                '2023-10-04 01:20', '2023-10-04 14:10', '2023-10-04 22:15',
                
                # Nigeria Dates (Randomized times)
                '2023-10-01 01:05', '2023-10-01 08:30', '2023-10-01 15:45',
                '2023-10-02 03:20', '2023-10-02 11:10', '2023-10-02 17:55',
                '2023-10-03 06:15', '2023-10-03 14:25', '2023-10-03 23:10',
                '2023-10-04 05:40', '2023-10-04 12:50', '2023-10-04 19:35'
            ],
            'country': [
                'United Kingdom', 'United Kingdom', 'United Kingdom',
                'United Kingdom', 'United Kingdom', 'United Kingdom',
                'United Kingdom', 'United Kingdom', 'United Kingdom',
                'United Kingdom', 'United Kingdom', 'United Kingdom',
            
                'Brazil', 'Brazil', 'Brazil',
                'Brazil', 'Brazil', 'Brazil',
                'Brazil', 'Brazil', 'Brazil',
                'Brazil', 'Brazil', 'Brazil',
                
                'Nigeria', 'Nigeria', 'Nigeria',
                'Nigeria', 'Nigeria', 'Nigeria',
                'Nigeria', 'Nigeria', 'Nigeria',
                'Nigeria', 'Nigeria', 'Nigeria'
            ],
            'wind_kph': [
                # UK Wind Speeds
                12.5, 18.2, 22.0,
                14.5, 19.1, 25.4,
                28.0, 20.3, 15.5,
                10.2, 8.5, 11.0,
                
                # Brazil Wind Speeds 
                8.0, 11.2, 9.5,
                10.1, 14.3, 12.0,
                9.2, 7.5, 8.8,
                12.4, 15.6, 11.1,
                
                # Nigeria Wind Speeds
                5.2, 7.1, 6.5,
                4.8, 8.2, 9.1,
                10.5, 11.2, 8.4,
                6.3, 5.9, 7.0
            ]
        }

    testDataframe = pd.DataFrame(mockData)
    testDataframe['last_updated'] = pd.to_datetime(testDataframe['last_updated'])
    plot_wind_speed(testDataframe, "United Kingdom")
    plot_wind_speed(testDataframe, "Brazil")
    plot_wind_speed(testDataframe, "Nigeria")
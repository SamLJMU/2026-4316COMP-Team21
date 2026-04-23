import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import dates
from classes.file_io import FileIO
from input import input_multiple_countries

def air_quality_by_country_over_time():
    df = FileIO.dataset_df
    # Normalize text columns that will be used for filtering
    if 'country' in df.columns:
        df['country'] = df['country'].astype(str).str.strip()

    df = df.dropna(subset=['last_updated'])
    df['date'] = pd.to_datetime(df['last_updated'], dayfirst=False, errors='coerce')
    df = df.dropna(subset=['date'])

    # Create a period column for month-level grouping and filtering
    df['period'] = df['date'].dt.to_period('M')

    # date range selection
    print("\nEnter the date range for the data (format YYYY-MM). Leave blank for current date range values.")
    min_period = df['period'].min()
    max_period = df['period'].max()
    print(f"Available span: {min_period} to {max_period}")

    while True:
        start_period_str = input("From (YYYY-MM) or blank: ").strip()
        if not start_period_str:
            start_period = min_period
            break
        try:
            start_period = pd.Period(start_period_str, freq='M')
            break
        except Exception:
            print("Invalid from-format; please use YYYY-MM or leave blank.")

    while True:
        end_period_str = input("To (YYYY-MM) or blank:   ").strip()
        if not end_period_str:
            end_period = max_period
            break
        try:
            end_period = pd.Period(end_period_str, freq='M')
            break
        except Exception:
            print("Invalid to-format; please use YYYY-MM or leave blank.")

    if start_period > end_period:
        print("From-period is after to-period; swapping values.")
        start_period, end_period = end_period, start_period

    # filter by period (month-level)
    df = df[(df['period'] >= start_period) & (df['period'] <= end_period)]
    print(f"Using period range: {start_period} to {end_period} (rows: {len(df)})")

    # Available air quality indices (excluding US and GB indices)
    available_indices = [
        'air_quality_Carbon_Monoxide',
        'air_quality_Ozone',
        'air_quality_Nitrogen_dioxide',
        'air_quality_Sulphur_dioxide',
        'air_quality_PM2.5',
        'air_quality_PM10'
    ]

    # Display indices and let user choose
    print("+" + "-"*21 + "+")
    print("| Air Quality Indices |")
    print("+" + "-"*21 + "+")
    for i, idx in enumerate(available_indices, 1):
        display_name = idx.replace('air_quality_', '').replace('_', ' ')
        print(f"{i}. {display_name}")

    while True:
        choice = input("\nSelect an index by list number: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(available_indices):
            selected_index = available_indices[int(choice) - 1]
            break
        elif choice.lower() in [idx.lower() for idx in available_indices]:
            selected_index = next(idx for idx in available_indices if idx.lower() == choice.lower())
            break
        else:
            print("❌ Invalid choice. Try again.")

    print(f"✅ Selected: {selected_index.replace('air_quality_', '').replace('_', ' ')}")

    # Countries input for filtering
    print("\n--- Select Countries ---")
    selected_countries = input_multiple_countries()
    
    # Convert selected index and wind columns to numeric (coerce non-numeric values)
    df[selected_index] = pd.to_numeric(df[selected_index], errors='coerce')
    if 'wind_kph' in df.columns:
        df['wind_kph'] = pd.to_numeric(df['wind_kph'], errors='coerce')

    # Now plot selected countries
    if selected_countries:
        # Filter down to only the selected countries to speed up grouping
        selected_countries_lower = [c.lower() for c in selected_countries]
        country_mask = df['country'].str.lower().isin(selected_countries_lower)
        
        # Figure out which columns we need to average
        cols_to_avg = [selected_index]
        if 'wind_kph' in df.columns:
            cols_to_avg.append('wind_kph')
            
        # Group by Month (period) and Country, then calculate the average
        avg_df = df[country_mask].groupby(['period', 'country'])[cols_to_avg].mean().reset_index()
        avg_df['month_start'] = avg_df['period'].apply(lambda p: p.to_timestamp())

        # Create a figure with 2 subplots, shared X-axis.
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
        
        for country in selected_countries:
            # Pull the averaged data for this specific country
            country_df = avg_df[avg_df['country'].str.lower() == country.lower()]
            
            if not country_df.empty:
                # Plot Monthly Average Air Quality on top chart (ax1)
                aq_df = country_df.dropna(subset=[selected_index])
                if not aq_df.empty:
                    ax1.plot(aq_df['month_start'], aq_df[selected_index], marker='o', label=country, linewidth=1.5)
                else:
                    print(f"\nNo numeric data for {country} in {selected_index}")
                
                # Plot Monthly Average Wind Speed on bottom chart (ax2)
                if 'wind_kph' in avg_df.columns:
                    wind_df = country_df.dropna(subset=['wind_kph'])
                    if not wind_df.empty:
                        ax2.plot(wind_df['month_start'], wind_df['wind_kph'], marker='o', label=country, linewidth=1.5)
                    else:
                        print(f"\nNo wind data for {country}")
                        
        index_name = selected_index.replace('air_quality_', '').replace('_', ' ')
        
        # Formatting Top Subplot (Air Quality)
        ax1.set_title(f'Average {index_name} Over Time')
        ax1.set_ylabel(f'{index_name}')
        ax1.legend()
        ax1.grid(True, linestyle='--', alpha=0.6)

        # Formatting Bottom Subplot (Wind)
        ax2.set_title('Average Wind Speed Over Time')
        ax2.set_xlabel('Month')
        ax2.set_ylabel('Wind Speed (kph)')
        ax2.legend()
        ax2.grid(True, linestyle='--', alpha=0.6)

        # Format the shared X-axis dates for monthly view
        ax2.xaxis.set_major_locator(dates.AutoDateLocator())
        ax2.xaxis.set_major_formatter(dates.DateFormatter('%Y-%m'))
        fig.autofmt_xdate(rotation=45)

        plt.tight_layout()
        plt.savefig('air_quality_and_wind_plot.png')
        print(f"✅ Plot saved as air_quality_and_wind_plot.png for {', '.join(selected_countries)}")
        plt.show()
    else:
        print("\nNo countries selected.")
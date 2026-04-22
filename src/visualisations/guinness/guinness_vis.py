import pandas as pd
import matplotlib.pyplot as plt
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

    # date range selection
    print("\nEnter the date range for the data (format YYYY-MM-DD). Leave blank for current date range values.")
    min_date = df['date'].min().date()
    max_date = df['date'].max().date()
    print(f"Available span: {min_date} to {max_date}")

    # strict + flexible input handling with separate loops
    while True:
        start_date_str = input("From date (or blank): ").strip()
        if not start_date_str:
            start_date = min_date
            break
        try:
            start_date = pd.to_datetime(start_date_str).date()
            break
        except Exception:
            print("Invalid from-date format; please use YYYY-MM-DD or leave blank.")

    while True:
        end_date_str = input("To date (or blank):   ").strip()
        if not end_date_str:
            end_date = max_date
            break
        try:
            end_date = pd.to_datetime(end_date_str).date()
            break
        except Exception:
            print("Invalid to-date format; please use YYYY-MM-DD or leave blank.")

    if start_date > end_date:
        print("From-date is after to-date; swapping values.")
        start_date, end_date = end_date, start_date

    df = df[(df['date'].dt.date >= start_date) & (df['date'].dt.date <= end_date)]
    print(f"Using date range: {start_date} to {end_date} (rows: {len(df)})")

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
    
    # Convert selected index and humidity columns to numeric (coerce non-numeric values)
    df[selected_index] = pd.to_numeric(df[selected_index], errors='coerce')
    if 'humidity' in df.columns:
        df['humidity'] = pd.to_numeric(df['humidity'], errors='coerce')

    # Now plot selected countries
    if selected_countries:
        # Create a figure with 2 subplots, shared X-axis.
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
        
        for country in selected_countries:
            country_df = df[df['country'].str.lower() == country.lower()]
            
            if not country_df.empty:
                # Plot Air Quality on top chart (ax1)
                aq_df = country_df.dropna(subset=[selected_index])
                if not aq_df.empty:
                    ax1.plot(aq_df['date'], aq_df[selected_index], label=country)
                else:
                    print(f"\nNo numeric data for {country} in {selected_index}")
                
                # Plot Humidity on bottom chart (ax2)
                if 'humidity' in df.columns:
                    hum_df = country_df.dropna(subset=['humidity'])
                    if not hum_df.empty:
                        ax2.plot(hum_df['date'], hum_df['humidity'], label=country)
                    else:
                        print(f"\nNo humidity data for {country}")
                        
        index_name = selected_index.replace('air_quality_', '').replace('_', ' ')
        
        # Formatting Top Subplot (Air Quality)
        ax1.set_title(f'{index_name} Over Time - Selected Countries')
        ax1.set_ylabel(index_name)
        ax1.legend()
        ax1.grid(True, linestyle='--', alpha=0.6)

        # Formatting Bottom Subplot (Humidity)
        ax2.set_title('Humidity Over Time - Selected Countries')
        ax2.set_xlabel('Date')
        ax2.set_ylabel('Humidity')
        ax2.legend()
        ax2.grid(True, linestyle='--', alpha=0.6)

        # Rotate the dates for better readability
        fig.autofmt_xdate(rotation=45)

        plt.tight_layout()
        plt.savefig('air_quality_and_humidity_plot.png')
        print(f"✅ Plot saved as air_quality_and_humidity_plot.png for {', '.join(selected_countries)}")
        plt.show()
    else:
        print("\nNo countries selected.")
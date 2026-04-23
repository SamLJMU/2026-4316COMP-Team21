from matplotlib import dates
import pandas as pd
import matplotlib.pyplot as plt
from classes.file_io import FileIO
from input import input_multiple_timezones 

def avg_temp_by_country_over_time():
    df = FileIO.dataset_df
    # Normalize text columns that will be used for filtering
    if 'timezone' in df.columns:
        df['timezone'] = df['timezone'].astype(str).str.strip()

    df = df.dropna(subset=['last_updated'])
    df['date'] = pd.to_datetime(df['last_updated'], dayfirst=False, errors='coerce')
    df = df.dropna(subset=['date'])

    # date range selection by year/month (aggregate by month)
    # create a period column for month-level grouping
    df['period'] = df['date'].dt.to_period('M')
    print("\nEnter the date range for the data (format YYYY-MM). Leave blank for current date range values.")
    min_period = df['period'].min()
    max_period = df['period'].max()
    print(f"Available span: {min_period} to {max_period}")

    # strict + flexible input handling with separate loops (YYYY-MM expected)
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

    # Available temperature units
    available_units = [
        'temperature_celsius',
        'temperature_fahrenheit',
    ]

    # Display indices and let user choose
    print("+" + "-"*19 + "+")
    print("| Temperature Units |")
    print("+" + "-"*19 + "+")
    for i, idx in enumerate(available_units, 1):
        display_name = idx.replace('temperature_', '').replace('_', ' ')
        display_name = display_name.capitalize()
        print(f"{i}. {display_name}")

    while True:
        choice = input("\nSelect an index by list number: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(available_units):
            selected_index = available_units[int(choice) - 1]
            break
        elif choice.lower() in [idx.lower() for idx in available_units]:
            selected_index = next(idx for idx in available_units if idx.lower() == choice.lower())
            break
        else:
            print("❌ Invalid choice. Try again.")

    print(f"✅ Selected: {selected_index.replace('temperature_', '').replace('_', ' ').capitalize()}")

    print("\n--- Select Timezones ---")
    selected_timezones = input_multiple_timezones()

    # Convert selected temperature and humidity columns to numeric (coerce non-numeric values)
    df[selected_index] = pd.to_numeric(df[selected_index], errors='coerce')
    if 'humidity' in df.columns:
        df['humidity'] = pd.to_numeric(df['humidity'], errors='coerce')

    # Calculate average temperature and humidity for the date range and selected timezones
    cols_to_average = [selected_index]
    if 'humidity' in df.columns:
        cols_to_average.append('humidity')

    avg_data = df[df['timezone'].isin(selected_timezones)].groupby(['period', 'timezone'])[cols_to_average].mean().reset_index()
    avg_data['month_start'] = avg_data['period'].apply(lambda p: p.to_timestamp())

    # Now plot average temperature and humidity for the selected timezones
    if selected_timezones:
        # Create a figure with 2 subplots, shared X-axis
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
        
        for timezone in avg_data['timezone'].unique():
            timezone_df = avg_data[avg_data['timezone'] == timezone]
            
            if not timezone_df.empty:
                x = timezone_df['month_start'].dt.to_pydatetime()
                
                # Plot Selected Temperature on the top chart (ax1)
                y_temp = timezone_df[selected_index].dropna()
                if not y_temp.empty:
                    ax1.plot(x[:len(y_temp)], y_temp, marker='o', label=timezone, linewidth=1.5)
                
                # Plot Humidity on the bottom chart (ax2)
                if 'humidity' in avg_data.columns:
                    y_humidity = timezone_df['humidity'].dropna()
                    if not y_humidity.empty:
                        ax2.plot(x[:len(y_humidity)], y_humidity, marker='o', label=timezone, linewidth=1.5)
            else:
                print(f"\nNo numeric data for {timezone}")

        index_name = selected_index.replace('temperature_', '').replace('_', ' ').capitalize()
        unit_label = "°C" if "celsius" in selected_index else "°F"

        # Formatting Top Subplot (Temperature)
        ax1.set_title(f'Average {index_name} Over Time')
        ax1.set_ylabel(f'Temperature ({unit_label})')
        ax1.legend()
        ax1.grid(True, linestyle='--', alpha=0.6)

        # Formatting Bottom Subplot (Humidity)
        ax2.set_title('Average Humidity Over Time')
        ax2.set_xlabel('Month')
        ax2.set_ylabel('Humidity (%)')
        ax2.legend()
        ax2.grid(True, linestyle='--', alpha=0.6)

        # Format the shared X-axis dates
        ax2.xaxis.set_major_locator(dates.AutoDateLocator())
        ax2.xaxis.set_major_formatter(dates.DateFormatter('%Y-%m'))
        plt.setp(ax2.xaxis.get_majorticklabels(), rotation=45)

        plt.tight_layout()
        plt.savefig('temperature_and_humidity_plot.png')
        print(f"✅ Plot saved as temperature_and_humidity_plot.png for {', '.join(selected_timezones)}")
        plt.show()
    else:
        print("\nNo timezones selected.")
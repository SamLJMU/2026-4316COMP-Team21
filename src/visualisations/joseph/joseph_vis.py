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

    print("\n--- Select Timezones ---")
    selected_timezones = input_multiple_timezones()

    # Convert BOTH selected index columns to numeric (coerce non-numeric values)
    df['temperature_celsius'] = pd.to_numeric(df['temperature_celsius'], errors='coerce')
    df['temperature_fahrenheit'] = pd.to_numeric(df['temperature_fahrenheit'], errors='coerce')

    # Calculate average temperature for the date range and selected timezones for BOTH units
    avg_temp = df[df['timezone'].isin(selected_timezones)].groupby(['period', 'timezone'])[['temperature_celsius', 'temperature_fahrenheit']].mean().reset_index()
    avg_temp['month_start'] = avg_temp['period'].apply(lambda p: p.to_timestamp())

    # Now plot average temperature for the selected timezones
    if selected_timezones:
        # Create a figure with 2 subplots, shared X-axis
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
        
        for timezone in avg_temp['timezone'].unique():
            timezone_df = avg_temp[avg_temp['timezone'] == timezone]
            
            if not timezone_df.empty:
                x = timezone_df['month_start'].dt.to_pydatetime()
                
                # Plot Celsius on the top chart (ax1)
                y_celsius = timezone_df['temperature_celsius'].dropna()
                if not y_celsius.empty:
                    ax1.plot(x[:len(y_celsius)], y_celsius, marker='o', label=timezone, linewidth=1.5)
                
                # Plot Fahrenheit on the bottom chart (ax2)
                y_fahrenheit = timezone_df['temperature_fahrenheit'].dropna()
                if not y_fahrenheit.empty:
                    ax2.plot(x[:len(y_fahrenheit)], y_fahrenheit, marker='o', label=timezone, linewidth=1.5)
            else:
                print(f"\nNo numeric data for {timezone}")

        # Formatting Top Subplot (Celsius)
        ax1.set_title('Average Temperature Over Time - Celsius')
        ax1.set_ylabel('Temperature (°C)')
        ax1.legend()
        ax1.grid(True, linestyle='--', alpha=0.6)

        # Formatting Bottom Subplot (Fahrenheit)
        ax2.set_title('Average Temperature Over Time - Fahrenheit')
        ax2.set_xlabel('Month')
        ax2.set_ylabel('Temperature (°F)')
        ax2.legend()
        ax2.grid(True, linestyle='--', alpha=0.6)

        # Format the shared X-axis dates
        ax2.xaxis.set_major_locator(dates.AutoDateLocator())
        ax2.xaxis.set_major_formatter(dates.DateFormatter('%Y-%m'))
        plt.setp(ax2.xaxis.get_majorticklabels(), rotation=45)

        plt.tight_layout()
        plt.savefig('average_temperature_plot.png')
        print(f"✅ Plot saved as average_temperature_plot.png for {', '.join(selected_timezones)}")
        plt.show()
    else:
        print("\nNo timezones selected.")
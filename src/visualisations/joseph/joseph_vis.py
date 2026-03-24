import pandas as pd
import matplotlib.pyplot as plt
from classes.file_io import FileIO

def avg_temp_by_country_over_time():
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

    # Available temperature units
    available_units = [
        'temperature_celsius',
        'temperature_fahrenheit',
    ]
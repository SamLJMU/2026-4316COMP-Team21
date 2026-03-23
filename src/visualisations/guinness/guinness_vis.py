import pandas as pd
import matplotlib.pyplot as plt
from classes.file_io import FileIO

def air_quality_by_country_over_time():
    df = FileIO.dataset_df
    df.columns = df.columns.str.strip()  # Remove leading/trailing spaces from column names
    # Normalize text columns that will be used for filtering
    if 'country' in df.columns:
        df['country'] = df['country'].astype(str).str.strip()

    df = df.dropna(subset=['last_updated'])
    df['date'] = pd.to_datetime(df['last_updated'], dayfirst=True, errors='coerce')
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
        choice = input("Select an index by number or name: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(available_indices):
            selected_index = available_indices[int(choice) - 1]
            break
        elif choice.lower() in [idx.lower() for idx in available_indices]:
            selected_index = next(idx for idx in available_indices if idx.lower() == choice.lower())
            break
        else:
            print("❌ Invalid choice. Try again.")

    print(f"✅ Selected: {selected_index.replace('air_quality_', '').replace('_', ' ')}")

    # Get unique countries
    available_countries = sorted([c.strip() for c in df['country'].unique() if pd.notna(c)])
    page_size = 10
    current_page = 0
    total_pages = (len(available_countries) + page_size - 1) // page_size

    # Pagination loop for countries
    selected_countries = []
    while True:
        start = current_page * page_size
        end = start + page_size
        page_countries = available_countries[start:end]
    
        if selected_countries:
            print(f"\nSelected countries: {', '.join(selected_countries)}")

        print(f"\nPage {current_page + 1} of {(len(available_countries) + page_size - 1) // page_size}:")
        for i, country in enumerate(page_countries, 1):
            print(f"{i}. {country}")
    
        print("\nOptions: 'next', 'prev', 'done', 'help', or pick by page number/country name.")
        choice = input("Your choice: ").strip()
        choice_lower = choice.lower()
    
        if choice_lower == 'help':
            print("Enter 'next'/'prev' to browse pages, 'done' to finish, page number (1-10) to select by position, or country name to add/remove from selection.")
            continue
        if choice_lower == 'help':
            print("Enter 'next'/'prev' to browse, 'done' to finish, page number (1-10) or country name.")
            continue
        if choice_lower == 'next':
            current_page = (current_page + 1) % total_pages
            continue
        if choice_lower == 'prev':
            current_page = (current_page - 1) % total_pages
            continue
        if choice_lower == 'done':
            break

        if choice.isdigit() and 1 <= int(choice) <= len(page_countries):
            exact_country = page_countries[int(choice) - 1]
        elif choice_lower in [c.lower() for c in available_countries]:
            exact_country = next(c for c in available_countries if c.lower() == choice_lower)
        elif choice == '':
            print("Invalid choice. Try again. Please enter a country name, page number, or command (next/prev/done/help).")
            continue
        else:
            similar = [c for c in available_countries if choice_lower in c.lower()]
            if len(similar) == 1:
                exact_country = similar[0]
                if exact_country in selected_countries:
                    selected_countries.remove(exact_country)
                    print(f"Removed {exact_country} (auto-match)")
                else:
                    selected_countries.append(exact_country)
                    print(f"Added {exact_country} (auto-match)")
            else:
                print(f"Invalid choice. Try again. Similar countries: {similar[:10]}")
            continue

        if exact_country in selected_countries:
            selected_countries.remove(exact_country)
            print(f"Removed {exact_country}")
        else:
            selected_countries.append(exact_country)
            print(f"Added {exact_country}")

    # Convert selected index column to numeric (coerce non-numeric values)
    df[selected_index] = pd.to_numeric(df[selected_index], errors='coerce')

    # Now plot selected countries for the selected index
    if selected_countries:
        plt.figure(figsize=(12,6))
        for country in selected_countries:
            country_df = df[df['country'].str.lower() == country.lower()]
            if not country_df.empty:
                country_df = country_df.dropna(subset=[selected_index])
                if not country_df.empty:
                    plt.plot(country_df['date'], country_df[selected_index], label=country)
                else:
                    print(f"No numeric data for {country} in {selected_index}")
    
        index_name = selected_index.replace('air_quality_', '').replace('_', ' ')
        plt.title(f'{index_name} Over Time - Selected Countries')
        plt.xlabel('Date')
        plt.ylabel(index_name)
        plt.legend()
        plt.tight_layout()
        plt.savefig('air_quality_plot.png')
        print(f"✅ Plot saved as air_quality_plot.png for {', '.join(selected_countries)} - {index_name}")
    else:
        print("No countries selected.")
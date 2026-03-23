import pandas as pd
import matplotlib.pyplot as plt
import os

base = os.path.dirname(__file__)
csv_path = os.path.join(base, '..', '..', 'dataset', 'GlobalWeatherRepository.csv')
csv_path = os.path.normpath(csv_path)
df = pd.read_csv(csv_path, engine='python')
df = df.dropna(subset=['last_updated'])
df['date'] = pd.to_datetime(df['last_updated'], dayfirst=True, errors='coerce')
df = df.dropna(subset=['date'])

# Get unique countries
available_countries = sorted(df['country'].unique())
page_size = 10
current_page = 0

# Pagination loop
selected_countries = []
while True:
    start = current_page * page_size
    end = start + page_size
    page_countries = available_countries[start:end]
    
    print(f"\nPage {current_page + 1} of {len(available_countries) // page_size + 1}:")
    for i, country in enumerate(page_countries, 1):
        print(f"{i}. {country}")
    
    print("\nOptions: 'next' (next page), 'prev' (previous page), 'done' (finish selecting), or type a country name to add it.")
    choice = input("Your choice: ").strip().lower()
    
    if choice == 'next' and end < len(available_countries):
        current_page += 1
    elif choice == 'prev' and current_page > 0:
        current_page -= 1
    elif choice == 'done':
        break
    elif choice in [c.lower() for c in available_countries]:
        # Find exact match
        exact_country = next(c for c in available_countries if c.lower() == choice)
        if exact_country not in selected_countries:
            selected_countries.append(exact_country)
            print(f"Added {exact_country}")
        else:
            print(f"{exact_country} already selected")
    else:
        print("Invalid choice. Try again.")

# Now plot selected countries
if selected_countries:
    plt.figure(figsize=(12,6))
    for country in selected_countries:
        country_df = df[df['country'].str.lower() == country.lower()]
        if not country_df.empty:
            plt.plot(country_df['date'], country_df['air_quality_PM2.5'], label=country)
    
    plt.title('PM2.5 Over Time - Selected Countries')
    plt.xlabel('Date')
    plt.ylabel('PM2.5')
    plt.legend()
    plt.tight_layout()
    plt.savefig('pm25_plot.png')
    print(f"Plot saved as pm25_plot.png for {', '.join(selected_countries)}")
else:
    print("No countries selected.")
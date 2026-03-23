import pandas as pd
import matplotlib.pyplot as plt
 
df = pd.read_csv('GlobalWeatherRepository - Guinness.csv', engine='python')
df = df.dropna(subset=['last_updated'])
df['date'] = pd.to_datetime(df['last_updated'], dayfirst=True, errors='coerce')
df = df.dropna(subset=['date'])
 
plt.figure(figsize=(12,6))
plt.plot(df['date'], df['air_quality_PM2.5'])
plt.title('Germany 2025 PM2.5 Over Time')
plt.xlabel('Date')
plt.ylabel('PM2.5')
plt.tight_layout()
plt.savefig('germany_pm25_plot.png')
import matplotlib.pyplot as plt

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

humidity_data = {
    "Nigeria":  [60, 62, 65, 70, 75, 80, 85, 83, 78, 72, 65, 61],
    "UK":       [80, 78, 72, 68, 65, 62, 63, 65, 68, 73, 78, 81],
    "Brazil":   [85, 84, 83, 80, 78, 75, 73, 74, 76, 79, 82, 85],
}

fig, ax = plt.subplots(figsize=(12, 6))

for country, values in humidity_data.items():
    ax.plot(months, values, marker='o', label=country)

ax.set_xlabel("Month")
ax.set_ylabel("Humidity (%)")
ax.set_title("Humidity by Month per Country")
ax.legend()

ax.xaxis.grid()
ax.yaxis.grid()


plt.tight_layout()
plt.show()
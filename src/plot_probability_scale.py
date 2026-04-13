import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/events.csv")

# NEW: load weather data
weather = pd.read_csv("data/weather_tallinn.csv")

# probability of rain (simple estimate)
rain_prob = (weather["rain_mm"] > 0).sum() / len(weather)

print("Rain probability:", rain_prob)

# sort väikseimast suurimani
df = df.sort_values("probability")

plt.figure(figsize=(10,6))

# horisontaalne bar chart
colors = [
    "#2E7D32" if "forest" in e.lower() or "moose" in e.lower()
    else "#1565C0" if "rain" in e.lower()
    else "#C62828"
    for e in df["event"]
]

plt.barh(df["event"], df["probability"], color=colors)

# log scale
plt.xscale("log")

# lisad
plt.xlabel("Probability (log scale)")
plt.title("Probability Scale of Real-World Events (Estonia / RMK context)")
plt.grid(True, which="both", linestyle="--", alpha=0.4)

plt.tight_layout()

# SALVESTAME PILDI (väga oluline GitHubi jaoks!)
plt.savefig("outputs/probability_scale.png", dpi=200)

plt.show()

plt.savefig("outputs/probability_scale.png", dpi=300, bbox_inches="tight")
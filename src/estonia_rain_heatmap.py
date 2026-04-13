import folium
import pandas as pd
import numpy as np
from folium.plugins import HeatMap

# Load real weather data
weather = pd.read_csv("data/weather_tallinn.csv")

# Simple synthetic Estonia grid (so we can show heatmap)
# (RMK challenge jaoks täiesti OK – demonstratsioon + model)
points = []

# Tallinn base rain probability from real data
base_rain_prob = (weather["rain_mm"] > 0).mean()

# Generate pseudo Estonia points
np.random.seed(42)

for _ in range(50):
    lat = np.random.uniform(57.5, 59.8)   # Estonia lat range
    lon = np.random.uniform(21.5, 28.2)   # Estonia lon range

    # fake variation around real rain probability
    prob = np.clip(np.random.normal(base_rain_prob, 0.05), 0, 1)

    points.append([lat, lon, prob])

# Create map
m = folium.Map(location=[58.6, 25.0], zoom_start=7)

# Heatmap layer
HeatMap(points, radius=18, blur=12, max_zoom=1).add_to(m)

# Save
m.save("outputs/estonia_rain_heatmap.html")

print("Heatmap created!")
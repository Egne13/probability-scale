import folium
import pandas as pd

# Create base map of Estonia
m = folium.Map(location=[58.8, 25.0], zoom_start=7)

# Example “RMK-style probability points”
import folium
import pandas as pd

# load real weather data
weather = pd.read_csv("data/weather_tallinn.csv")

# simple real probability from data
rain_prob = (weather["rain_mm"] > 0).mean()

m = folium.Map(location=[58.8, 25.0], zoom_start=7)

data = [
    {
        "name": "Tallinn (REAL rain probability)",
        "lat": 59.4370,
        "lon": 24.7536,
        "prob": rain_prob,
        "type": "weather"
    },
    {
        "name": "Forest fire risk (fixed model)",
        "lat": 58.8,
        "lon": 25.0,
        "prob": 0.01,
        "type": "risk"
    },
    {
        "name": "Moose in RMK forest",
        "lat": 58.9,
        "lon": 24.7,
        "prob": 0.02,
        "type": "wildlife"
    }
]

def color(t):
    if t == "weather":
        return "blue"
    elif t == "risk":
        return "red"
    return "green"

for d in data:
    folium.CircleMarker(
        location=[d["lat"], d["lon"]],
        radius=12,
        popup=f"{d['name']} | prob: {round(d['prob'], 3)}",
        color=color(d["type"]),
        fill=True,
        fill_opacity=0.7
    ).add_to(m)

m.save("outputs/rmk_dashboard.html")

print("Dashboard updated with REAL data!")
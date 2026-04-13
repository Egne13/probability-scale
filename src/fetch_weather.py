import requests
import pandas as pd

# Tallinn coordinates
lat = 59.4370
lon = 24.7536

url = (
    "https://api.open-meteo.com/v1/forecast"
    f"?latitude={lat}&longitude={lon}"
    "&daily=precipitation_sum,temperature_2m_max"
    "&timezone=auto"
)

response = requests.get(url)
data = response.json()

df = pd.DataFrame({
    "date": data["daily"]["time"],
    "rain_mm": data["daily"]["precipitation_sum"],
    "temp_max": data["daily"]["temperature_2m_max"]
})

df.to_csv("data/weather_tallinn.csv", index=False)

print("Weather data saved!")
import folium

# Estonia center
map_estonia = folium.Map(location=[58.5953, 25.0136], zoom_start=7)

# Tallinn (rain probability)
folium.CircleMarker(
    location=[59.4370, 24.7536],
    radius=10,
    popup="Tallinn: Rain probability ~0.35",
    color="blue",
    fill=True
).add_to(map_estonia)

# Tartu
folium.CircleMarker(
    location=[58.3776, 26.7290],
    radius=8,
    popup="Tartu",
    color="green",
    fill=True
).add_to(map_estonia)

# Pärnu
folium.CircleMarker(
    location=[58.3859, 24.4971],
    radius=7,
    popup="Pärnu",
    color="red",
    fill=True
).add_to(map_estonia)

map_estonia.save("outputs/estonia_map.html")

print("Map created!")
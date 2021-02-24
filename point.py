import folium
import pandas as pd
from folium import Circle

hospitals = pd.read_csv("hos.csv")
bubble_map = folium.Map(location=[13.0700,80.2492], tiles='cartodbpositron', zoom_start=11) 
def color_producer(val):
    if val <= 500:
        return "forestgreen"
    else:
        return "darkred"

for i in range(0,len(hospitals)):
    Circle(
        location=[hospitals.iloc[i]['latitude'], hospitals.iloc[i]['longitude']],
        radius=100,
        color=color_producer(hospitals.iloc[i]["capacity"])).add_to(bubble_map)

# Display the map
bubble_map.save("kk.html")

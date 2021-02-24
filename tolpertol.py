import folium
import pandas as pd
from folium.plugins import MarkerCluster
from folium import plugins
from folium.plugins import MeasureControl
from folium.plugins import Draw
from folium.plugins import FloatImage
from folium import Circle

m = folium.Map(location=[13.0700,80.2492], zoom_start=5)
hospitals = pd.read_csv("hos.csv")
def color_producer(val):
    if val <= 500:
        return "forestgreen"
    else:
        return "darkred"

for i in range(0,len(hospitals)):
    Circle(
        location=[hospitals.iloc[i]['latitude'], hospitals.iloc[i]['longitude']],
        radius=500,
        color=color_producer(hospitals.iloc[i]["capacity"])).add_to(m)

marker_cluster = MarkerCluster().add_to(m)
icon_url='https://cdn1.iconfinder.com/data/icons/transportation-filled-outline/64/toll-plaza-transportation-256.png'
df = pd.read_csv('tolgate.csv')
for index, row in df.iterrows():
    folium.Marker(location=[row['latitude'], row['longitude']],popup=row['name'],icon=folium.features.CustomIcon(icon_url,icon_size=(60, 60))).add_to(marker_cluster)


pe=pd.read_csv('petrol.csv')
icon_url = 'https://cdn1.iconfinder.com/data/icons/transportation-330/100/Fuel_Dispenser-256.png'
for index, row in pe.iterrows():
    folium.Marker(location=[row['latitude'], row['longitude']],popup=row['name'],icon = folium.features.CustomIcon(icon_url,icon_size=(80, 80))).add_to(marker_cluster)
atm=pd.read_csv('atm.csv')
icon_url='https://cdn3.iconfinder.com/data/icons/airport-scenes/64/man_using_atm-512.png'
for index, row in atm.iterrows():
    folium.Marker(location=[row['latitude'], row['longitude']],popup=row['name'],icon=folium.features.CustomIcon(icon_url,icon_size=(100, 100))).add_to(marker_cluster)

at = pd.read_csv('hotel.csv')
icon_url='https://cdn4.iconfinder.com/data/icons/map-pins-2/256/21-256.png'
for index, row in at.iterrows():
    folium.Marker(location=[row['latitude'], row['longitude']],popup=row['name'],icon=folium.features.CustomIcon(icon_url,icon_size=(60, 60))).add_to(marker_cluster)

tp = pd.read_csv('truckrepairshops.csv')
icon_url='https://cdn4.iconfinder.com/data/icons/landscapes-places-scenes-still-life/512/44-256.png'
for index, row in tp.iterrows():
    folium.Marker(location=[row['latitude'], row['longitude']],popup=row['name'],icon=folium.features.CustomIcon(icon_url,icon_size=(60, 60))).add_to(marker_cluster)

we = pd.read_csv('weigh.csv')
icon_url='https://image.shutterstock.com/image-vector/dangerous-garbage-truck-on-weighing-260nw-1826699066.jpg'
for index, row in we.iterrows():
    folium.Marker(location=[row['latitude'], row['longitude']],popup=row['name'],icon=folium.features.CustomIcon(icon_url,icon_size=(60, 60))).add_to(marker_cluster)

p = pd.read_csv('parking.csv')
icon_url='https://cdn2.iconfinder.com/data/icons/parking-filledoutline/64/TOW_TRUCK-car_breakdown-tow-breakdown-truck_-256.png'
for index, row in p.iterrows():
    folium.Marker(location=[row['latitude'], row['longitude']],popup=row['name'],icon=folium.features.CustomIcon(icon_url,icon_size=(60, 60))).add_to(marker_cluster)
# Adds tool to the top right

m.add_child(MeasureControl())

# Fairly obvious I imagine - works best with transparent backgrounds
url = ('https://media.licdn.com/mpr/mpr/shrinknp_100_100/AAEAAQAAAAAAAAlgAAAAJGE3OTA4YTdlLTkzZjUtNDFjYy1iZThlLWQ5OTNkYzlhNzM4OQ.jpg')
FloatImage(url, bottom=5, left=85).add_to(m)

draw = Draw(export=True)
draw.add_to(m)

m.save("loci.html")
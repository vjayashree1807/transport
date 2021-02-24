import openrouteservice
import folium
from folium import plugins
from folium.plugins import Search
from folium.plugins import Terminator
import pandas as pd
df = pd.read_csv('route.csv')
t=pd.read_csv('traffic.csv')

m = folium.Map(location=[13.0700,80.2492], zoom_start=15)
folium.Marker([13.0700,80.2492], popup="Women's Christian College", tooltip='click').add_to(m)
# map
folium.raster_layers.TileLayer('Open Street Map').add_to(m)
folium.raster_layers.TileLayer('Stamen Terrain').add_to(m)
folium.raster_layers.TileLayer('Stamen Toner').add_to(m)
folium.raster_layers.TileLayer('Stamen Watercolor').add_to(m)
folium.raster_layers.TileLayer('CartoDB Positron').add_to(m)
folium.raster_layers.TileLayer('CartoDB Dark_Matter').add_to(m)

client = openrouteservice.Client(key='5b3ce3597851110001cf62487257b6abfcd34bf3a78b7f8d098aff4a') # Specify your personal API key

for index, row in df.iterrows():
    c=[[row['from1'], row['from2']],
        [row['to1'], row['to2']]]
    r= client.directions(coordinates=c,profile='driving-car',format='geojson')
    folium.GeoJson(r, name=row['name']).add_to(m)# add geojson to map
    folium.Marker([row['to2'],row['to1']], popup=row['name'], icon=folium.Icon(color='purple'),tooltip='click').add_to(m)

icon_url='https://cdn4.iconfinder.com/data/icons/universal-signs-symbols/128/traffic-light-color-256.png'
for index, row in t.iterrows():
    folium.Marker(location=[row['latitude'], row['longitude']],popup=row['name'],icon = folium.features.CustomIcon(icon_url,icon_size=(30, 30))).add_to(m)


# add layer control to map (allows layer to be turned on or off)
folium.LayerControl().add_to(m)
Terminator().add_to(m) 
folium.LayerControl(position= 'topright', collapsed = False).add_to(m)
# display map
m.save("route.html")
# coordinates


import folium
import pandas

data = pandas.read_csv("./files/Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def colour_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="My Map")

# When iterate through two lists can use the zip function
for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius=6, weight=2, popup=folium.Popup(str(el) + "m", parse_html=True), fill_color=colour_producer(el), color='grey', fill=True, fill_opacity=0.7))

# Adding population data
# Can break lines in python when expression inside brackets
fg.add_child(folium.GeoJson(data=open('./files/world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 50000000 else 'red' }))

map.add_child(fg)
map.save("129-map.html")
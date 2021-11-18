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
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(str(el) + "m", parse_html=True), icon=folium.Icon(color=colour_producer(el))))

map.add_child(fg)
map.save("123-map.html")
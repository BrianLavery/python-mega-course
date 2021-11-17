import folium
map = folium.Map 
dir(folium)
# help(folium.Map)

# Pass location via coordinates
# This produces a map object inside Python memory
map1 = folium.Map(location=[80, -100])
map2 = folium.Map(location=[38.58, -99.09])
map3 = folium.Map(location=[38.58, -99.09], zoom_start=15)

# Need to access the map via some memory
map1.save("116-map1.html")
map2.save("116-map2.html")
map3.save("116-map3.html")
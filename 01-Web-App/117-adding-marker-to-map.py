import folium
map1 = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")

# Add objects to the map
map1.add_child(folium.Marker(location=[38.2, -99.1], popup="Hi I am a Marker!", icon=folium.Icon(color='green')))

map1.save("117-map-add_child-approach.html")

# Second approach he recommends - more organisation
map2 = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")

# Create a feature group
fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[38.2, -99.1], popup="Hi I am a Marker!", icon=folium.Icon(color='green')))

map2.add_child(fg)
map2.save("117-map-feature-group.html")
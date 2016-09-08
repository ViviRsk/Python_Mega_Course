import folium
import pandas

# store the data in a variable
df = pandas.read_csv("Volcanoes-USA.txt")

# we create an object
map = folium.Map(location=[45.372,-121.697],zoom_start=4,tiles='Stamen Terrain')

for lat,lon,name,elev in zip(df['LAT'],df['LON'],df['NAME'],df['ELEV']):
    # the section where we add markers
    map.simple_marker(location=[lat,lon],popup=name,marker_color='green' if elev in range(0,1000) else 'orange' if elev in range(1000,3000) else 'red')

# where we create the HTML map
map.create_map(path='test.html')

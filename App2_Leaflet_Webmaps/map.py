import folium
import pandas

# store the data in a variable
df = pandas.read_csv("Volcanoes-USA.txt")

# we create an object
map = folium.Map(location=[df['LAT'].mean(),df['LON'].mean()],zoom_start=6,tiles='Mapbox bright')


def color(elev):
    minimum = int(min(df['ELEV']))
    step = int((max(df['ELEV'])-min(df['ELEV']))/3)
    if elev in range(minimum,minimum+step):
        col = 'green'
    elif elev in range(minimum+step,minimum+step*2):
        col = 'orange'
    else:
        col = 'red'
    return col

fg = folium.FeatureGroup(name="Volcano Locations")

for lat,lon,name,elev in zip(df['LAT'],df['LON'],df['NAME'],df['ELEV']):
    # the section where we add markers
    fg.add_child(folium.Marker(location=[lat,lon],popup=name,icon=folium.Icon(color=color(elev),icon_color='green')))

map.add_child(fg)

map.add_child(folium.GeoJson(data=open('World_population.geojson'),
                             name='World Population',
                             style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005']<=10000000 else 'orange' if 10000000<x['properties']['POP2005']<20000000 else 'red'}))

map.add_child(folium.LayerControl())

# where we create the HTML map
map.save(outfile='test.html')

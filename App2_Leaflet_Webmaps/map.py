import folium
import pandas

# store the data in a variable
df = pandas.read_csv("Volcanoes-USA.txt")

# we create an object
map = folium.Map(location=[df['LAT'].mean(),df['LON'].mean()],zoom_start=6,tiles='Stamen Terrain')


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

for lat,lon,name,elev in zip(df['LAT'],df['LON'],df['NAME'],df['ELEV']):
    # the section where we add markers
    map.add_child(folium.Marker(location=[lat,lon],popup=name,icon=folium.Icon(color=color(elev),icon_color='green')))

# where we create the HTML map
map.save(outfile='test.html')

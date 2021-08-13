import folium
import pandas

html = """<h4>Volcano information:</h4>
Height : %s m
"""
data = pandas.read_csv("volcanoes.txt") #Read data file containing volcanoes information.
lat = list(data["LAT"]) #List of latitude data under the column LAT.
lon = list(data["LON"]) #List of longitude data under the column LON.
ele = list(data["ELEV"]) #List of elevation data under the column ELEV.

def color_mark(elevation):
    if elevation < 1500:
        return 'green'
    elif 1500 <= elevation < 2500:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location = [39,-111],zoom_start=6,tiles="Stamen Terrain") #Set initial position.

fgv = folium.FeatureGroup(name="Volcanoes") #Creating a feature group.

for lt,ln,el in zip(lat,lon,ele): #zip is used becouse there are more than one value to iterate.
    iframe = folium.IFrame(html=html % str(el), width=200, height=100)
    fgv.add_child(folium.Marker(location=[lt,ln], popup=folium.Popup(iframe),
    icon=folium.Icon(color=color_mark(el))))

fgp = folium.FeatureGroup(name="Population") #Creating a feature group.

fgp.add_child(folium.GeoJson(data = open("world.json","r",encoding = 'utf-8-sig').read(),
style_function= lambda x:{'fillColor':'green' if x['properties']['POP2005'] < 10000000 
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red' }))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl()) #Layer control should be added after adding feature group to the map.

map.save("Map1.html") #Save map data in html format.
import json 
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline 

# Explore the structure of the data.
filename = 'data/readable_month.json'
with open(filename) as f:
    all_eq_data = json.load(f)

# there is 158 total earthquakes recoreded 
title = all_eq_data['metadata'] ['title']
all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))


mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    hover_texts.append(eq_dict['properties']['title'])

# Map the earthquakes 
# change the size of the markers depending on the magnitude of the earth quake 
data = [{
    'type' : 'scattergeo',
    'lon' : lons,
    'lat' : lats,
    'text' : hover_texts,
    'marker' : {
       'colorscale' : 'Viridis',
       'reversescale' : True,
       'colorbar' : {'title' : 'Magnitude'},
    },
}]

my_layout = Layout(title=title)
try:
    fig = {'data': data, 'layout': my_layout}
except ValueError:
    print(f"Missing data")
else:
    offline.plot(fig, filename='global_earthquakes.html')
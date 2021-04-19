import csv

from datetime import datetime
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline 

num_rows = 10_000

filename = 'data/world_fires_1_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # get the dates, latitudes, longitudes, brightness  and infor about the fires
    dates, lats, lons, brightnesses, hover_texts = [], [], [], [],[]
    row_num = 0
    for row in reader:
        current_date = datetime.strptime(row[5],'%Y-%m-%d')
        brightness = float(row[2])
        label = f"{current_date.strftime('%m-%d-%y')} - {brightness}"

        dates.append(current_date)
        lats.append(row[0])
        lons.append(row[1])
        brightnesses.append(brightness)
        hover_texts.append(label)
        row_num += 1
        if row_num == num_rows:
            break

data = [{
    'type' : 'scattergeo',
    'lon' : lons,
    'lat' : lats,
    'text' : hover_texts,
    'marker' : {
        'size' : [brightness/20 for brightness in brightnesses],
        'color' : brightnesses,
        'colorscale' : 'YlOrRd',
        'reversescale' : True,
        'colorbar' : {'title' : 'Brightness'},
    },
}]

my_layout = Layout(title='Global fires')

fig = {'data': data, 'layout' : my_layout}

offline.plot(fig, filename='global_fires.html')
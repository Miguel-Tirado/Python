import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename ='data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, prcps = [], []
    for row in reader:
        currrent_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
           prcp = int(row[3])
        except ValueError:
            print(f"Missing data for {currrent_date}")
        else:
            dates.append(currrent_date)
            prcps.append(prcp)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, prcps, c='green')

title = 'Daily perciptation at Sitka rain forest'
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Percipitation ", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()

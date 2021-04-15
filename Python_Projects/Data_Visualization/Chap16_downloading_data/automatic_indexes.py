import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column in enumerate(header_row):
        #print(index, column)
        if column == 'TMAX':
            tmax_index = index
        if column == 'TMIN':
            tmin_index = index
        if column == 'DATE':
            date_index = index
    
    # Get dates and high and low temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
        stattion = row[1]
        try:      
            high = int(row[tmax_index])
            low = int(row[tmin_index])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# plot the high temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
# takes one x-argument (dates) and two y-arguments (highs,lows) to fill in between
ax.fill_between(dates, highs, lows, facecolor='blue', alpha = 0.1)

# format plot
title = f"Daily high and low temperatures - 2020\n{stattion}"
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
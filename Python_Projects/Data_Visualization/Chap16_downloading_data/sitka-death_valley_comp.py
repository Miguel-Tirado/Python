import csv
from datetime import datetime

import matplotlib.pyplot as plt

def get_weather_date(filename, dates, highs, lows):
    """Get the highs and lows from a data file"""
    with open(filename) as f :
        reader = csv.reader(f)
        header_row = next(reader)

        # dates, highs, lows = [], [], []
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            try:      
                high = int(row[5])
                low = int(row[6])
            except ValueError:
                print(f"Missing data for {current_date}")
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)

# get temperature data for sikta 
dates, highs, lows = [], [], []
get_weather_date('data/sitka_weather_2018_simple.csv', dates, highs, lows)
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.6)
ax.plot(dates, lows, c='blue', alpha=0.6)
# takes one x-argument (dates) and two y-arguments (highs,lows) to fill in between
ax.fill_between(dates, highs, lows, facecolor='blue', alpha = 0.15)

# get death valley data
dates, highs, lows = [], [], []
get_weather_date('data/death_valley_2018_simple.csv', dates, highs, lows)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.3)
ax.plot(dates, lows, c='blue', alpha=0.3)
# takes one x-argument (dates) and two y-arguments (highs,lows) to fill in between
ax.fill_between(dates, highs, lows, facecolor='blue', alpha = 0.05)

title = 'Daily high and low temperatures'
title += "\nSikta, AK and Death Valley, CA"
ax.set_title(title, fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
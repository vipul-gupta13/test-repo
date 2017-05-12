#!/usr/bin/python3.4

import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

dates=[]
y=[]
for line in open('avg_load.log','r'):
    split = line.strip().split('\t', 1)
    dates.append(split[0])
    y.append(split[1])
print dates
print y

#dates = ['01/02/1991','01/03/1991','01/04/1991']
x = [dt.datetime.strptime(d,'%m/%d/%Y').date() for d in dates]
#y = range(len(x)) # many thanks to Kyss Tao for setting me straight here
#y = [2,6,4]
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())
plt.plot(x,y)
plt.gcf().autofmt_xdate()

plt.savefig('smooth_plot12.png')

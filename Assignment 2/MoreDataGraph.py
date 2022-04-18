from logging import info
from requests import get
import matplotlib.pyplot as plt
from dateutil import parser
import matplotlib.dates as mdates



url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallmeasurements/1572018'
weather = get(url).json()

data = weather['items']
pages = 1
while 'next' in weather and pages < 9:
    url = weather['next']['$ref']
    print('Fetching {0}'.format(url))
    weather = get(url).json()
    data += weather['items']
    pages += 1

rainfall = [info['rainfall'] for info in data]

temperatures = [info['ambient_temp'] for info in data ]
timestamps = [parser.parse(info['reading_timestamp']) for info in data]
humittiy = [info['humidity'] for info in data ]

plt.plot(timestamps, temperatures, label= 'Temprature')
plt.plot(timestamps, rainfall, label= 'Rainfall')
plt.plot(timestamps, humittiy, label= 'humidity')
plt.ylabel('Rain fall  and Air Temperature')
plt.xlabel('Time')
plt.gcf().autofmt_xdate()
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%b-%d'))
plt.legend()
plt.show()


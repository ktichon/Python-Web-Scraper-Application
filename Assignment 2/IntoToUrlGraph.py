from urllib.request import DataHandler
from requests import get
import matplotlib.pyplot as plt
from dateutil import parser

url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations'
weather = get(url).json()

temperatures = []
recentlyUpdated = []


for info in weather['items']:
    specificURL = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallmeasurements/' + str(info["weather_stn_id"])
    station = get(specificURL).json()

    for info in station['items']:
        if '202' in  str(info['reading_timestamp']) and info['weather_stn_id'] not in recentlyUpdated:
            print("ID: " + str(info['weather_stn_id']) + "     Last Update " + str(info['reading_timestamp']))
            recentlyUpdated.append(info['weather_stn_id'])
        break

print(recentlyUpdated)

#same thing as loop above
#temperatures = [info['ambient_temp'] for info in weather['items'] ]














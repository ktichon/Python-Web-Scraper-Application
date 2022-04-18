from html.parser import HTMLParser
from html.entities import name2codepoint
from typing import Text
import urllib.request
import numbers
import datetime
from dateutil.relativedelta import relativedelta
import re
from dateutil.relativedelta import relativedelta

#if we ask for september 1996, but if we don't get that date, there is no data that means its the end

class WeatherScraper(HTMLParser):
    """Functions to parse html data to read and write weather data."""
    def __init__(self):
        HTMLParser.__init__(self)
        self.h1Date = False
        self.tBodyTag = False
        self.trTag = False
        self.tdTag = False
        self.thTag = False
        self.aTag = False
        self.goodRow = False
        self.weatherDict = {}
        self.valuesList = []
        self.position = 0
        self.date = ""
        self.url = None
        #print("" )


    def handle_starttag(self, tag, attrs):
            if tag == "h1":
                self.h1Date = True
            if tag == "tr":
                self.valuesList = []
                self.position = 0
                #print("Start tag:_____", tag)
                self.trTag = True
            if tag == "th":
                self.thTag = True
            if tag == "a" and self.thTag:
                self.aTag = True
                #print("TH :_____", tag)
                for attr , vals in attrs:
                    self.date = vals
                  #  print("     vals:", vals)
                   # print("            attr:", attr)
            if tag == "td":
                #print("Start tag:_______", tag)
                self.tdTag = True
                #self.position += 1



    def handle_endtag(self, tag):
            if tag == "h1":
                self.h1Date = False
            if tag == "tr":
                self.goodRow = False
                #self.valuesList.append("____________")
                #self.valuesList.append(self.date)

                self.trTag = False
                if(len(self.valuesList) == 3):
                    if(not(re.search('[a-zA-Z]', self.valuesList[0]) or  re.search('[a-zA-Z]', self.valuesList[1])  or  re.search('[a-zA-Z]', self.valuesList[2]))):
                            daily_temps = {"Max": self.valuesList[0], "Min": self.valuesList[1], "Mean": self.valuesList[2]}
                            self.weatherDict[self.date] = daily_temps
            if tag == "td":
                self.tdTag = False
            if tag == "th":
                stringStart = "/climate_data/hourly_data_e.html"
                if stringStart in self.date:
                    year = self.date[self.date.find("&Year=")+len("&Year="):self.date.rfind("&Month")]
                    month = self.date.partition("&Month=")[2]
                    day = self.date[self.date.find("&Day=")+len("&Day="):self.date.rfind("&Year=")]
                    self.date = "{}-{}-{}".format(year, month, day)
                self.thTag = False
            if tag == "a":
                self.aTag = False


    def handle_data(self, data):
        if self.h1Date:
            dateString = data.partition("Daily Data Report for ")[2] + "1 "
            self.date = datetime.strptime(dateString,)
        if self.thTag and data.isnumeric() :
            self.goodRow = True

        if  self.trTag:
            if  self.tdTag and self.goodRow:
                if self.position < 3:
                    self.valuesList.append(data)
                self.position += 1



    def print_dictionary(self):
        for k,v in self.weatherDict.items():
            print(k)
            print(v)
            print()



myparser = WeatherScraper()

siteUrl = 'https://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID=27174&timeframe=2&StartYear=1840&EndYear=2018&Day=25&Year=2021&Month=11'
yearFind = siteUrl[siteUrl.find("&Year=")+len("&Year="):siteUrl.rfind("&Month")]
monthFind = siteUrl.partition("&Month=")[2]
url = "https://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID=27174&timeframe=2&StartYear=1840&EndYear=2018&Day=1&Year={}&Month={}".format(yearFind, monthFind)
yearCount = int(yearFind)
monthCount = int(monthFind)


for x in range(1):
    url = "https://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID=27174&timeframe=2&StartYear=1840&EndYear=2018&Day=1&Year={}&Month={}".format(yearCount, monthCount)
    with urllib.request.urlopen(url) as response:
        html = str(response.read())
    myparser.feed(html)
    monthCount = monthCount - 1

monthCount = 12

for x in range(2):
    for x in range(12):
        url = "https://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID=27174&timeframe=2&StartYear=1840&EndYear=2018&Day=1&Year={}&Month={}".format(yearCount, monthCount)
        with urllib.request.urlopen(url) as response:
            html = str(response.read())
        myparser.feed(html)
        monthCount = monthCount - 1
    monthCount = 12
    with urllib.request.urlopen(url) as response:
        html = str(response.read())
    myparser.feed(html)
    yearCount = yearCount - 1

myparser.print_dictionary()


#with urllib.request.urlopen(url) as response:
    #html = str(response.read())

#myparser.feed(html)

#myparser.print_dictionary()

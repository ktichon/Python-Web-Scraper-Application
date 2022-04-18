from html.parser import HTMLParser
from html.entities import name2codepoint
from typing import Text
import urllib.request
import datetime
from dateutil.relativedelta import relativedelta

from db_operations import DBOperations



#if we ask for september 1996, but if we don't get that date, there is no data that means its the end

class WeatherScraper(HTMLParser):
    """Functions to parse html data to read and write weather data."""
    def __init__(self, url):
        HTMLParser.__init__(self)



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



    def handle_starttag(self, tag, attrs):
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
            if tag == "tr":
                self.goodRow = False
                #self.valuesList.append("____________")
                #self.valuesList.append(self.date)

                self.trTag = False
                if(len(self.valuesList) == 3):
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
        if self.thTag and data.isnumeric() :
            self.goodRow = True

        if  self.trTag:
            if  self.tdTag and self.goodRow:
                if self.position < 3 and data.isnumeric():
                    self.valuesList.append(data)
                self.position += 1



    def print_dictionary(self):
        for k,v in self.weatherDict.items():
            print(k)
            print(v)
            print()

        print(str(len(self.weatherDict)))
    def get_dictionary(self):
        return self.weatherDict


myparser = WeatherScraper()

with urllib.request.urlopen('https://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID=27174&timeframe=2&StartYear=1840&EndYear=2018&Day=1&Year=2018&Month=5') as response:
    html = str(response.read())

myparser.feed(html)

myparser.print_dictionary()
myDatabase = DBOperations(myparser.get_dictionary)
myDatabase.initialize_db()

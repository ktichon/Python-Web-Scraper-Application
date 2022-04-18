from html import parser
from html.parser import HTMLParser
from html.entities import name2codepoint
from typing import Text
import urllib.request
import numbers
import re
import datetime
import dateutil.relativedelta
#if we ask for september 1996, but if we don't get that date, there is no data that means its the end
#https://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID=27174&timeframe=2&StartYear=1840&EndYear=2018&Day=25&Year=2021&Month=11
class WeatherScraper():
    BASEURL = "https://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID=27174&timeframe=2&StartYear=1840"

    """Runs the WeatherParser class for each month avalible"""
    def __init__(self):
        """Initialises the varibles"""
        self.todayDate = datetime.date.today()
        self.unChangingURL = self.BASEURL + self.todayDate.strftime("&EndYear=%Y") + "&Day=1"
        self.lastYearMonth = None

    def parse_website(self, lastYearMonth):
        self.lastYearMonth = lastYearMonth
        """Parses the website in a loop"""
        urlDate = self.todayDate
        monthsFromToday = 0
        weatherParser = WeatherParser()
        while( urlDate.strftime('%#m/%Y') != self.lastYearMonth ):

            urlDate = self.todayDate + dateutil.relativedelta.relativedelta(months=monthsFromToday)
            print("Fetching data from " + urlDate.strftime("%B %Y"))

            siteUrl = self.unChangingURL + urlDate.strftime("&Year=%Y&Month=%#m")
            with urllib.request.urlopen(siteUrl) as response:
                html = str(response.read())
            weatherParser.feed(html)
            monthsFromToday -= 1

        return weatherParser.weatherDict

class WeatherParser(HTMLParser):
    """Functions to parse html data to read and write weather data."""
    def __init__(self):
        HTMLParser.__init__(self)
        self.tBodyTag = False
        self.trTag = False
        self.tdTag = False
        self.thTag = False
        self.abbrTag = False
        self.goodRow = False
        self.weatherDict = {}
        self.valuesList = []
        self.position = 0
        self.date = None
        #print("" )

    def handle_starttag(self, tag, attrs):
            if tag == "tbody":
                self.tBodyTag = True
            if tag == "tr":
                self.valuesList = []
                self.position = 0
                #print("Start tag:_____", tag)
                self.trTag = True
            if tag == "th":
                self.thTag = True
            if tag == "abbr" and self.thTag and self.tBodyTag:
                self.abbrTag = True
                #print("TH :_____", tag)
                for attr , vals in attrs:
                    self.date = vals





                    #print("     vals:", vals)
                    #print("            attr:", attr)
            if tag == "td":
                #print("Start tag:_______", tag)
                self.tdTag = True
                #self.position += 1



    def handle_endtag(self, tag):
            if tag == "tbody":
                self.tBodyTag = False
            if tag == "tr":
                self.goodRow = False
                #self.valuesList.append("____________")
                #self.valuesList.append(self.date)

                self.trTag = False
                if(len(self.valuesList) == 3):
                    if(not(re.search('[a-zA-Z]', self.valuesList[0]) or  re.search('[a-zA-Z]', self.valuesList[1])  or  re.search('[a-zA-Z]', self.valuesList[2]))):
                            daily_temps = {"Max": self.valuesList[0], "Min": self.valuesList[1], "Mean": self.valuesList[2]}
                            dateObject = datetime.datetime.strptime(self.date, "%B %d, %Y")
                            self.weatherDict[dateObject.strftime("%Y-%#m-%d")] = daily_temps
            if tag == "td":
                self.tdTag = False
            if tag == "th":

                   #self.date = "{}-{}-{}".format(year, month, day)
                self.thTag = False
            if tag == "abbr":
                self.abbrTag = False


    def handle_data(self, data):
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





siteUrl = 'https://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID=27174&timeframe=2&StartYear=1840&EndYear=2018&Day=25&Year=2021&Month=11'
myparser = WeatherScraper()
#dictionary = myparser.parse_website('1/2015')
#print("# of dates :" +  str(len(dictionary)))


# with urllib.request.urlopen(siteUrl) as response:
#     html = str(response.read())

# myparser.feed(html)

# myparser.print_dictionary()

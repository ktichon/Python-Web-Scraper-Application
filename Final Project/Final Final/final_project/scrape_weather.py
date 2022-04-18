"""
Scrapes weather data from climate.weather.gc.ca website.
"""
from html.parser import HTMLParser
import urllib.request
import logging
import re
import datetime
import dateutil.relativedelta


class WeatherScraper():
    """Scrapes weather from climate.weather.gc.ca until the date provided."""

    logger = logging.getLogger("main." + __name__)

    BASEURL = "https://climate.weather.gc.ca/climate_data/"\
              "daily_data_e.html?StationID=27174&timeframe=2&StartYear=1840"

    def __init__(self):
        """Initializes the varibles"""
        try:
            self.todays_date = datetime.date.today()
            self.unchanging_url = self.BASEURL + self.todays_date.strftime("&EndYear=%Y") + "&Day=1"
            self.last_year_month = None
        except Exception as error:
            self.logger.error("WeatherScraper/init: %s", error)

    def parse_website(self, date_input):
        """Parses the website in a loop until date provided by user or end of data is reached."""
        try:
            self.last_year_month = date_input
            url_date = self.todays_date
            months_from_today = 0
            weather_parser = WeatherParser()
            while url_date.strftime('%#m/%Y') != self.last_year_month:

                url_date = self.todays_date + dateutil.relativedelta.relativedelta(months=months_from_today)

                site_url = self.unchanging_url + url_date.strftime("&Year=%Y&Month=%#m")
                with urllib.request.urlopen(site_url) as response:
                    html = str(response.read())
                weather_parser.feed(html)
                months_from_today -= 1

                print("Fetching data from " + url_date.strftime("%B %Y"))

                if str(url_date.strftime("%m")) != str(weather_parser.current_month()):
                    print(f'Reached end of data. {url_date.strftime("%B %Y")} is not available.')
                    break
        except Exception as error:
            self.logger.error("WeatherScraper/parse_website: %s", error)

        return weather_parser.weather_dict


class WeatherParser(HTMLParser):
    """Functions to parse html data to read and write weather data."""

    def __init__(self):
        """Initialises the varibles"""
        try:
            HTMLParser.__init__(self)
            self.tbody_tag = False
            self.tr_tag = False
            self.td_tag = False
            self.th_tag = False
            self.abbr_tag = False
            self.good_row = False
            self.weather_dict = {}
            self.values_list = []
            self.position = 0
            self.date = None
            self.current_year_value = 0
            self.current_month_value = 0
            self.h1_tag = False
            self.h1date = None
        except Exception as error:
            self.logger.error("WeatherParser/init: %s", error)


    def handle_starttag(self, tag, attrs):
        try:
            if tag == "h1":
                self.h1_tag = True
            if tag == "tbody":
                self.tbody_tag = True
            if tag == "tr":
                self.values_list = []
                self.position = 0
                self.tr_tag = True
            if tag == "th":
                self.th_tag = True
            if tag == "abbr" and self.th_tag and self.tbody_tag:
                self.abbr_tag = True
                for attr , vals in attrs:
                    self.date = vals
            if tag == "td":
                self.td_tag = True
        except Exception as error:
            self.logger.error("WeatherParser/handle_starttag: %s", error)

    def handle_endtag(self, tag):
        try:
            if tag == "h1":
                self.h1_tag = False
                month_text = self.h1date[self.h1date.find("for ")+len("for "):self.h1date.rfind(" ")]
                self.current_year_value =  self.h1date[-4:]
                datetime_month = datetime.datetime.strptime(month_text, "%B")
                self.current_month_value = datetime_month.month
            if tag == "tbody":
                self.tbody_tag = False
            if tag == "tr":
                self.good_row = False
                self.tr_tag = False
            if len(self.values_list) == 3:
                if not(re.search('[a-zA-Z]', self.values_list[0]) or
                   re.search('[a-zA-Z]', self.values_list[1])  or
                   re.search('[a-zA-Z]', self.values_list[2])):
                    daily_temps = {"Max": self.values_list[0],
                                   "Min": self.values_list[1],
                                   "Mean": self.values_list[2]}
                    parsed_date = datetime.datetime.strptime(self.date, "%B %d, %Y")
                    self.weather_dict[parsed_date.strftime("%Y-%m-%d")] = daily_temps
            if tag == "td":
                self.td_tag = False
            if tag == "th":
                self.th_tag = False
            if tag == "abbr":
                self.abbr_tag = False
        except Exception as error:
            self.logger.error("WeatherParser/handle_endtag: %s", error)

    def handle_data(self, data):
        try:
            if self.h1_tag:
                self.h1date = data
            if self.th_tag and data.isnumeric() :
                self.good_row = True
            if  self.tr_tag:
                if  self.td_tag and self.good_row:
                    if self.position < 3:
                        self.values_list.append(data)
                    self.position += 1
        except Exception as error:
            self.logger.error("WeatherParser/handle_data: %s", error)

    def print_dictionary(self):
        """Prints out all of the date values in the weather dictionary."""
        try:
            for key,value in self.weather_dict.items():
                print(key)
                print(value)
                print()
        except Exception as error:
            self.logger.error("WeatherParser/print_dictionary: %s", error)

    def current_year(self):
        """Returns the current year based on the h1 tag on the website."""
        return self.current_year_value

    def current_month(self):
        """Returns the current month based on the h1 tag on the website."""
        return '{:02}'.format(self.current_month_value)

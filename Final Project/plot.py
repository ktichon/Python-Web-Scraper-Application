from email.errors import MalformedHeaderDefect
from requests import get
import matplotlib.pyplot as plt
from dateutil import parser
from scrape_weather import WeatherScraper
from datetime import datetime
from decimal import Decimal
import numpy as np
from db_operations import DBOperations
import statistics
# from weather_processor import WeatherProcessor

class PlotOperations:

  # def __init__(self):
  #   self.box_data = None

  def box_plot(self, box_input):

    fetch_box_data = box_input

    years = []

    for keys, values in fetch_box_data.items():
      years.append(keys)

    plt.xlabel("Month")
    plt.ylabel("Temperature (Celcius)")
    plt.title(f"Montly Temperature Distribution for {years[0]} to {years[1]}")

    new_dict = {}
    for id, info in fetch_box_data.items():
      month = 0
      for key in info:
        month = key
        if key not in new_dict:
          new_dict.update({key: []})
        temp_list = []
        for x in info[key]:
          temp_list.append(float(x[1]))
        new_dict[month].extend(temp_list)

    keys = new_dict.keys()
    values = new_dict.values()

    plt.boxplot(values)
    plt.xticks(range(1, len(keys) + 1), keys)
    plt.show()


  def line_plot(self, line_input):

    fetch_line_data = line_input

    plt.xlabel("Date")
    plt.ylabel("Temperature (Celcius)")

    line_dict = {}
    input_month = None
    input_year = None
    for id, info in fetch_line_data.items():
      for key in info:
        for x in info[key]:
          date_object = datetime.strptime(x[0], "%Y-%m-%d")
          date_value = str(date_object.day)
          input_month = str(date_object.month)
          input_year = str(date_object.year)
          line_dict.update({date_value : float(x[1])})

    values = line_dict.values()
    plt.title(f"Daily Temperature Distribution for {input_month} - {input_year}")

    plt.plot(values)
    plt.show()

# testbox = PlotOperations
# testbox.box_plot()
# testbox.line_plot()


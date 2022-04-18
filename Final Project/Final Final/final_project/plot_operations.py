"""
Displays weather data from climate.weather.gc.ca website in a box or line plot.
"""
from datetime import datetime
import logging
import matplotlib.pyplot as plt


class PlotOperations:
    """Contains box plot and line plot methods to plot weather data."""

    logger = logging.getLogger("main." + __name__)

    def box_plot(self, box_input):
        """Takes in a date dictionary and displays weather between year dates on a box plot."""
        try:
            fetch_box_data = box_input
            years = []
            for keys, values in fetch_box_data.items():
                years.append(keys)
        except Exception as error:
            self.logger.error("PlotOperations/box_plot/input: %s", error)

        try:
            new_dict = {}
            for year_id, info in fetch_box_data.items():
                month = 0
                for key in info:
                    month = key
                    if key not in new_dict:
                        new_dict.update({key: []})
                    temp_list = []
                    for temps in info[key]:
                        temp_list.append(float(temps[1]))
                    new_dict[month].extend(temp_list)

            keys = new_dict.keys()
            values = new_dict.values()
        except Exception as error:
            self.logger.error("PlotOperations/box_plot/dictionary: %s", error)

        try:
            plt.xlabel("Month")
            plt.ylabel("Temperature (Celcius)")
            plt.title(f"Montly Temperature Distribution for {years[0]} to {years[len(years) -1]}")

            plt.boxplot(values)
            plt.xticks(range(1, len(keys) + 1), keys)
            plt.show()
        except Exception as error:
            self.logger.error("PlotOperations/box_plot/plotting: %s", error)


    def line_plot(self, line_input):
        """Takes in a date dictionary and displays weather for the month and year in a line plot."""

        try:
            fetch_line_data = line_input

            line_dict = {}
            input_month = None
            input_year = None
            for year_id, info in fetch_line_data.items():
                for key in info:
                    for date in info[key]:
                        date_object = datetime.strptime(date[0], "%Y-%m-%d")
                        date_value = str(date_object.day)
                        input_month = str(date_object.month)
                        input_year = str(date_object.year)
                        line_dict.update({date_value : float(date[1])})

            values = line_dict.values()
        except Exception as error:
            self.logger.error("PlotOperations/line_plot/dictionary: %s", error)

        try:
            plt.xlabel("Date")
            plt.ylabel("Temperature (Celcius)")
            plt.title(f"Daily Temperature Distribution for {input_month} - {input_year}")
            plt.plot(values)
            plt.show()
        except Exception as error:
            self.logger.error("PlotOperations/line_plot/plotting: %s", error)


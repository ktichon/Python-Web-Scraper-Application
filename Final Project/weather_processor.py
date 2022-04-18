"""UI interfaces for the final project"""

import datetime
import logging
import logging.handlers
from db_operations import DBOperations
from scrape_weather import WeatherScraper
from plot import PlotOperations

class WeatherProcessor:
    """Main class that calls the other classes based on user input"""

    logger = logging.getLogger("main." + __name__)

    def __init__(self):
        """Initializes the classes that will be used in the application"""
        try:
            self.main_menu = { 1: "Update Weather Data",
                            2: "Download Full Set of Weather Data",
                            3: "Generate Box Plot",
                            4: "Generate Line Plot",
                            5: "Exit"}
            self.todays_date = datetime.date.today()
            self.database = DBOperations()
            self.database.initialize_db()
            self.weather_scraper = WeatherScraper()
            self.plot_operation = PlotOperations()
        except Exception as error:
            self.logger.error("WeatherProcessor/init: %s", error)
            self.todays_date = None
            self.database = None
            self.weather_scraper = None



    def start(self):
        """ Prompts the user for user input, and then call the respected method """
        try:
            print("Weather Processor App")
            while True:
                try:
                    for key,value in self.main_menu.items():
                        try:
                            print(key, ")-----", value)
                        except Exception as error:
                            self.logger.error("WeatherProcessor/start/menu/print option: %s", error)
                    selected = input("Please enter the # of the choice you would like to run: ")
                    if selected == "1":
                        self.update_weather()
                    elif selected == "2":
                        self.download_full()
                    elif selected == "3":
                        self.generate_box_plot()
                    elif selected == "4":
                        self.generate_line_plot()
                    elif selected in ("5", "exit"):
                        break
                    else:
                        print("Invaild value")
                except Exception as error:
                    self.logger.error("WeatherProcessor/start/menu loop: %s", error)
        except Exception as error:
            self.logger.error("WeatherProcessor/start: %s", error)

    def update_weather(self):
        """Updates the database to current date"""

        try:
            print("Updating Weather")
            last_date = self.database.get_most_recent()
            print("Fetching weather from " + last_date + " to today ... ")
            split_date = last_date.split('-')
            formated_date = split_date[1] + '/' + split_date[0]
            weather_data = self.weather_scraper.parse_website(formated_date)
            print("Saving new Data")
            self.database.save_data(weather_data)
            print("All up to date!")
        except Exception as error:
            self.logger.error('WeatherProcessor/Update Weather: %s', error)


    def download_full(self):
        """Deletes all data and redownloads ll infromation from weather_scraper.py"""

        try:
            print("Deleting Saved Data")
            self.database.purge_data()
            print("Fetching new Data")
            weather_data = self.weather_scraper.parse_website('1/1960')
            print("Saving new data")
            self.database.save_data(weather_data)
        except Exception as error:
            self.logger.error('WeatherProcessor/Download_full: %s', error)

    def generate_box_plot(self):
        """Calls the box plot method, passing in user inputed start/end year"""
        try:
            start_year = None
            end_year = None
            while True:
                try:
                    start_year = input("Please enter the Start Year:   ")
                    try:
                        if int(start_year) <= int(self.todays_date.year):
                            break

                        print("""Please enter a vaild year.
                        This app doen't have access to a time machine""")
                    except Exception:
                        print('Invaild Value')
                except Exception as error:
                    self.logger.error("WeatherProcssor/Generate_Box_Plot/Get Start Year: %s", error)
            while True:
                try:
                    end_year = input("Please enter the End Year:   ")
                    try:
                        if int(end_year) <= int(self.todays_date.year) and end_year > start_year:
                            break
                        print("Please enter a vaild year. That isn't how liner time works")
                    except Exception:
                        print('Invaild Value')
                except Exception as error:
                    self.logger.error("WeatherProcssor/Generate_Box_Plot/Get End Year: %s", error)
            print("Loading dates from " + start_year + " to " + end_year + " ... ")
            box_plots = self.database.fetch_data(int(start_year), int(end_year))
            print("Creating box plot ... ")
            self.plot_operation.box_plot(box_plots)
        except Exception as error:
            self.logger.error("WeatherProcssor/Generate_Box_Plot: %s", error)





    def generate_line_plot(self):
        """Calls the line plot method, passing in user inputed year and month"""
        try:
            year = None
            month = None
            while True:
                try:
                    year = input("Please enter the Year:   ")
                    try:
                        if int(year) <= int(self.todays_date.year):
                            break
                        print("""Please enter a vaild year.
                             This app doen't have access to a time machine""")
                    except Exception:
                        print('Invaild Value')
                except Exception as error:
                    self.logger.error("WeatherProcssor/Generate_Line_Plot/Get Year: %s", error)
            while True:
                try:
                    month = input("Please enter the month as a number:   ")
                    try:
                        if int(month) <= 12 :
                            break
                        print("Please enter a number between 1-12 to represent the month.")
                    except Exception:
                        print('Invaild Value')
                except Exception as error:
                    self.logger.error("WeatherProcssor/Generate_Line_Plot/Get Month: %s", error)
            print("Loading dates from " + month + "/" + year + " ... ")
            line_plot = self.database.fetch_data(int(year), int(year), int(month))
            print("Creating line plot ... ")
            self.plot_operation.line_plot(line_plot)
        except Exception as error:
            self.logger.error("WeatherProcessor/Generate_line_plot %s", error)



if __name__ == "__main__":
    logger = logging.getLogger("main")
    logger.setLevel(logging.DEBUG)
    file_handler = logging.handlers.RotatingFileHandler(filename="weather_processor.log",
                                                  maxBytes=10485760,
                                                  backupCount=10)
    file_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.info("Main Application WeatherProcessor Started")


    user_int= WeatherProcessor()
    user_int.start()

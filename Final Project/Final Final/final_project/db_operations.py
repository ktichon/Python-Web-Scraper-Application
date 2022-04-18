"""
Stores data from the weather dictionary to a SQLite file
"""
import calendar
import logging
from scrape_weather import WeatherScraper


from dbcm import DBCM

class DBOperations:
    """Store and retire weather data"""

    logger = logging.getLogger("main." + __name__)

    def __init__(self):
        """Initializes varibles that will be used throught the class"""
        self.database = "weatherData.sqlite"


    def initialize_db(self):
        """Initializes the database"""
        with DBCM(self.database) as cursor:
            try:
                cursor.execute("""create table if not exists weather
                (id integer primary key autoincrement not null,
                sample_date text unique,
                location text,
                min_temp real,
                max_temp real,
                avg_temp);""")
            except Exception as error:
                self.logger.error('DBOperations/initialize_db: %s', error)

    def purge_data(self):
        """Removes all data from the db"""
        with DBCM(self.database) as cursor:
            try:
                cursor.execute("""DELETE FROM weather;""")
            except Exception as error:
                self.logger.error('DBOperations/purge_data: %s', error)

    def fetch_data(self, start_year, end_year, selected_month = None):
        """Fetches data from start year to end year, or from month/year if selected"""
        try:
            loop_year = start_year
            sql = """SELECT sample_date, avg_temp
            FROM weather WHERE sample_date LIKE ?
             ORDER BY sample_date ASC """
            months = range(1, 13)
            if selected_month is not None:
                months = range(selected_month, selected_month + 1)
            year_data = {}

            #my attempt at a do while loop
            while True:
                try:
                    print("Loading data from " + str(loop_year))
                    month_data = {}
                    for month in months:
                        try:
                            print("     " + calendar.month_name[month])
                            with DBCM(self.database) as cursor:
                                month_year = str(loop_year) + "-" + str(month).zfill(2) + "%"
                                month_data[month] = cursor.execute(sql, (month_year,)).fetchall()

                        except Exception as error:
                            self.logger.error("""DBOperations/fetch_data
                            /while year/while month: %s""", error)
                    year_data[loop_year] = month_data

                    #breakes out of infinte loop
                    if loop_year >= end_year:
                        break
                    loop_year += 1
                except Exception as error:
                    self.logger.error('DBOperations/fetch_data/while year: %s', error)
        except Exception as error:
            self.logger.error('DBOperations/fetch_data/: %s', error)

        #Returns a dictionary of years
        #that point to a dictionary of months
        # that are a list of tuples
        return year_data

    def get_most_recent(self):
        """Gets the most recent date in the database"""
        most_recent = None
        try:
            sql = """SELECT sample_date
            FROM weather ORDER BY sample_date DESC"""
            with DBCM(self.database) as cursor:
                first_tuple = cursor.execute(sql).fetchone()
                if first_tuple:
                    most_recent = first_tuple[0]
        except Exception as error:
            self.logger.error('DBOperations/get_most_recent: %s', error)
        return most_recent

    def save_data(self, weather_dictionary):
        """Saves a dictionary of weather values to the database"""
        try:
            insert_sql =  """INSERT OR IGNORE into weather
            (sample_date, location, min_temp, max_temp, avg_temp)
            values (?, ?, ?, ?, ?)"""

            data = []
            for key,value in weather_dictionary.items():
                try:
                    data.append((key, 'Winnipeg MB', value['Min'], value['Max'], value['Mean'],))
                except Exception as error:
                    self.logger.error("DBOperations/save_data/append data to list %s", error)
            with DBCM(self.database) as cursor:
                try:
                    before_insert = cursor.execute("SELECT COUNT() FROM weather").fetchone()[0]
                    cursor.executemany(insert_sql, data)
                    after_insert = cursor.execute("SELECT COUNT() FROM weather").fetchone()[0]
                    print("Inserted " + str(after_insert - before_insert) + " new rows")
                except Exception as error:
                    self.logger.error('DBOperations/save_data/Insert Into database: %s', error)
        except Exception as error:
            self.logger.errorint('DBOperations/save_data: %s', error)


if __name__ == "__main__":
    database = DBOperations()
    database.initialize_db()
    database.purge_data()

    myparser = WeatherScraper()
    dictionary = myparser.parse_website('1/2019')
    database.save_data(dictionary)
    fetch_box_data = database.fetch_data(2020, 2021)
    fetch_line_data = database.fetch_data(2021,2021, 7)
    print(fetch_line_data)

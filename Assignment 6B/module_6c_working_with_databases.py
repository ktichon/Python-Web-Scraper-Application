from os import waitpid
import sqlite3
from sqlite3.dbapi2 import Timestamp

class DataBase:
  """Context Manger to use database"""
  def __init__(self, databaseName):
    """Initializes the database and cursor"""
    self.databaseName = databaseName
    self.connect = None
    self.cursor = None

  def __enter__(self):
    """Returns the cursor"""
    self.connect = sqlite3.connect(self.databaseName)
    self.cursor = self.connect.cursor()
    return self.cursor

  def __exit__(self, exc_type, exc_value, exc_trace):
    """Closes the database"""
    self.connect.commit()
    self.cursor.close()
    self.connect.close()

class DBOperations:
    """Adding data to a database"""
    def __init__(self, database):
        self.database = database

    def create_table(self):
        """Create the weather sql table"""
        with DataBase(self.database) as d:
            try:
              d.execute("""create table if not exists samples (id integer primary key autoincrement not null, date text not null, location text not null,min_temp real not null,max_temp real not null, avg_temp real not null);""")
            except Exception as e:
              print('create_table:', e)

    def add_dictionary(self, dictionary):
        """Adds a dictionary of values to the database"""
        sql= """insert into samples (date, location, min_temp, max_temp, avg_temp) values (?, ?, ?, ?, ?)"""

        for name,row in dictionary.items():
            with DataBase(self.database) as d:
              data = (name, 'Winnipeg MB', row['Max'], row['Min'], row['Mean'])
              d.execute(sql, data)
    def print_table(self):
        """Prints all items in table"""
        with DataBase(self.database) as d:
            for row in d.execute("select * from samples"):
                print(row)

test = DBOperations("weather.sqlite")
weather = {"2018-06-01": {"Max": 12.0, "Min": 5.6, "Mean": 7.1},
                   "2018-06-02": {"Max": 22.2, "Min": 11.1, "Mean": 15.5},
                  "2018-06-03": {"Max": 31.3, "Min": 29.9, "Mean": 30.0}}
try:
  test.create_table()
  test.add_dictionary(weather)
  test.print_table()
except Exception as e:
  print('Error:', e)
print("Testing complete")

# with DataBase("weather.sqlite") as d:
#   d.execute("""drop table samples;""")







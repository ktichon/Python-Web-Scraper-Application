"""Module 4C"""
class MyMath:
    """Runs math calculations"""
    def __init__(self):
        """Instantiates an empty list to be used for the calculations in this class"""
        try:
            self.num_list = []
        except Exception as e:
          print("MyMath:__init__: error: ", e)


    def cal_average(self):
        """Calculats the average of a list of numbers"""

        try:
            num_sum = 0
            avg = 0
            if len(self.num_list) == 0:
                raise ZeroDivisionError("num_list is empty")
            for num in self.num_list:
                try:
                    num_sum = num_sum + num
                except Exception as e:
                    print("MyMath:cal_average:loop: error: ", e)
            avg = num_sum/len(self.num_list)
        except Exception as e:
            print("MyMath:cal_average: error: ", e)
            avg = 0
        return avg


    def standard_deviation(self):
        """Calculates the standard deviation of a list"""
        try:
            num_sum = 0
            stddev = 0
            avg = self.cal_average()
            if len(self.num_list) == 1:
                raise ZeroDivisionError("num_list length has to be greater than 1")
            for num in self.num_list:
                try:
                    num_sum = num_sum + (num - avg) ** 2
                except Exception as e:
                    print("MyMath:standard_deviation:loop: error: ", e)
            stddev =  (num_sum / (len(self.num_list) - 1)) ** 0.5
        except Exception as e:
            print("MyMath:standard_deviation: error: ", e)
            stddev = 0
        return stddev




    def max_number(self):
        """Gets the highest number in list"""
        try:
            if not self.num_list:
                raise ValueError("num_list is empty")
            max_num = max(self.num_list)
        except Exception as  e:
            print("MyMath:max_number: error: ", e)
            max_num = 0
        return max_num
try:
    math = MyMath()
    while True:
        try:
            myinput= input("Enter  data point or 'done' when finished:")

            if str(myinput) == "done":
                break

            math.num_list.append(float(myinput))
            print(myinput)
        except Exception as e:
            print("Output:user input error:", e)

    print("Max: ", math.max_number())
    print("Average: ", math.cal_average())
    print("Standard deviation: ", math.standard_deviation())
except Exception as e:
    print("Output error:", e)

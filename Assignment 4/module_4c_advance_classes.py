"""Module 4C"""
class MyMath:
    """Runs math calculations"""
    def __init__(self):
        """Instantiates an empty list to be used for the calculations in this class"""
        self.num_list = []


    def cal_average(self):
        """Calculats the average of a list of numbers"""
        num_sum = 0
        for num in self.num_list:
            num_sum = num_sum + num
        avg = num_sum/len(self.num_list)
        return avg


    def standard_deviation(self):
        """Calculates the standard deviation of a list"""
        num_sum = 0
        avg = self.cal_average()
        for num in self.num_list:
            num_sum = num_sum + (num - avg) ** 2
        return (num_sum / (len(self.num_list) - 1)) ** 0.5

    def max_number(self):
        """Gets the highest number in list"""
        return max(self.num_list)

math = MyMath()
while True:
    myinput= input("Enter  data point or 'done' when finished:")

    if str(myinput) == "done":
        break

    math.num_list.append(float(myinput))
    print(myinput)

print("Max: ", math.max_number())
print("Average: ", math.cal_average())
print("Standard deviation: ", math.standard_deviation())

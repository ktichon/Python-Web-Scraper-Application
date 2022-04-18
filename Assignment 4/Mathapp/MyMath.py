class MyMath:
  """Runs math calculations"""
  def __init__(self):
      """Instantiates an empty list to be used for the calculations in this class"""
      self.num_list = []


  def cal_average(self):
    """Calculats the average of a list of numbers"""
    sum = 0
    for num in self.num_list:
      sum = sum + num
    avg = sum/len(self.num_list)
    return avg


  def standard_Deviation(self):
    """Calculates the standard deviation of a list"""
    sums = 0
    avg = self.cal_average()
    for num in self.num_list:
      sums = sums + (num - avg) ** 2
    return (sums / (len(self.num_list) - 1)) ** 0.5

  def max_number(self):
    """Gets the highest number in list"""
    return max(self.num_list)
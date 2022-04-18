def cal_average(numlist):
  """Calculats the average of a list of numbers"""
  sum = 0
  for num in numlist:
    sum = sum + num
  avg = sum/len(numlist)
  return avg


def standard_Deviation(numlist):
  """Calculates the standard deviation of a list"""
  sums = 0
  avg = cal_average(numlist)
  for num in numlist:
    sums = sums + (num - avg) ** 2
  return (sums / (len(numlist) - 1)) ** 0.5

numLists = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(standard_Deviation(numLists))
def cal_average(numlist):
  """Calculats the average of a list of numbers"""
  sum = 0
  for num in numlist:
    sum = sum + num
  avg = sum/len(numlist)
  return avg

ouroutput = "Path to follow from Start [1, 1] to Exit [7, 11] - 27 steps:\n[1, 1]\n[2, 1]\n[3, 1]\n[4, 1]\n[5, 1]\n[5, 2]\n[5, 3]\n[6, 3]\n[7, 3]\n[7, 2]\n[7, 1]\n[8, 1]\n[9, 1]\n[9, 2]\n[9, 3]\n[9, 4]\n[9, 5]\n[9, 6]\n[9, 7]\n[8, 7]\n[7, 7]\n[7, 8]\n[7, 9]\n[6, 9]\n[6, 10]\n[6, 11]\n[7, 11]\n\n\nWWWWWWWWWWWWW\nW.    W     W\nW.WWW W WWW W\nW.W       W W\nW.WWWWWWW WWW\nW...WVVVW   W\nWWW.WVWWW...W\nW...VVW...WEW\nW.WWWWW.WVWWW\nW.......WVVVW\nWWWWWWWWWWWWW"
testoutput = "Path to follow from Start [1, 1] to Exit [7, 11] - 27 steps:\n[1, 1]\n[2, 1]\n[3, 1]\n[4, 1]\n[5, 1]\n[5, 2]\n[5, 3]\n[6, 3]\n[7, 3]\n[7, 2]\n[7, 1]\n[8, 1]\n[9, 1]\n[9, 2]\n[9, 3]\n[9, 4]\n[9, 5]\n[9, 6]\n[9, 7]\n[8, 7]\n[7, 7]\n[7, 8]\n[7, 9]\n[6, 9]\n[6, 10]\n[6, 11]\n[7, 11]\n" + "WWWWWWWWWWWWW\nW.    W     W\nW.WWW W WWW W\nW.W       W W\nW.WWWWWWW WWW\nW...WVVVW   W\nWWW.WVWWW...W\nW...VVW...WEW\nW.WWWWW.WVWWW\nW.......WVVVW\nWWWWWWWWWWWWW"
print(ouroutput)
print(testoutput)
print(len(ouroutput))
print(len(testoutput))


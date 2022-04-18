import csv

def csv_reader(filename):
    """Reads csv filea and get changed list"""
    modifiedList = []
    with open(filename) as csvdata:
      for line in csv.DictReader(csvdata):
        for k, v in line.items():
          line[k] = float(v) * 2

        modifiedList.append(line)
    return modifiedList

def csv_writer(modifiedList, newFileName):
  """Writes a csv file based off a list"""
  with open(newFileName, 'w', newline='') as newFile:
    filewriter = csv.DictWriter(newFile, fieldnames=modifiedList[0].keys())
    filewriter.writeheader()
    for row in modifiedList:
      filewriter.writerow(row)

file = 'csv_file.csv'
print(csv_reader(file))
csv_writer(csv_reader(file), 'newfile.csv')


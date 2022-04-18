def replace_aqua(textfile):
    stringFile = ""
    with open('text_document.txt', 'r') as file:
      for line in file:
        stringline = line
        if "Aqua" in line:
          stringline = "Azure #007fff\n"
        stringFile += stringline
    return stringFile

def writeNew(newtext, textfile):
    with open(textfile, 'w') as file:
      file.write(newtext)

file = 'text_document.txt'
writeNew(replace_aqua(file), file)
print(replace_aqua(file))

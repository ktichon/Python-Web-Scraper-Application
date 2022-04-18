from html.parser import HTMLParser
from html.entities import name2codepoint
import urllib.request


class MyHTMLParser(HTMLParser):
    """Functions to parse html data to read and write colours."""
    def __init__(self):
        HTMLParser.__init__(self)
        self.colorExists = False
        self.hexExists = False
        self.rightTags = False
        self.hex = ""
        self.colourDict = {}
    
    def handle_starttag(self, tag, attrs):
            if tag == "td":
                self.rightTags = True
            if tag == "a":
                for attr, val in attrs:
                    if attr == 'class':
                        self.colorExists = True
                    if attr == 'href':
                        self.hexExists = True
                        self.hex = val

    def handle_endtag(self, tag):
            if tag == "a":
                self.colorExists = False
                self.hexExists = False
                self.rightTags = False

    def handle_data(self, data):
        if self.colorExists and self.hexExists and self.rightTags:
            self.colourDict.update({data: self.hex.replace("/", "#", 1)})
            print(data, self.hex.replace("/", "#", 1))
            
    def print_dictionary(self):
        print(len(self.colourDict))
            

myparser = MyHTMLParser()

with urllib.request.urlopen('https://www.colorhexa.com/color-names') as response:
    html = str(response.read())

myparser.feed(html)

myparser.print_dictionary()

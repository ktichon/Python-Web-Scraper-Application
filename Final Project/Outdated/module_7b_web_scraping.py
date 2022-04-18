
from html.parser import HTMLParser
import urllib.request

from html.entities import name2codepoint
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


class WebParsser(HTMLParser):
    def __init__(self, parentTag, childTag, numOfValues ):
        HTMLParser.__init__(self, convert_charrefs=True)
        self.parentTage = parentTag
        self.childTag = childTag
        self.inParent = False
        self.inInfo = False
        self.key = None
        self.vaules = []
        self.numOfValues = numOfValues
        self.numOfValuesProccesed = 1
        self.colours = {}
        self.inTableBody = False


    def handle_starttag(self, tag, attrs):
        if tag == "tbody":
            self.inTableBody = True
        if self.inTableBody and self.parentTage == tag:
            self.inParent = True
            self.numOfValuesProccesed = 1
        if self.inParent and self.childTag == tag and self.numOfValuesProccesed <=  self.numOfValues:
            self.inInfo = True

    def handle_endtag(self, tag):
        if tag == "tbody":
            self.inTableBody = False
        if self.inTableBody and self.parentTage == tag:
            self.colours[self.key] = self.vaules
            self.inParent = False
            self.key = None
            self.vaules = []
        if self.inParent and self.childTag == tag:
            self.inInfo = False


    def handle_data(self, data):
        if self.inInfo:
            if not self.key:
                self.key = data
            else:
                self.vaules.append(data)
                self.numOfValuesProccesed += 1

    def print_colours(self):
        for k,v in self.colours.items():
            text = k
            for value in v:
                text = text + " " + value
            print(text)
        print("Total Colours: " + str(len(self.colours)))

myparser = WebParsser("tr", "td", 1)
with urllib.request.urlopen('http://www.colorhexa.com/color-names') as response:
    html = str(response.read())
myparser.feed(html)
myparser.print_colours()

from html.parser import HTMLParser
import urllib.request

from html.entities import name2codepoint
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


class WebTableParsser(HTMLParser):
    """Parses the first x collumns from a html table and puts in a dictionary"""
    def __init__(self, parentTag, childTag, numOfValues ):
        HTMLParser.__init__(self, convert_charrefs=True)
        self.parentTage = parentTag
        self.childTag = childTag
        self.inParent = False
        self.inInfo = False
        self.key = None
        self.vaules = []
        self.numOfValues = numOfValues
        self.NumOfValuesProccesed = 1
        self.items = {}
        self.InTableBody = False


    def handle_starttag(self, tag, attrs):
        if tag == "tbody":
            self.InTableBody = True
        if self.InTableBody and self.parentTage == tag:
            self.inParent = True
            self.NumOfValuesProccesed = 1
        if self.inParent and self.childTag == tag and self.NumOfValuesProccesed <=  self.numOfValues:
            self.inInfo = True
        # for attr in attrs:
        #     print("   attr:", attr)

    def handle_endtag(self, tag):
        if tag == "tbody":
            self.InTableBody = False
        if self.InTableBody and self.parentTage == tag:
            self.items[self.key] = self.vaules
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
                self.NumOfValuesProccesed += 1
    def print_items(self):
        for k,v in self.items.items():
            text = k
            for value in v:
                text = text + " " + value
            print(text)
        print("Total items: " + str(len(self.items)))


    # def handle_comment(self, data):
    #     print("Comment  :", data)

    # def handle_entityref(self, name):
    #     c = chr(name2codepoint[name])
    #     print("Named ent:", c)

    # def handle_charref(self, name):
    #     if name.startswith('x'):
    #         c = chr(int(name[1:], 16))
    #     else:
    #         c = chr(int(name))
    #     print("Num ent  :", c)

    # def handle_decl(self, data):
    #     print("Decl   :", data)

myparser = WebTableParsser("tr", "td", 3)
with urllib.request.urlopen('http://www.colorhexa.com/color-names') as response:
    html = str(response.read())
myparser.feed(html)
myparser.print_items()
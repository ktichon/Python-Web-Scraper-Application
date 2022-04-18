from html.parser import HTMLParser

import urllib.request

class GetAfterHTMLParser(HTMLParser):
    def __init__(self, stringBefore):
        HTMLParser.__init__(self, convert_charrefs=True)
        self.stringBefore = stringBefore
    # def handle_starttag(self, tag, attrs):
    #     print("Found a start tag:", tag)
    # def handle_endtag(self, tag):
    #     print("Found end tag :", tag)
    def handle_data(self, data):
        if self.stringBefore in data:
            print(data.removeprefix(self.stringBefore).strip())

myparser = GetAfterHTMLParser("Current IP Address:")
with urllib.request.urlopen('http://checkip.dyndns.org/') as response:
    html = str(response.read())
myparser.feed(html)
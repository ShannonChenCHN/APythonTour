

from html.parser import HTMLParser
from bs4 import BeautifulSoup

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('Start Tag: <%s>' % tag)

    def handle_endtag(self, tag):
        print('End Tag: </%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('Start End Tag: <%s/>' % tag)

    def handle_data(self, data):
        print('Data: ', data)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)

HTMLText = '''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>'''

parser = MyHTMLParser()
parser.feed(HTMLText)

soup = BeautifulSoup(HTMLText, features="html.parser")
tag = soup.a

print('f')

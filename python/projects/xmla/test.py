import requests
from bs4 import BeautifulSoup
import codecs

url = 'http://www.ximalaya.com/zhubo/8889234/'

r = requests.get(url)

with codecs.open('test.html', 'w', 'utf-8') as fh:
    fh.write(r.text)


import requests
from bs4 import BeautifulSoup
import os

URL_BASE = 'http://flask.pocoo.org/docs/0.10/'
PATH_BASE = r'flask-doc'

url = 'http://flask.pocoo.org/docs/0.10/errorhandling/#debugging-application-errors'
url = 'http://flask.pocoo.org/docs/0.10/foreword/'


HTML_PREFIX = '''
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title></title>
<link href="style.css" rel="stylesheet" type="text/css" />
</head>
'''
HTML_SUFFIX = '</html>'

def getData(url):
    headers = {
            "User-Agent":'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36',}        
    res = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(res.content, 'lxml')
    data = soup.find('div', class_='bodywrapper')
    # return str(data.contents).encode('utf-8')
    return data


def getUrlList(url=URL_BASE):
    url_list = []
    
    data = getData(url)
    links = data.find_all('a')
    for link in links:
        # print link['href']
        href = link['href']
        if not href.startswith('#'):
            href = href.split('/')[0]
            url_list.append(link['href'].split('/')[0])
    
    urls = {}
    for url in url_list:
        urls[url] = urls.get(url)   # default: None
        
    url_list = urls.keys()
    return url_list
        
    
    
def writeHtml(url, fname):
    data = getData(url).renderContents()
    html = HTML_PREFIX + data + HTML_SUFFIX
    fname = r'flask-doc\test.html'
    with open(fname, 'w') as f:
        f.write(html)

if __name__ == '__main__':
    url_list =  getUrlList()
    for url in url_list:
        print url

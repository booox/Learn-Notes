import requests
from bs4 import BeautifulSoup
import os

URL_BASE = 'http://flask.pocoo.org/docs/0.10/'
PATH_BASE = 'flask-doc\\'

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
    return data


def getTitleList(url=URL_BASE):
    title_list = []
    
    data = getData(url)
    
    # write the index.html
    fname = PATH_BASE + '\\' + 'index.html'
    with open(fname, 'w') as f:
        html = HTML_PREFIX + data.renderContents() + HTML_SUFFIX
        f.write(html)
    
    # extract title_list
    links = data.find_all('a')
    for link in links:
        print link['href']
        href = link['href']
        if ( not href.startswith('#') ) and ( not href.startswith('http:') ):
            href = href.split('/')[0]
            title_list.append(link['href'].split('/')[0])
    
    titles = {}
    for url in title_list:
        titles[url] = titles.get(url)   # default: None
        
    title_list = titles.keys()
    return title_list
        
    

if __name__ == '__main__':
    title_list =  getTitleList()
    print title_list
    exit(1)
    for title in title_list:
        fname = PATH_BASE + '\\' + title + '.html'
        url = URL_BASE + title
        print title, '\t', fname, '\t', url
        
        data = getData(url)
        # data = str(data.contents).encode('utf-8')
        html = HTML_PREFIX + data.renderContents() + HTML_SUFFIX
        
        with open(fname, 'w') as f:
            f.write(html)
            
        # break

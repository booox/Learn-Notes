#coding=utf-8
import requests
from bs4 import BeautifulSoup
import os
import re
import sys
import time

reload(sys)
sys.setdefaultencoding('utf-8')

CONFIG = {
    'HOME_BASE' : 'http://blog.miguelgrinberg.com',
    'URL_BASE' : 'http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world',
    'PATH_BASE' : 'flask-mega-tutorial',
    'TITLE' : 'The Flask Mega-Tutorial',
    }



url = 'http://flask.pocoo.org/docs/0.10/errorhandling/#debugging-application-errors'
url = 'http://flask.pocoo.org/docs/0.10/foreword/'


def generateHTML(title, content):
    ''' generate html code '''
    html = '''
    <!DOCTYPE html>
    <html xmlns="http://www.w3.org/1999/xhtml">
    <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>%s</title>
    <link href="style.css" rel="stylesheet" type="text/css" />
    </head>
    %s
    </html>
    ''' % (title, content)
    
    return html
    
def initConfig(config=CONFIG):
    if not os.path.isdir(config['PATH_BASE']):
        os.makedirs(config['PATH_BASE'])   
    
def getResSoup(url):
    headers = {
            "User-Agent":'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36',}        
    res = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(res.content, 'lxml')
    # data = soup.find('div', class_='bodywrapper')
    return res, soup

def getOnePage(url, out_title):
    res, soup = getResSoup(url)
    
    # main content tag wrap
    tag_wrap = soup.find('div', id='main')
    
    # need delete tags
    tag_wrap.find('div', class_='posted').extract()
    tag_wrap.find('div', class_='social-bar').extract()
    
    # deal for local link
    tag_wrap_urls = soup.find('div', class_='post_body').ul
    tag_list_a = tag_wrap_urls.find_all('a') 
    for tag_a in tag_list_a:
        
        # change the href for local access
        tag_a['href'] = tag_a['href'][6:]  # kick '/post/'
    
    soup_pretty = tag_wrap.prettify()
    
    # write index.html
    fname = CONFIG['PATH_BASE'] + '\\' + out_title
    with open(fname, 'w') as f:
        # html = generateHTML(TITLE, res.renderContents() )
        html = generateHTML(CONFIG['TITLE'], soup_pretty )
        f.write(html)

def getAllUrls(url=CONFIG['URL_BASE']):
    # [['url', 'link']]      
    # url : for web scrapy
    # link : for local filename
    url_list = []
    
    res, soup = getResSoup(url)
    
    # main content tag wrap
    tag_wrap = soup.find('div', id='main')
    
    # need delete tags
    tag_wrap.find('div', class_='posted').extract()
    tag_wrap.find('div', class_='social-bar').extract()
    
    # extract all urls
    tag_wrap_urls = soup.find('div', class_='post_body').ul
    tag_list_a = tag_wrap_urls.find_all('a') 
    for tag_a in tag_list_a:
        url = CONFIG['HOME_BASE'] + tag_a['href']      # for web access
        link = re.sub(r'/post/', '', tag_a['href'])     # for local access
        
        tag_a['href'] = link  # change the href for local access
      
        url_list.append([url, link])
    
    # soup_pretty = tag_wrap.prettify()
    
    # write index.html
    
    # fname = CONFIG['PATH_BASE'] + '\\' + 'index.html'
    # with open(fname, 'w') as f:
        # html = generateHTML(TITLE, res.renderContents() )
        # html = generateHTML(CONFIG['TITLE'], soup_pretty )
        # f.write(html)
    
    return url_list
        
        
def main():
    url_list = getAllUrls()
    print len(url_list)
    print url_list[2]
    
    for oneurl in url_list:
        url = oneurl[0]
        link = oneurl[1]
        print '\nstart:', link
        print '\t', url
        getOnePage(url, link)
        print 'done:', link
        time.sleep(1)
        
    # for url in url_list:
        
def test():
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
    
    
def getTitleList(url=CONFIG['URL_BASE']):
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
    
    initConfig(config=CONFIG)
    # print generateHTML(TITLE, '<div>test</div>')
    
    main()
    
    # exit()
    

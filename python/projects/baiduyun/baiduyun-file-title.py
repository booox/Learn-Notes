#encoding=utf-8
import requests
from bs4 import BeautifulSoup



baseurl = 'http://pan.baidu.com/wap/share/home?third=4&uk=2252021684&start='
suffix = '&adapt=pc&fr=ftw'


def getData(url):
    
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"}
    
    res = requests.get(url, headers=headers)
    return res.content
    


fname = 'title.txt'
with open(fname, 'w+') as f:

    start = 0
    while start <= 840:
        
        url = baseurl + str(start) + suffix
        data = getData(url)
        soup = BeautifulSoup(data, 'lxml')

        tag_wrap = soup.find('ul', class_='list').find_all('li')
        
        for li in tag_wrap:
            f.write(li['data-fn'].encode('utf-8') + '\n')
            print li['data-fn'].encode('utf-8')
        print 'Done'
        
        start += 20
        if start >100: break
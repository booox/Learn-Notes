#coding=utf-8
import requests
from bs4 import BeautifulSoup



board_url = 'http://www.douban.com/board/1001394/?dcs=sns'
# kw_song_search_url = 'http://search.kuwo.cn/r.s?ft=music&rn=100&newsearch=1&primitive=0&cluster=0&itemset=newkm&rformat=json&encoding=utf8&all='


def extract_board_title(url):
    r = requests.get(url)
    data = r.content

    soup = BeautifulSoup(data, 'lxml')

    tag_wrap = soup.find_all('div', class_='item-intro')

    for tag in tag_wrap:
        song_name = tag.a.text
        songer_name = tag.span.text.split('/')[0]
        songer_name = songer_name.encode('utf-8')
        print song_name, '\t[', songer_name, ']'
    
    
extract_board_title(board_url)



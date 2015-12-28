# encoding: utf-8

#!/usr/bin/env python
import sqlite3
import xmly
import json
import re

try:
    import requests
    from bs4 import BeautifulSoup
except:
    print "Library requests/BeautifulSoup NOT FOUND, and We need them."
    
class XMLYSession(requests.Session):
    """ Wrapper of requests.Session at zhihu.com. """
    
    def __init__(self):
        # print xmly.HOME_URL
        super(XMLYSession, self).__init__()
        r = self.get(url=xmly.HOME_URL)
        print r.ok, r.status_code, r.url
        
        self._cookies = r.cookies

    def getData(self, url, **kwargs):
        res = self.get(url=url, **kwargs)
        self._cookies = res.cookies
        return res
        
    def postData(self, url, data=None, **kwargs):
        data['_xsrf'] = self._cookies['_xsrf']
        return self.post(url=url, data=data, cookies = self._cookies, **kwargs)
        
    def getZhuboProfile(self, url=None):
        """   Get a zhubo's profile, url is the zhubo's homepage url  """
        

        zhubo = xmly.Zhubo()    # create a Zhubo instance
        zhubo.url  = url
        zhubo.zbid = zbid
        
        res = self.getData(zhubo.url)
        soup = BeautifulSoup(res.text, 'html')
        
        try:
            # print soup.title
            tag_zhubo = soup.find('div', class_='mainbox')
            zhubo.name = tag_zhubo.find('h2', class_='txt-lg5').span.string
            zhubo.fans = tag_zhubo.find('i', class_='icon4-person'). \
                         next_sibling.next_sibling.string
            zhubo.follow = tag_zhubo.find('i', class_='icon4-add'). \
                         next_sibling.next_sibling.string
            zhubo.sound = tag_zhubo.find('i', class_='icon4-sound'). \
                         next_sibling.next_sibling.string
            zhubo.favorites = tag_zhubo.find('i', class_='icon4-heart'). \
                         next_sibling.next_sibling.string
                         
            # zhubo.album = tag_zhubo.find('div', class_='userCenterHd').span.string.split('(')[1][:-1]
            
            zhubo.desc = tag_zhubo.find('div', class_='elli mgtb-10').span.string
            
            
        except:
            raise
            
        return zhubo
            
        
            
    def getPageCount(self, url=None):
        ''' extract page_count from url '''
        
        page_count = 0
        
        res = self.getData(url)
        soup = BeautifulSoup(res.text, 'html')
        
        try:
            pagingBar = soup.find('div', class_='pagingBar_wrapper')
            
            if not pagingBar:
                page_count = 1
            else:
                next = soup.find('a', rel='next')
                page_count = int(next.previous_element.previous_element)
            
        except:
            raise
            
        return page_count
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
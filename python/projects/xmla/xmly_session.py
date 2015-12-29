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
        
    # def postData(self, url, data=None, **kwargs):
        # data['_xsrf'] = self._cookies['_xsrf']
        # return self.post(url=url, data=data, cookies = self._cookies, **kwargs)
        
    def getPageCount(self, url=None):
        ''' extract page_count from url '''
        
        page_count = 0
        
        res = self.getData(url)
        soup = BeautifulSoup(res.text, 'lxml')
        
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
        
        
    def getItemsOnPages(self, url=None, _type='album'):
        '''   get album id or sound ids on all pages  '''
        
        print '\t Start get ', _type, 'on pages'
        item_list = []
        
        res = self.getData(url)
        soup = BeautifulSoup(res.text, 'lxml')
        
        try:
            pagingBar = soup.find('div', class_='pagingBar_wrapper')
            
            if not pagingBar:
                page_count = 1
            else:
                next = soup.find('a', rel='next')
                page_count = int(next.previous_element.previous_element)
            
            print '\t Start retrive the first page, total:', page_count
            
            if _type == 'album' or _type == 0:
                tag_wrap = soup.find('ul', class_='album_list')
                albums = tag_wrap.find_all('li')
            
                for album in albums:
                    item_list.append(album["album_id"])     # 327780
                    
            elif _type == 'sound' or _type == 1:
                tag_wrap = soup.find('ul', class_='body_list') 
                sound_ids = tag_wrap['sound_ids'].split(',')        # ['11011001','10859773','10669099']
                
                item_list.extend(sound_ids)
                
            print '\t End retrive the first page'
                
            if page_count > 1:
                page = 2
                while page <= page_count:
                    print '\t Start retrive No.', page, ' page'
                    res = self.getData(url=url.lstrip('/') + '/p' + str(page))
                    soup = BeautifulSoup(res.text, 'lxml')
                    
                    if _type == 'album' or _type == 0:
                    
                        tag_wrap = soup.find('ul', class_='album_list')
                        albums = tag_wrap.find_all('li')
                        
                        for album in albums:
                            item_list.append(album["album_id"])            # 327780
                            
                    elif _type == "sound" or _type == 1:
                        
                        tag_wrap = soup.find('ul', class_='body_list') 
                        sound_ids = tag_wrap['sound_ids'].split(',')        # ['11011001','10859773','10669099']
                        
                        item_list.extend(sound_ids)
                    print '\t End retrive No,' , page, ' page'
                    
                    page = page + 1

                    # print '+',
                    
            print '\n\t Done get ', _type, 'on pages'
        except:
            raise
            
        return item_list
        
        
    def getZhuboProfile(self, url=None):
        """   Get a zhubo's profile, url is the zhubo's homepage url  """
        
        print 'Retrive Start:', url
        zhubo = xmly.Zhubo()    # create a Zhubo instance
        
        zhubo.url  = url
        zbid = url.rstrip('/').split('/')[-1]
        album_url = xmly.HOME_URL + '/' + zbid + '/album'
        zhubo.zbid = zbid
        zhubo.album_url = album_url
        
        res = self.getData(zhubo.url)
        soup = BeautifulSoup(res.text, 'lxml')
        
        try:
            # print soup.title
            tag_zhubo = soup.find('div', class_='mainbox')
            zhubo.name = tag_zhubo.find('h2', class_='txt-lg5').span.string
            zhubo.fans = int(tag_zhubo.find('i', class_='icon4-person'). \
                         next_sibling.next_sibling.string)
            zhubo.follow = int(tag_zhubo.find('i', class_='icon4-add'). \
                         next_sibling.next_sibling.string)
            zhubo.sound = int(tag_zhubo.find('i', class_='icon4-sound'). \
                         next_sibling.next_sibling.string)
            zhubo.favorites = int(tag_zhubo.find('i', class_='icon4-heart'). \
                         next_sibling.next_sibling.string)
                         
            zhubo.album_ids = self.getItemsOnPages(album_url, 'album')       
            zhubo.desc = tag_zhubo.find('div', class_='elli mgtb-10').span.string
            print 'Retrive Done', url
            
        except:
            raise
            
        return zhubo
            
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
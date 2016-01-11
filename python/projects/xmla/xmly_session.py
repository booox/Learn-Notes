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
        headers = {
                "User-Agent":'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36',}        
        r = self.get(url=xmly.HOME_URL, headers=headers)
        # r = self.get(url=xmly.HOME_URL)
        # print r.ok, r.status_code, r.url
        
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
        soup = BeautifulSoup(res.content, 'lxml')
        
        try:
            pagingBar = soup.find('div', class_='pagingBar_wrapper')
            
            if not pagingBar:
                page_count = 1
            else:
                page_count = int(soup.find_all('a', class_='pagingBar_page')[-2].string)
            
        except:
            raise
            
        return page_count
    
    def getTagOnPage(self, soup):
        tag_list = []
        
        try:
            tag_wrap = soup.find_all('a', class_='tagBtn2')
            for tag in tag_wrap:
                tag_list.append(tag.span.string.encode('utf-8'))
                # print type(tag.span.string)
        # except:
            # pass
        except Exception, x:
            print x
            raise
            
        return tag_list
        
    def getItemsOnPages(self, url=None, _type='allAlbum'):
        '''   get album id or sound ids on all pages  
            _type( allAlbum ): Zhubo's all albums page
            _type( allSound ): Zhubo's all sounds page
            _type( albumSound ): Album's all sounds
        '''
        
        print '\t Start getItemsOnPages _type= ', _type, 'From : ', url
        item_list = []
        
        res = self.getData(url)
        soup = BeautifulSoup(res.content, 'lxml')
        try:
            pagingBar = soup.find('div', class_='pagingBar_wrapper')
            
            if not pagingBar:
                page_count = 1
            else:
                page_count = int(soup.find_all('a', class_='pagingBar_page')[-2].string)
            
            print '\t getItemsOnPages retrieve the first page, total:', page_count
            
            if _type == 'allAlbum':
                tag_wrap = soup.find('ul', class_='album_list')
                albums = tag_wrap.find_all('li')
            
                for album in albums:
                    item_list.append(album["album_id"])     # 327780
                    
            elif _type == 'allSound':
                tag_wrap = soup.find('div', class_='body_list_wrap').find('ul', class_='body_list') 
                sound_ids = tag_wrap['sound_ids'].split(',')        # ['11011001','10859773','10669099']
                
                item_list.extend(sound_ids)
                
            elif _type == 'albumSound':
                tag_wrap = soup.find('div', class_='personal_body')
                sound_ids = tag_wrap['sound_ids'].split(',')
                
                for sound_id in sound_ids:
                    item_list.append(sound_id)
                
            print '\t getItemsOnPages retrive the first page done.'
            print '\t getItemsOnPages retrive multi pages start.'
                
            if page_count > 1:
                page = 2
                while page <= page_count:
                    page_url = url.rstrip('/') + '/p' + str(page)
                    if _type == 'albumSound': page_url = url.rstrip('/') + '?page=' + str(page)
                    print '\t Retriving page ', page, '/', page_count
                    print '\t Page url: ', page_url,
                    
                    res = self.getData(page_url)
                    soup = BeautifulSoup(res.content, 'lxml')
                    if _type == 'allAlbum':
                    
                        tag_wrap = soup.find('ul', class_='album_list')
                        albums = tag_wrap.find_all('li')
                        
                        for album in albums:
                            item_list.append(album["album_id"])            # 327780
                            
                    elif _type == "allSound":
                        
                        tag_wrap = soup.find('div', class_='body_list_wrap').find('ul', class_='body_list')
                        sound_ids = tag_wrap['sound_ids'].split(',')        # ['11011001','10859773','10669099']
                        
                        item_list.extend(sound_ids)
                        
                    elif _type == 'albumSound':
                        tag_wrap = soup.find('div', class_='personal_body')
                        sound_ids = tag_wrap['sound_ids'].split(',')
                        
                        for sound_id in sound_ids:
                            item_list.append(sound_id)
                        
                    print '\t Retriving page done ', page, '/', page_count
                    page = page + 1

            print '\t getItemsOnPages retrive multi pages Done.'
                    
            print '\n\t getItemsOnPages Done : get ', _type, 'from', page_count, 'pages'
        except:
            raise
            
        return item_list
        
        
    def getZhuboProfile(self, url=None):
        """   Get a zhubo's profile, url is the zhubo's homepage url  """
        
        print '\t Retrive Start:', url
        zhubo = xmly.Zhubo()    # create a Zhubo instance
        
        zhubo.url  = url
        zhubo_id = url.rstrip('/').split('/')[-1]
        album_url = xmly.HOME_URL + '/' + zhubo_id + '/album/'
        sound_url = xmly.HOME_URL + '/' + zhubo_id + '/sound/'
        zhubo.zhubo_id = zhubo_id
        zhubo.album_url = album_url
        zhubo.sound_url = sound_url
        
        res = self.getData(zhubo.url)
        soup = BeautifulSoup(res.content, 'lxml')
        
        try:
            # print soup.title
            tag_zhubo = soup.find('div', class_='mainbox')
            zhubo.name = tag_zhubo.find('h2', class_='txt-lg5').span.string
            zhubo.fans = int(tag_zhubo.find('i', class_='icon4-person'). \
                         next_sibling.next_sibling.string)
            zhubo.follow = int(tag_zhubo.find('i', class_='icon4-add'). \
                         next_sibling.next_sibling.string)
            # zhubo.sound = int(tag_zhubo.find('i', class_='icon4-sound'). \
                         # next_sibling.next_sibling.string)
            zhubo.favorites = int(tag_zhubo.find('i', class_='icon4-heart'). \
                         next_sibling.next_sibling.string)
            zhubo.album_count = int(soup.find_all('div', class_='userCenterHd')[0]. \
                        span.string.rstrip(')').split('(')[1])
            zhubo.sound_count = int(soup.find_all('div', class_='userCenterHd')[1]. \
                        span.string.rstrip(')').split('(')[1])
                        
                         
            zhubo.album_ids = self.getItemsOnPages(album_url, 'allAlbum')       
            zhubo.sound_ids = self.getItemsOnPages(sound_url , 'allSound')       
            zhubo.desc = tag_zhubo.find('div', class_='elli mgtb-10').span.string
            
            print '\t Retrive Done', url
            
        except:
            raise
            
        return zhubo
            
    def updateZhubo(self, url=None, do='getnew'):
        """   Get a zhubo's album & sound count , url is the zhubo's homepage url  """
        
        print '\t Retrive Start:', url
        zhubo = xmly.Zhubo()    # create a Zhubo instance
        
        zhubo.url  = url
        zhubo_id = url.rstrip('/').split('/')[-1]
        album_url = xmly.HOME_URL + '/' + zhubo_id + '/album/'
        sound_url = xmly.HOME_URL + '/' + zhubo_id + '/sound/'
        
        res = self.getData(zhubo.url)
        soup = BeautifulSoup(res.content, 'lxml')
        
        if do == 'check':
            try:
                print '\t Zhubo Check Start'
                zhubo.album_count = int(soup.find_all('div', class_='userCenterHd')[0]. \
                            span.string.rstrip(')').split('(')[1])
                zhubo.sound_count = int(soup.find_all('div', class_='userCenterHd')[1]. \
                            span.string.rstrip(')').split('(')[1])
                            
                print '\t Zhubo Check Done'
                
            except:
                raise
        elif do == 'getnew':
            try:
                print '\t Zhubo getnew Start'
                zhubo.album_count = int(soup.find_all('div', class_='userCenterHd')[0]. \
                            span.string.rstrip(')').split('(')[1])
                zhubo.sound_count = int(soup.find_all('div', class_='userCenterHd')[1]. \
                            span.string.rstrip(')').split('(')[1])
                            
                             
                zhubo.album_ids = self.getItemsOnPages(album_url, 'album')       
                zhubo.sound_ids = self.getItemsOnPages(sound_url , 'sound')       
                
                print '\t Zhubo getnew Done'
                
            except:
                raise
            
        return zhubo
            
            
            
    def getAlbumProfile(self, zhubo_id, album_id):
        url = xmly.HOME_URL + '/' + zhubo_id + '/album/' + album_id + '/'
        print url
        album = xmly.Album()    # create a Album instance
        
        # album properties
        
        # extract info about album
        res = self.getData(url)
        soup = BeautifulSoup(res.content, 'lxml')
        
        
        try:
            name                =   soup.h1.string
            category            =   soup.find('span', class_='mgr-5').previous_element.previous_element    
            playcount          =    soup.find('div', class_='detailContent_playcountDetail').span.string
            sound_count     =   int(soup.find('span', class_='albumSoundcount').string[1:-1])
            update_time      =  soup.find('div', class_='detailContent_category').span.string.split(':')[1].strip()
            
            tag_list = self.getTagOnPage(soup)
            sound_ids = self.getItemsOnPages(url , 'albumSound')       
            
            
            album.album_id         =   album_id
            album.zhubo_id         =   zhubo_id
            album.url                    =   url
            
            album.name               =   name
            album.category           =   category
            album.tag                    =   tag_list
            album.playcount          =   playcount
            album.sound_count        =   sound_count
            album.update_time        =   update_time            
            album.sound_ids          =   sound_ids
            
        except:
            raise
            
        return album
            
            
    def updateAlbum(self, url=None, do='check'):
        """   Get a zhubo's album & sound count , url is the zhubo's homepage url  """
        
        print '\t Retrive Start:', url
        album = xmly.Album()    # create a Zhubo instance
        
        album.url  = url
        # zhubo_id = url.rstrip('/').split('/')[-1]
        # album_url = xmly.HOME_URL + '/' + zhubo_id + '/album/'
        # sound_url = xmly.HOME_URL + '/' + zhubo_id + '/sound/'
        
        res = self.getData(album.url)
        soup = BeautifulSoup(res.content, 'lxml')
        
        if do == 'check':
            try:
                print '\t Album Check Start'
                album.sound_count = int(soup.find('span', class_='albumSoundcount').string[1:-1])
                album.update_time = soup.find('div', class_='detailContent_category').span.string.split(':')[1].strip()
                
                            
                print '\t Album Check Done'
                
            except:
                raise
        elif do == 'getnew':
            try:
                print '\t Album getnew Start'
                sound_count = int(soup.find('span', class_='albumSoundcount').string[1:-1])
                update_time = soup.find('div', class_='detailContent_category').span.string.split(':')[1].strip()
                playcount      = soup.find('div', class_='detailContent_playcountDetail').span.string
                            
                sound_ids = self.getItemsOnPages(url , 'albumSound') 

                
                album.playcount        =   playcount              
                album.sound_ids       =   sound_ids
                album.sound_count   =   sound_count               
                album.update_time    =   update_time                

                print '\t Album getnew Done'
                
            except:
                raise
            
        return album
            

    def getTrackProfile(self, sound_id):
        ''' get track profile '''
        
        # url: http://www.ximalaya.com/tracks/10259524.json
        url = xmly.HOME_URL + '/tracks/' + sound_id + '.json'
        
        res = self.getData(url)
        data = json.loads(res.content)
        
        track = xmly.Track() 
        
        try:
      
            album_id            =  data['album_id']     
            zhubo_id            =  data['uid']
            sound_id            =  data['id']
            title                   =  data['title']
            intro                  =  data['intro']
            duration             =  data['duration']
            play_count          =  data['play_count']
            play_path_32      =  data['play_path_32']
            play_path_64      =  data['play_path_64']
            play_path           =  data['play_path']
            category_name    =  data['category_name']
            shares_count       =  data['shares_count']
            favorites_count    =  data['favorites_count']

        
            track.album_id       =    album_id
            track.zhubo_id       =    zhubo_id
            track.sound_id       =    sound_id
            track.title                  =   title
            track.intro              =   intro
            track.duration           =   duration
            track.play_count         =   play_count
            track.play_path_32      =   play_path_32
            track.play_path_64       =   play_path_64
            track.play_path            =   play_path
            track.category_name      =   category_name
            track.shares_count        =   shares_count
            track.favorites_count      =   favorites_count
        
            
            
        except:
            raise
            
        return track
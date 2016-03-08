#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xmly
from xmly_session import XMLYSession
import pickle
import sys



if __name__ == '__main__':
    ''' how to judge the server have been updated.???'''
    
    sys.stdout = xmly.Logger('log.txt')
    sys.stderr = xmly.Logger('log.txt')
    sys.getfilesystemencoding()
    
    while True:
        print ''
        url = raw_input('Enter a zhubo, album or sound url:')
        
        # if len(url) < 1: url = 'http://www.ximalaya.com/zhubo/1012757/'
        if len(url) < 1: 
            # url = 'http://www.ximalaya.com/29872932/album/2754031/'
            # url = 'http://www.ximalaya.com/zhubo/1412917/'
            # url = 'http://www.ximalaya.com/37310896/album/3253111/'
            # url = 'http://www.ximalaya.com/37310896/album/3253111/'
            # url = 'http://www.ximalaya.com/38909644/album/3376281/'
            # url = 'http://www.ximalaya.com/1412917/album/239463/'  # 罗辑思维 全集
            # url = 'http://www.ximalaya.com/1000168/album/213506/'  # 小晓说
            
            # url = 'http://www.ximalaya.com/22366783/album/2685288/'  # 读读书
            # url = 'http://www.ximalaya.com/12495477/album/269179/'  # 吴晓波频道   
            # url = 'http://www.ximalaya.com/39200626/album/3385980/'  # 静说日本   
            # url = 'http://www.ximalaya.com/11119867/album/262212/'  # 潘吉Jenny告诉你--学英语聊美国   
            # url = 'http://www.ximalaya.com/38212466/album/3492675/'  # 偏见
            # url = 'http://www.ximalaya.com/16174533/album/3340045/'  # 你不恐慌，我不入场
            url = 'http://www.ximalaya.com/12512006/album/2894105/'  # 给孩子的诗
            
        if url == 'bye': exit(1)
            
        print url        
        result = xmly.checkURL(url)
        if not result["url_type"]:
            xmly.printUrlError()
        else:
                
            # flesh database
            conn, cur = xmly.openDB()
            xmly.initDB(cur)
            
            # -------------- zhubo ------------ 
            if result["url_type"] == "zhubo":
                xmly.writeZhuboToDB(conn, cur, url, result)
            
            # -------------- album ------------ 
            elif result["url_type"] == "album":
                # Write to db
                # xmly.writeAlbumToDB(conn, cur, url, result)
                
                # download Album from db
                xmly.downloadAlbum(conn, cur, url, result)
            
            # -------------- Track ------------ 
            elif result["url_type"] == "sound":
                xmly.writeTrackToDB(conn, cur, url, result)
                    
    
    
            xmly.closeDB(conn)
    
    # session = XMLYSession()
    # zhubo = session.getZhuboProfile(url)
    # print zhubo.url
    # print zhubo.follow, zhubo.fans 
    # print zhubo.album_url, zhubo.album_ids
    # print type(zhubo.album_ids)
    # print 'sound:', zhubo.sound, 'favorites:', zhubo.favorites
    # print zhubo.name.decode('utf-8')
    # print zhubo.desc.decode('utf-8')
    
    # print 'Start Write into db.'
    
    # buffer album_ids for BLOB
    # zhubo.album_ids = buffer(pickle.dumps(zhubo.album_ids, pickle.HIGHEST_PROTOCOL))
    
    # cur.execute('''INSERT OR REPLACE INTO Zhubo
        # (zbid, name, url, fans, follow, sound, favorites, album_url, desc, album_ids)
        # VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ? )''',
        # (zhubo.zbid, zhubo.name, zhubo.url, 
        # zhubo.fans, zhubo.follow, zhubo.sound, zhubo.favorites, 
        # zhubo.album_url, zhubo.desc, zhubo.album_ids))
    
    # conn.commit()
    
    
    # Fetch vars
    # cur.execute("""SELECT album_ids FROM Zhubo""")
    # out = cur.fetchone()
    # album_id = out[0] 
    # album_id = pickle.loads(album_id)
    
    # print album_id, type(album_id)

    
    
    # close database
    # xmly.closeDB(conn)

    
    
    # url = 'http://www.ximalaya.com/zhubo/1000120/'      
                # zhubo: 郎咸平说
    # url = 'http://www.ximalaya.com/8889234/album/'   
                # albums : 谢涛听世界
    # url = 'http://www.ximalaya.com/1000120/album/327780'   
                # album : 财经郎眼 2015
    # url = 'http://www.ximalaya.com/1000120/sound/'                   
                # sounds : 郎咸平说
    # url = 'http://www.ximalaya.com/1162654/sound/11011001'     
                # sound : 郎咸平说
    
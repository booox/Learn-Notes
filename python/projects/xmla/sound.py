#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xmly
from xmly_session import XMLYSession
import pickle

if __name__ == '__main__':
    
    # flesh database
    conn, cur = xmly.openDB()
    xmly.initDB(cur)
    
    session = XMLYSession()
    url = 'http://www.ximalaya.com/zhubo/1000120/'      
                # zhubo: 郎咸平说
    # url = 'http://www.ximalaya.com/8889234/album/'   
                # albums : 谢涛听世界
    # url = 'http://www.ximalaya.com/1000120/album/327780'   
                # album : 财经郎眼 2015
    # url = 'http://www.ximalaya.com/1000120/sound/'                   
                # sounds : 郎咸平说
    # url = 'http://www.ximalaya.com/1162654/sound/11011001'     
                # sound : 郎咸平说
    
    zhubo = session.getZhuboProfile(url)
    print zhubo.url
    print zhubo.follow, zhubo.fans 
    print zhubo.album_url, zhubo.album_ids
    print type(zhubo.album_ids)
    print 'sound:', zhubo.sound, 'favorites:', zhubo.favorites
    # print zhubo.name.decode('utf-8')
    # print zhubo.desc.decode('utf-8')
    
    # buffer album_ids for BLOB
    zhubo.album_ids = buffer(pickle.dumps(zhubo.album_ids, pickle.HIGHEST_PROTOCOL))
    
    cur.execute('''INSERT OR REPLACE INTO Zhubo
        (zbid, name, url, fans, follow, sound, favorites, album_url, desc, album_ids)
        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ? )''',
        (zhubo.zbid, zhubo.name, zhubo.url, 
        zhubo.fans, zhubo.follow, zhubo.sound, zhubo.favorites, 
        zhubo.album_url, zhubo.desc, zhubo.album_ids))
    
    conn.commit()
    
    
    # Fetch vars
    # cursor.execute("""
        # SELECT * FROM trials WHERE timestamp = ?""", (timestamp,))
    # out = cursor.fetchone()
    # s1 = out[1] 
    # emg1 = pickle.loads(s1)

    # print emg1
    # print emg1[0], emg1[:5]
    # print 15 in emg1
    # print 'abc' in emg1    
    
    
    
    # close database
    xmly.closeDB(conn)
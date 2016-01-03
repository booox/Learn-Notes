#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xmly
from xmly_session import XMLYSession
import pickle

if __name__ == '__main__':
    ''' how to judge the server have been updated.???'''
    
    while True:
        print ''
        url = raw_input('Enter a zhubo, album or sound url:')
        
        # if len(url) < 1: url = 'http://www.ximalaya.com/zhubo/1012757/'
        if len(url) < 1: url = 'http://www.ximalaya.com/29872932/album/2754031/'
        if url == 'bye': exit(1)
        print url
        result = xmly.checkURL(url)
        if not result["url_type"]:
            print '[URL Error] : Please check the url. Only 3 types urls been supporting:'
            print '\t zhubo_url: http://www.ximalaya.com/zhubo/1000120/'
            print '\t album_url: http://www.ximalaya.com/1000120/album/327780/'
            print '\t sound_url: http://www.ximalaya.com/1162654/sound/11011001/'
            print '\t NOTICE: The url must be end with a "/". '
        else:
                
            # flesh database
            conn, cur = xmly.openDB()
            xmly.initDB(cur)
            
            # -------------- zhubo ------------ 
            if result["url_type"] == "zhubo":
                zhubo_id = result["zhubo_id"]
                print '\tzhubo_id:', zhubo_id
                
                # check zhubo_id exists?
                cur.execute("SELECT zhubo_id, album_count, album_ids, sound_count, sound_ids FROM Zhubo WHERE zhubo_id = ?",
                        (zhubo_id, ))
                try:                                                        # Found the record
                    data = cur.fetchone()
                    
                    album_count = data[1]
                    # album_ids = pickle.loads(data[2])
                    sound_count = data[3]
                    # sound_ids = pickle.loads(data[4])
                    print "Zhubo in database ", zhubo_id
                    # print 'Album ids:', album_ids
                    # print 'Sound ids:', sound_ids
                    
                    session = XMLYSession()
                    zhubo = session.updateZhubo(url, 'check')
                    print "\t Count in DB -- album_count:", album_count, '\t sound_count:', sound_count
                    print '\t Count in Web -- album_count:', zhubo.album_count, '\t sound_count:', zhubo.sound_count
                    
                    # album_count, sound_count increase ?
                    if zhubo.album_count > album_count or zhubo.sound_count > sound_count:
                        # update db
                        print 'Zhubo Need Update '
                        zhubo = session.updateZhubo(url, 'getnew')
                        
                        zhubo.album_ids = buffer(pickle.dumps(zhubo.album_ids, 
                                pickle.HIGHEST_PROTOCOL))                       # buffer album_ids for BLOB
                        zhubo.sound_ids = buffer(pickle.dumps(zhubo.sound_ids, 
                                pickle.HIGHEST_PROTOCOL))                       # buffer album_ids for BLOB
                                
                        print 'Update zhubo start.', zhubo_id
                        cur.execute('''UPDATE Zhubo SET album_count = ?, album_ids = ?, 
                             sound_count = ?, sound_ids = ? WHERE zhubo_id = ?''', (zhubo.album_count,
                             zhubo.album_ids, zhubo.sound_count, zhubo.sound_ids, zhubo_id))
                        
                        conn.commit()
                        print 'Update zhubo Done.', zhubo_id
                        
                    else:
                        print "NO NEED for update."
                        
                except TypeError:                                   # record not in database
                    print "zhubo_id doesn't in db:", zhubo_id
                    
                    # Add new zhubo into db
                    session = XMLYSession()
                    zhubo = session.getZhuboProfile(url)
                    print zhubo.follow, zhubo.fans
                    
                    print '\t=Start Write into db.', zhubo.zhubo_id
                    
                    
                    zhubo.album_ids = buffer(pickle.dumps(zhubo.album_ids, 
                            pickle.HIGHEST_PROTOCOL))                       # buffer album_ids for BLOB
                    zhubo.sound_ids = buffer(pickle.dumps(zhubo.sound_ids, 
                            pickle.HIGHEST_PROTOCOL))                       # buffer album_ids for BLOB
                    
                    cur.execute('''INSERT OR REPLACE INTO Zhubo(zhubo_id, name, url, fans, follow,
                        favorites, album_url, desc, album_ids, album_count, sound_count, sound_ids)
                        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (zhubo.zhubo_id, zhubo.name, zhubo.url,
                        zhubo.fans, zhubo.follow, zhubo.favorites, zhubo.album_url, zhubo.desc,
                         zhubo.album_ids, zhubo.album_count, zhubo.sound_count, zhubo.sound_ids))
                    
                    conn.commit()
                    print '\t=Write zhubo into db done.', zhubo.zhubo_id
                    
                except Exception, x:
                    print x
                    raise
                
            
            # -------------- album ------------ 
            elif result["url_type"] == "album":
                zhubo_id = result["zhubo_id"]
                album_id = result["album_id"]
                
                # check if album_id exists in db?
                cur.execute("SELECT sound_count, update_time FROM Album WHERE album_id = ?", (album_id, ))
                
                try:
                    data = cur.fetchone()
                    sound_count = data[0]
                    update_time = data[1]
                    print "Album in database ", zhubo_id, '/album/', album_id
                    
                    # check the value in web page
                    print 'Check album in webpage'
                    session = XMLYSession()
                    album = session.updateAlbum(url, 'check')
                    print "\t Value in DB -- sound_count:", sound_count, '\t update_time:', update_time
                    print '\t Value in Web -- sound_count:', album.sound_count, '\t update_time:', album.update_time
                    
                    # the value increase or fresh?
                    if album.sound_count > sound_count or album.update_time > update_time:
                        
                        # update db
                        print 'Album Nedd Update.'
                        album = session.updateAlbum(url, 'getnew')
                        
                        playcount      =  album.playcount
                        sound_ids     =  album.sound_ids 
                        sound_count = album.sound_count   
                        update_time  = album.update_time
                        
                        # buffer album_ids for BLOB
                        sound_ids = buffer(pickle.dumps(sound_ids, pickle.HIGHEST_PROTOCOL))
                        
                        print 'Update album start.', zhubo_id, '/album/', album_id
                        cur.execute('''UPDATE Album SET playcount = ?, sound_ids = ?, sound_count = ?,
                                update_time = ? WHERE album_id = ?''', (playcount, sound_ids,
                                sound_count, update_time, album_id))
                                
                        conn.commit()
                        print 'Update album Done.', zhubo_id, '/album/', album_id
                    else:
                        print "NO NEED for update."

                    
                except TypeError:
                    print "Album  doesn't in db:", zhubo_id, '/album/', album_id
                    
                    # Add new Album into db
                    session = XMLYSession()
                    album = session.getAlbumProfile(zhubo_id, album_id)
                    
                    album_id       =  album.album_id
                    zhubo_id       =  album.zhubo_id
                    name            =  album.name
                    url                 =  album.url
                    category        = album.category
                    tag                 = album.tag
                    playcount      =  album.playcount
                    sound_ids      = album.sound_ids
                    sound_count  = album.sound_count
                    update_time   = album.update_time
                    
                    # buffer album_ids for BLOB                    
                    tag = buffer(pickle.dumps(tag, pickle.HIGHEST_PROTOCOL))
                    sound_ids = buffer(pickle.dumps(sound_ids, pickle.HIGHEST_PROTOCOL))
                    
                    print 'Write New Album start.', zhubo_id, '/album/', album_id
                    cur.execute('''INSERT OR REPLACE INTO Album (album_id, zhubo_id, name, url,
                    category, tag, playcount, sound_ids, sound_count, update_time) VALUES (?, ?, ?, ?,
                    ?, ?, ?, ?, ?, ?)''', (album_id, zhubo_id, name, url,
                    category, tag, playcount, sound_ids, sound_count, update_time))
                            
                    conn.commit()
                    print 'Write New Album Done.', zhubo_id, '/album/', album_id
                    
                    
                except Exception, x:
                    print x
                    raise
                
            
            # -------------- sound ------------ 
            elif result["url_type"] == "sound":
                zhubo_id = result["zhubo_id"]
                sound_id = result["sound_id"]
                
                # check if the sound exists in db ?
                cur.execute("SELECT play_path_64, play_path_32, play_path, title FROM Track WHERE sound_id = ?", (sound_id, ))
                
                try:
                    data = cur.fetchone()
                    play_path_64 = data[0]
                    play_path_32 = data[1]
                    play_path = data[2]
                    title = data[3]
                    print 'Sound in database ', zhubo_id, '/sound/', sound_id
                    
                    # do download
                    print 'Download Sound start'
                    print 'Download Sound end...'
                    
                except TypeError:
                    print "Sound  doesn't in db:", zhubo_id, '/sound/', sound_id
                    
                    # Add new Album into db
                    session = XMLYSession()
                    track = session.getTrackProfile(sound_id)
                    
                    album_id            =  track.album_id          
                    zhubo_id            =   track.zhubo_id           
                    sound_id            =   track.sound_id           
                    title                   =  track.title                 
                    intro                  =   track.intro                 
                    duration             =   track.duration            
                    play_count          =  track.play_count       
                    play_path_32      =  track.play_path_32    
                    play_path_64      =  track.play_path_64    
                    play_path           =  track.play_path         
                    category_name    =  track.category_name 
                    shares_count       =  track.shares_count     
                    favorites_count    =  track.favorites_count  
                    
                    

                    print 'Write New Sound start.', zhubo_id, '/sound/', sound_id
                    cur.execute('''INSERT OR REPLACE INTO Track (album_id, zhubo_id, sound_id, title,
                    intro, duration, play_count, play_path_32, play_path_64, play_path, 
                    category_name, shares_count, favorites_count) VALUES (?, ?, ?, ?,
                    ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (album_id, zhubo_id, sound_id, title,
                    intro, duration, play_count, play_path_32, play_path_64, play_path, 
                    category_name, shares_count, favorites_count))
                            
                    conn.commit()
                    print 'Write New Sound Done.', zhubo_id, '/sound/', sound_id
                    
                    
                except Exception, x:
                    print x
                    raise
                    
                    
    
    
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
    
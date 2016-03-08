#coding=utf-8
import sqlite3
from xmly_session import XMLYSession
import re
import pickle
import requests
import os
import sys
import time
import os.path
import subprocess

HOME_URL = 'http://www.ximalaya.com'
DATA_BASE = 'xmly.sqlite'
# AUDIO_DIR = os.path.expanduser('~')   # 'C:\\Users\\username'
AUDIO_DIR = 'E:\\xmly'   # 'C:\\Users\\username'

reload(sys)
sys.setdefaultencoding('gb18030')


class Logger(object):
    "print to console & redirect to a file"
    def __init__(self, filename="Default.log"):
        self.terminal = sys.stdout
        self.log = open(filename, "a")

    def write(self, message):
        self.terminal.write(message.encode('utf-8'))
        self.log.write(message.encode('utf-8'))

class Zhubo(object):
    def __init__(self, 
            zhubo_id      = None,
            name = None,
            url         = None,
            fans        = 0,
            follow   = 0,
            favorites   = 0,
            album_url   = None,
            album_ids   = None,
            album_count   = 0,
            sound_ids   = None,
            sound_count   = 0,
            desc        = None ):
        
        self.zhubo_id = zhubo_id
        self.name = name
        self.url = url
        self.fans = fans
        self.follow = follow
        self.favorites = favorites
        self.album_url = album_url
        self.album_ids = album_ids
        self.album_count = album_count
        self.sound_ids = sound_ids
        self.sound_count = sound_count
        self.desc = desc
        
        
class Album(object):
    def __init__(self,
            album_id              = None,
            zhubo_id              = None,
            name        =   None,
            url             =   None,
            category   =   None,
            tag             =   None,
            playcount   =  None,
            sound_ids      =   None,
            sound_count      =   0,
            update_time =   None):
            
        self.album_id         =   album_id
        self.zhubo_id         =   zhubo_id
        self.name               =   name
        self.url                    =   url
        self.category           =   category
        self.tag                    =   tag
        self.playcount          =   playcount
        self.sound_ids          =   sound_ids
        self.sound_count        =   sound_count
        self.update_time        =   update_time
        
class Track(object):
    def __init__(self,
            album_id            =   None,
            zhubo_id            =   None,  # uid
            sound_id            =   None,  # id
            intro                   =   None,
            duration             =   0,
            title                   =   None,
            play_count          =   0,
            play_path_32       =   None,
            play_path_64        =   None,
            play_path             =   None,
            category_name      =   None,
            shares_count         =   0,
            favorites_count       =   0,
            downloaded       =   0
            ):
        
        self.album_id       =    album_id
        self.zhubo_id       =    zhubo_id
        self.sound_id       =    sound_id
        self.title                  =   title
        self.intro              =   intro
        self.duration           =   duration
        self.play_count         =   play_count
        self.play_path_32      =   play_path_32
        self.play_path_64       =   play_path_64
        self.play_path            =   play_path
        self.category_name      =   category_name
        self.shares_count        =   shares_count
        self.favorites_count      =   favorites_count
        self.downloaded      =   downloaded
        

       
def openDB(db=DATA_BASE):
    ''' open Database  '''
    
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    return conn, cur
    
def closeDB(conn):
    ''' close database '''
    conn.close()

def initDB(cur):
    """ fresh database """
    
    cur.executescript('''
        CREATE TABLE IF NOT EXISTS Zhubo (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            zhubo_id TEXT UNIQUE,
            name TEXT,
            url TEXT,
            fans INTEGER,
            follow INTEGER,
            favorites INTEGER,
            album_url TEXT,
            album_ids BLOB,
            album_count INTEGER,
            sound_ids BLOB,
            sound_count INTEGER,
            desc TEXT
        );
        
        CREATE TABLE IF NOT EXISTS Album (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            album_id TEXT UNIQUE,
            zhubo_id TEXT,
            name TEXT,
            url TEXT,
            category TEXT,
            tag BLOB,
            playcount TEXT,
            sound_ids BLOB,
            sound_count INTEGER,
            update_time TEXT
        );
        
        CREATE TABLE IF NOT EXISTS Track (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            sound_id TEXT UNIQUE,
            album_id TEXT,
            zhubo_id TEXT,
            title TEXT,
            intro TEXT,
            duration INTEGER,
            play_count INTEGER,
            play_path_32 TEXT,
            play_path_64 TEXT,
            play_path TEXT,
            category_name TEXT,
            shares_count INTEGER,
            favorites_count INTEGER,
            downloaded INTEGER DEFAULT 0
        );
        
    ''')
        

def checkURL(url):
    ''' simple check zhubo url '''
    
    # url = 'http://www.ximalaya.com/zhubo/1000120/'      
                # zhubo: 郎咸平说
    # url = 'http://www.ximalaya.com/1000120/album/327780/'   
                # album : 财经郎眼 2015
    # url = 'http://www.ximalaya.com/1162654/sound/11011001/'     
                # sound : 郎咸平说
                
    # url = 'http://www.ximalaya.com/8889234/album/'   
                # albums : 谢涛听世界
    # url = 'http://www.ximalaya.com/1000120/sound/'                   
                # sounds : 郎咸平说
    
    pattern_zhubo = 'http://www\.ximalaya\.com/zhubo/(\d+)/'
    pattern_album = 'http://www\.ximalaya\.com/(\d+)/album/(\d+)/'
    pattern_sound = 'http://www\.ximalaya\.com/(\d+)/sound/(\d+)/'
    
    patterns = [pattern_zhubo, pattern_album, pattern_sound]
    
    result = {}    # url type: zhubo, album, sound

    match_zhubo = re.search(pattern_zhubo, url)
    match_album = re.search(pattern_album , url)
    match_sound = re.search(pattern_sound , url)
    if match_zhubo:
        result["url_type"] = 'zhubo'
        result["zhubo_id"] = match_zhubo.group(1)
        
    elif match_album:
        result["url_type"] = 'album'
        result["zhubo_id"] = match_album.group(1)
        result["album_id"] = match_album.group(2)
    elif match_sound:
        result["url_type"] = 'sound'
        result["zhubo_id"] = match_sound.group(1)
        result["sound_id"] = match_sound.group(2)
    else:
        result["url_type"] = None
        
    return result
    
def printUrlError():
    print '[URL Error] : Please check the url. Only 3 types urls been supporting:'
    print '\t zhubo_url: http://www.ximalaya.com/zhubo/1000120/'
    print '\t album_url: http://www.ximalaya.com/1000120/album/327780/'
    print '\t sound_url: http://www.ximalaya.com/1162654/sound/11011001/'
    print '\t NOTICE: The url must be end with a "/". '

def pretty_windows_filename(filename):
    """clean the file name for winodws"""
    
    pattern = r'[\\/:*?"<>|]'       # strip special chars for windows filename
    filename = re.sub(pattern, ' ', filename)
    return filename


def writeToDB(result):
    
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
        
    
    # -------------- Track ------------ 
    elif result["url_type"] == "sound":
        zhubo_id = result["zhubo_id"]
        sound_id = result["sound_id"]
        
        # check if the Track exists in db ?
        cur.execute("SELECT play_path_64, play_path_32, play_path, title FROM Track WHERE sound_id = ?", (sound_id, ))
        
        try:
            data = cur.fetchone()
            play_path_64 = data[0]
            play_path_32 = data[1]
            play_path = data[2]
            title = data[3]
            print 'Track in database ', zhubo_id, '/sound/', sound_id
            
            # do download
            print 'Download Track start'
            print 'Download Track end...'
            
        except TypeError:
            print "Track  doesn't in db:", zhubo_id, '/sound/', sound_id
            
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
            
            

            print 'Write New Track start.', zhubo_id, '/sound/', sound_id
            cur.execute('''INSERT OR REPLACE INTO Track (album_id, zhubo_id, sound_id, title,
            intro, duration, play_count, play_path_32, play_path_64, play_path, 
            category_name, shares_count, favorites_count) VALUES (?, ?, ?, ?,
            ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (album_id, zhubo_id, sound_id, title,
            intro, duration, play_count, play_path_32, play_path_64, play_path, 
            category_name, shares_count, favorites_count))
                    
            conn.commit()
            print 'Write New Track Done.', zhubo_id, '/sound/', sound_id
            
            
        except Exception, x:
            print x
            raise
            
def writeZhuboToDB(conn, cur, url, result):
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
    
    
    
def writeAlbumToDB(conn, cur, url, result):
    zhubo_id = result["zhubo_id"]
    album_id = result["album_id"]
    
    # check if album_id exists in db?
    cur.execute("SELECT sound_count, update_time, sound_ids FROM Album WHERE album_id = ?", (album_id, ))
    
    try:        # Album in db
        data = cur.fetchone()
        sound_count = data[0]
        update_time = data[1]
        sound_ids_db = data[2]
        print "Album in database ", zhubo_id, '/album/', album_id
        
        # check the value in web page
        print 'Check album in webpage'
        session = XMLYSession()
        album = session.updateAlbum(url, 'check')
        print "\t Value in DB -- sound_count:", sound_count, '\t update_time:', update_time
        print '\t Value in Web -- sound_count:', album.sound_count, '\t update_time:', album.update_time
        
        # the value increase or fresh?
        if album.sound_count > sound_count or album.update_time > update_time:
            
            # sound_ids: buffer --> list
            sound_ids_db = pickle.loads(sound_ids_db)

            
            
            # update db
            print 'Album Nedd Update.'
            album = session.updateAlbum(url, 'getnew')
            
            playcount      =  album.playcount
            sound_ids_web     =  album.sound_ids 
            sound_count = album.sound_count   
            update_time  = album.update_time
            
            # buffer album_ids for BLOB
            sound_ids_buffer = buffer(pickle.dumps(sound_ids_web, pickle.HIGHEST_PROTOCOL))
            
            print 'Update album start.', zhubo_id, '/album/', album_id
            cur.execute('''UPDATE Album SET playcount = ?, sound_ids = ?, sound_count = ?,
                    update_time = ? WHERE album_id = ?''', (playcount, sound_ids_buffer,
                    sound_count, update_time, album_id))
                    
            conn.commit()
            print 'Update album Done.', zhubo_id, '/album/', album_id
            
            print "Update track start."
            # compare two sound_ids list
            sound_ids_compare = [sid for sid in sound_ids_web if sid not in sound_ids_db]
            if len(sound_ids_compare) > 1:
                
                for sound_id in sound_ids_compare:
                # for sound_id in sound_ids:
                    sound_url = HOME_URL + "/" + zhubo_id + "/sound/" + sound_id + "/"
                    
                    result = checkURL(sound_url)
                    if not result["url_type"]:
                        printUrlError()
                    else:
                        print '\nstart write the track into db. \n\t', sound_url
                        writeTrackToDB(conn, cur, sound_url, result)
                        print 'the track write into db done. \n\t', sound_url
            
            
            print "Update track Done."
            
        else:
            print "NO NEED for update."

        
    except TypeError:   # Album doesn't in db
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
        sound_ids_buffer = buffer(pickle.dumps(sound_ids, pickle.HIGHEST_PROTOCOL))
        
        print 'Write New Album start.', zhubo_id, '/album/', album_id
        cur.execute('''INSERT OR REPLACE INTO Album (album_id, zhubo_id, name, url,
        category, tag, playcount, sound_ids, sound_count, update_time) VALUES (?, ?, ?, ?,
        ?, ?, ?, ?, ?, ?)''', (album_id, zhubo_id, name, url,
        category, tag, playcount, sound_ids_buffer, sound_count, update_time))
                
        conn.commit()
        print 'Write New Album Done.', zhubo_id, '/album/', album_id
        
        print "Write Tracks of the Album Start."
        for sound_id in sound_ids:
            sound_url = HOME_URL + "/" + zhubo_id + "/sound/" + sound_id + "/"
            
            result = checkURL(sound_url)
            if not result["url_type"]:
                printUrlError()
            else:
                print '\nstart write the track into db. \n\t', sound_url
                writeTrackToDB(conn, cur, sound_url, result)
                print 'the track write into db done. \n\t', sound_url
        
        print "Write Tracks of the Album Done."
        
        
    except Exception, x:
        print x
        raise
    
def writeTrackToDB(conn, cur, url, result):
    zhubo_id = result["zhubo_id"]
    sound_id = result["sound_id"]
    
    # check if the Track exists in db ?
    cur.execute("SELECT play_path_64, play_path_32, play_path, title FROM Track WHERE sound_id = ?", (sound_id, ))
    
    try:
        data = cur.fetchone()
        play_path_64 = data[0]
        play_path_32 = data[1]
        play_path = data[2]
        title = data[3]
        print '\tTrack in database ', zhubo_id, '/sound/', sound_id
        
        # do download
        print '\tcheck done'
        
        
    except TypeError:
        print "\tTrack  doesn't in db:", zhubo_id, '/sound/', sound_id
        
        # Add new Track into db
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
        
        

        print '\tWrite New Track start.', zhubo_id, '/sound/', sound_id
        cur.execute('''INSERT OR REPLACE INTO Track (album_id, zhubo_id, sound_id, title,
        intro, duration, play_count, play_path_32, play_path_64, play_path, 
        category_name, shares_count, favorites_count) VALUES (?, ?, ?, ?,
        ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (album_id, zhubo_id, sound_id, title,
        intro, duration, play_count, play_path_32, play_path_64, play_path, 
        category_name, shares_count, favorites_count))
                
        conn.commit()
        print '\tWrite New Track Done.', zhubo_id, '/sound/', sound_id
        
        
    except Exception, x:
        print x
        raise
    
def prettyAlbumDir(album_name):
    """clean the album name, create album directory"""
    
    # pattern = r'[\\/:*?"<>|]'       # strip special chars for windows filename
    # album_name = re.sub(pattern, ' ', album_name)
    
    album_name = pretty_windows_filename(album_name)
    
    # check weather the album_title dir exist?
    album_dir = AUDIO_DIR + '\\' + album_name + '\\'
    if not os.path.isdir(album_dir):
        os.makedirs(album_dir)
        
    return album_name, album_dir
    
        
def m4aToMp3(m4a_path, mp3_path):
    """ convert all the m4a to mp3 in a directory and move all the mp3 to mp3 directory """
    if not os.path.isdir(m4a_path):
        os.makedirs(m4a_path)
    if not os.path.isdir(mp3_path):
        os.makedirs(mp3_path)
    
    # move all the mp3 file to mp3 directory
    filenames_mp3 = [
        filename for filename in os.listdir(m4a_path)
        if filename.endswith('.mp3')
        ]
        
    for filename in filenames_mp3:
        filename = filename
        # print '\n\nStart mp3_path:', type(mp3_path), mp3_path
        # print '\n\nStart m4a_path:', type(m4a_path), m4a_path
        # print '\n\nStart filename:', type(filename)
        # print repr(filename)
        src_mp3 = os.path.join(m4a_path, filename)
        # print src_mp3
        dst_mp3 = os.path.join(mp3_path, '%s.mp3' % filename[:-4])
        # print dst_mp3
        os.rename(src_mp3, dst_mp3)
        
        
    
    
    # convert all the m4a file to mp3 format to mp3 directory
    
    filenames_m4a = [
        filename for filename in os.listdir(m4a_path)
        if filename.endswith('.m4a')
        ]
        
    for filename in filenames_m4a:
        # filename = filename
        
        
        subprocess.call([
            "ffmpeg", "-i", 
            os.path.join(m4a_path, filename), 
            "-acodec", "libmp3lame", "-ab", "128k", 
            os.path.join(mp3_path, '%s.mp3' % filename[:-4])
            ])
        print '\n\nEnd#'
    # return 0
    
        
        
def downloadAlbum(conn, cur, url, result):
    "check the album status, and download all the tracks in the album."
    
    # check the album status
    writeAlbumToDB(conn, cur, url, result)
    
    zhubo_id = result["zhubo_id"]
    album_id = result["album_id"]
    
    # do download
    cur.execute("SELECT name, sound_count, sound_ids FROM Album  \
            WHERE zhubo_id = ? AND album_id = ?", (zhubo_id, album_id))
    
    try:
        out = cur.fetchone()
        album_name = out[0] 
        sound_count = out[1] 
        sound_ids = out[2] 
        sound_ids = pickle.loads(sound_ids)
        
               
        # get all the tracks in the album from db.
        cur.execute("SELECT title, play_path, play_path_32, play_path_64, downloaded, id, sound_id FROM Track \
                        WHERE downloaded = 0 AND album_id = ?", (album_id, ))
        rowcount = cur.rowcount
        print '\n\t this album has ', sound_count, 'tracks.'
        print '\n\t this album has ', rowcount, "tracks doesn't download."
        
        
        try:
            downloaded_dict = {}    # downloaded flag dictionary
            album_name, album_dir = prettyAlbumDir(album_name)
            
            print 'Start download track...'
            for row in cur:
                print '\t', row[0], row[2], row[3], row[4]
                track_title = row[0]
                play_path = row[1]
                play_path_32 = row[2]
                play_path_64 = row[3]
                downloaded = row[4]
                track_id = row[5]
                sound_id = row[6]
                track_suffix = '.' + play_path_64.split('.')[-1]
                
                track_pub_date = sound_ids.get(sound_id, '000000')
                # clean the file name for windows OS.
                track_title = pretty_windows_filename(track_title) 
                
                print "track_title:", type(track_title), track_title
                track_path = album_dir + track_pub_date + " " + track_title + track_suffix
                print '\t', track_path
                
                # download track with requests
                try:
                    rec_track = requests.get(play_path_64)
                    with open(track_path, "wb") as code:
                        code.write(rec_track.content)                    
                    time.sleep(1)
                    
                    print '\t\t track_id:', track_id
                    downloaded_dict[track_id] = 1
                    print '\t\t', downloaded_dict
                    
                except Exception, x:
                    print '\n download track error', x
                    # raise
                    
            # update downloaded
            try:
                for track_id, downloaded in downloaded_dict.items():
                    cur.execute("UPDATE Track SET downloaded = ? WHERE id = ?", (downloaded, int(track_id)))
                conn.commit()
            except Exception, x:
                print '\n update track downloaded error:', x
                raise
                
            # convert m4a to mp3
            print "\n\n -------- Convert m4a to mp3 start   ----------- "
            # print "album_dir:", album_dir
            
            m4a_path = album_dir
            mp3_path = album_dir + "mp3"
            # print "m4a_path:", type(m4a_path), m4a_path
            # print "mp3_path:", type(mp3_path), mp3_path
            if not os.path.isdir(mp3_path):  # for m4a convert
                os.makedirs(mp3_path)
            
            m4aToMp3(m4a_path, mp3_path)
            
                
        except Exception, x:
            print '\n get all the tracks error:', x
            raise
        
    except Exception, x:
        print '\n get album record error:', x
        raise
    
    pass
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
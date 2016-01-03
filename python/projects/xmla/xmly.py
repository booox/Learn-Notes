#coding=utf-8
import sqlite3
import re


HOME_URL = 'http://www.ximalaya.com'
DATA_BASE = 'xmly.sqlite'



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
            favorites_count       =   0
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
            favorites_count INTEGER
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
    
    
        
        
        
        
        
        
        
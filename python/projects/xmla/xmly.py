#coding=utf-8
import sqlite3
HOME_URL = 'http://www.ximalaya.com'
DATA_BASE = 'xmly.sqlite'




class Zhubo(object):
    def __init__(self, 
            zbid      = None,
            name = None,
            url         = None,
            fans        = 0,
            follow   = 0,
            sound      = 0,
            favorites   = 0,
            album_ids   = None,
            album_url   = None,
            desc        = None ):
        
        self.zbid = zbid
        self.name = name
        self.url = url
        self.fans = fans
        self.follow = follow
        self.sound = sound
        self.favorites = favorites
        self.album_ids = album_ids
        self.album_url = album_url
        self.desc = desc
        
        
class Album(object):
    def __init__(self,
            aid              = None,
            name        =   None,
            url             =   None,
            category   =   None,
            tag             =   None,
            playcount   =  0,
            sound_ids      =   None,
            update_time =   None):
            
        self.aid         =   aid
        self.name   =   name
        self.url   =   url
        self.category   =   category
        self.tag   =   tag
        self.playcount   =   playcount
        self.sound_ids   =   sound_ids
        self.update_time   =   update_time
        
class Sound(object):
    def __init__(self,
            sid      =   None,
            name    =   None,
            url         =   None,
            playcount  =   0,
            createtime  =   None,
            like        =   0,
            comment     =   0,
            forward         =   0
            ):
        
        self.sid                 =    sid
        self.name           =   name
        self.url                =   url
        self.playcount     =   playcount
        self.createtime    =   createtime
        self.like              =   like
        self.comment     =   comment
        self.forward        =   forward
        

       
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
            zbid TEXT UNIQUE,
            name TEXT,
            url TEXT,
            fans INTEGER,
            follow INTEGER,
            sound INTEGER,
            favorites INTEGER,
            album_ids BLOB,
            album_url TEXT,
            desc TEXT
        );
        
        CREATE TABLE IF NOT EXISTS Album (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            aid TEXT UNIQUE,
            name TEXT,
            url TEXT,
            category TEXT,
            tag BLOB,
            playcount INTEGER,
            sound_ids BLOB,
            update_time TEXT
        );
        
        CREATE TABLE IF NOT EXISTS Sound (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            sid TEXT UNIQUE,
            name TEXT,
            url TEXT,
            playcount INTEGER,
            createtime TEXT,
            like INTEGER,
            comment INTEGER,
            forward INTEGER
        );
        
    ''')
        
def queryDB(cur, column, table, field, value):          
    ''' query database by column from table '''
    
    cur.execute('SELECT ? FROM ? WHERE ? = ?',
        (column, table, field, buffer(value)))
        
    try:
        data = cur.fetchone()[0]
    except:
        raise




def checkURL(url):
    ''' simple check zhubo url '''
    
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
    
    url = url.lstrip('/')
    
    # sounds: 
    _type = None    # url type: zhubo, albums, album, sounds, sound
        
    
    if not url.startswith(HOME_URL):
        print "[URL ERROR] : The url outside of xmly."
        exit(1)
        
    # zhubo
    if 'zhubo' in url:
        zbid = url.split('/')[-1]       
        if not zbid.isdigit():
            print "[URL ERROR] : check Zhubo url."
            exit(1)
        _type = 'zhubo'
    elif 'album' in url:
        if url.endswith('album'):   # url = 'http://www.ximalaya.com/8889234/album/'  
            pass

        
    pass
        
        
        
        
        
        
        
        
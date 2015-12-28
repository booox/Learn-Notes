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
            album   = None,
            desc        = None ):
        
        self.zbid = zbid
        self.name = name
        self.url = url
        self.fans = fans
        self.follow = follow
        self.sound = sound
        self.favorites = favorites
        self.album = album
        self.desc = desc
        
        
class Album(object):
    def __init__(self,
            aid              = None,
            name        =   None,
            url             =   None,
            category   =   None,
            tag             =   None,
            playcount   =  0,
            sounds      =   None,
            update_time =   None):
            
        self.aid         =   aid
        self.name   =   name
        self.url   =   url
        self.category   =   category
        self.tag   =   tag
        self.playcount   =   playcount
        self.sounds   =   sounds
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
            zbid INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            name TEXT UNIQUE,
            url TEXT,
            fans INTEGER,
            follow INTEGER,
            sound INTEGER,
            favorites INTEGER,
            album TEXT,
            desc TEXT
        );
        
        CREATE TABLE IF NOT EXISTS Album (
            aid INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            name TEXT UNIQUE,
            url TEXT,
            category TEXT,
            tag TEXT,
            playcount INTEGER,
            sounds TEXT,
            update_time TEXT
        );
        
        CREATE TABLE IF NOT EXISTS Sound (
            sid INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            name TEXT UNIQUE,
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
    pass
    
    url_prefix = HOME_URL + '/zhubo/'
    zbid = url[len(HOME_URL + '/zhubo/'):].replace('/', '')
    
    if not url.startswith(url_prefix) or not zbid.isdigit():
        print "[URL ERROR] : Please check the zhubo homepage url."
        exit(1)
        
        
        
        
        
        
        
        
        
        
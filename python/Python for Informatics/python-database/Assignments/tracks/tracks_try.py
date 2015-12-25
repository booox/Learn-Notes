import xml.etree.ElementTree  as ET
import sqlite3


# connetc to sqlite
conn = sqlite3.connect('tracks.sqlite')
cur = conn.cursor()

# fresh database
cur.executescript('''
    DROP TABLE IF EXISTS Artist;
    DROP TABLE IF EXISTS Album;
    DROP TABLE IF EXISTS Genre;
    DROP TABLE IF EXISTS Track;
    
    CREATE TABLE Artist(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE
    );
    
    CREATE TABLE Album(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE,
        artist_id INTEGER
    );
    
    CREATE TABLE Genre(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE
    );
    
    CREATE TABLE Track(
        id INTEGER NOT NULL PRIMARY KEY 
            AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE,
        album_id INTEGER,
        genre_id INTEGER,
        len INTEGER, rating INTEGER, count INTEGER
    );''')

fname = raw_input('Enter file name:')
if(len(fname) < 1) : fname = 'Library.xml'


# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>
def findText(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key:
            found = True
    return None

stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')
print 'Dict count:', len(all)

for entry in all:
    if ( findText(entry, 'Track ID') is None ) : continue
    
    name = findText(entry, 'Name')
    artist = findText(entry, 'Artist')
    album = findText(entry, 'Album')
    genre = findText(entry, 'Genre')
    count = findText(entry, 'Play Count')
    rating = findText(entry, 'Rating')
    length = findText(entry, 'Total Time')
    
    if name is None or artist is None or album is None or genre is None:
        continue
        
    print name, genre, artist, album, genre
    
    cur.execute('''INSERT OR IGNORE INTO Genre (name)
        VALUES (?)''', (genre, ))
    cur.execute('SELECT id FROM Genre WHERE name = ?', (genre, ))
    genre_id = cur.fetchone()[0]
    
    cur.execute('''INSERT OR IGNORE INTO Artist (name)
        VALUES (?)''', (artist, ))
    cur.execute('SELECT id FROM Artist WHERE name = ?', (artist, ))
    artist_id = cur.fetchone()[0]
    
    cur.execute('''INSERT OR IGNORE INTO Album (name, artist_id)
        VALUES (?, ?)''', (album, artist_id))
    cur.execute('SELECT id FROM Album WHERE name = ?', (album, ))
    album_id = cur.fetchone()[0]
    
    cur.execute('''INSERT OR REPLACE INTO Track 
        (name, album_id, genre_id, len, rating, count)
        VALUES (?, ?, ?, ?, ?, ?)''',
        (name, album_id, genre_id, length, rating, count))
    
    conn.commit()
    
    
    
    
    
    
    
    
    
    
    
import sqlite3
import pickle

conn = sqlite3.connect("xmly.sqlite")
cur = conn.cursor()

zhubo_id = '36774850'
cur.execute("SELECT zhubo_id, album_count, album_ids, sound_count, sound_ids FROM Zhubo WHERE zhubo_id = ?",(zhubo_id, ))

data = cur.fetchone()
zhubo_id = data[0]


zhubo_id = data[0]
album_count = data[1]
album_ids = pickle.loads(data[2])
sound_count = data[3]
sound_ids = pickle.loads(data[4])
print "\tzhubo_id in database ", zhubo_id
print zhubo_id, album_count, sound_count
print 'Album ids:', album_ids
print 'Sound ids:', sound_ids

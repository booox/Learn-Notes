import sqlite3
import pickle

conn = sqlite3.connect("xmly.sqlite")
cur = conn.cursor()

album_id = '2754031'
cur.execute("SELECT tag, sound_count, sound_ids, update_time FROM Album WHERE album_id = ?",(album_id, ))

data = cur.fetchone()

tag = pickle.loads(data[0])
sound_count = data[1]
sound_ids = pickle.loads(data[2])
update_time = data[3]




print "\t album_id in database ", album_id
print update_time, sound_count
print 'tag:', tag
print 'Sound ids:', sound_ids

for t in tag:
    print t.decode('utf-8')

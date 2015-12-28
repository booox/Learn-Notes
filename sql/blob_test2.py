import sqlite3
import datetime
import time 
import pickle

# Create DB
dbpath = 'test2.db'
db = sqlite3.connect(dbpath)
cursor=db.cursor()
cursor.execute("""           
    CREATE TABLE IF NOT EXISTS trials (
    timestamp INTEGER PRIMARY KEY, emg BLOB) """)
cursor.execute ('DELETE FROM trials')
# Define vars
now = datetime.datetime.now()
timestamp = time.mktime(now.timetuple())
emg = list(range(200))
s = pickle.dumps(emg, pickle.HIGHEST_PROTOCOL)

# Store vars
cursor.execute("""
    INSERT INTO trials VALUES (?,?)""", (timestamp, buffer(s)))
db.commit()

# Fetch vars
cursor.execute("""
    SELECT * FROM trials WHERE timestamp = ?""", (timestamp,))
out = cursor.fetchone()
s1 = out[1] 
emg1 = pickle.loads(s1)

print emg1
print emg1[0], emg1[:5]
print 15 in emg1
print 'abc' in emg1

# Test equality
print(emg1 == emg)
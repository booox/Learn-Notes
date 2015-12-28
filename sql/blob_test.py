import sqlite3
import datetime
import time
import pickle

dbname = 'test.sqlite3'
conn = sqlite3.connect(dbname)
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS Test ( 
        timestamp INTEGER PRIMARY KEY, emg BLOB) """)

now = datetime.datetime.now()
timestamp = time.mktime(now.timetuple())
emg = list(range(200))
s = pickle.dumps(emg, pickle.HIGHEST_PROTOCOL)

cur.execute("""
    INSERT INTO Test VALUES ( ?, ? )""", (timestamp, s))
conn.commit()


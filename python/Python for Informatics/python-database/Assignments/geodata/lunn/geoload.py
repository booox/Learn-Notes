import urllib, urllib2
import sqlite3
import json
import time


serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
apikey = 'AIzaSyDeQfDlkgOIOIC_4eW0foaMn2xctFH_yok'

# connect db
conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()

# db init
cur.execute('''
    CREATE TABLE IF NOT EXISTS Locations ( address TEXT, geodata TEXT)
    ''')
    
fh = open('where.data')
count = 0
for line in fh:
    if count > 2 : break
    address = line.strip()
    print ''
    
    # check data if exists
    cur.execute("SELECT geodata FROM Locations WHERE address = ?",
        (buffer(address), ))
        
    try:
        data = cur.fetchone()[0]
        print 'Found in database : ', address
        continue
    except:
        pass
        
    # retrieve the data
    print 'Resolving : ', address
    url = serviceurl + urllib.urlencode({"sensor":"false", "address":address})
    url = url + '&key=' + apikey
    print 'Retrieving : ', url
    uh = urllib2.urlopen(url)
    data = uh.read()
    print 'Retrieved : ', len(data), 'characters', data[:20]. replace('\n', ' ')
    count = count + 1
    
    # load json
    try:
        js = json.loads(str(data))
        print js    # error?
    except:
        continue
        
    if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS'):
        print '\n==== Failure to Retrieve ===='
        print data
        break
    
    cur.execute('''
        INSERT INTO Locations (address, geodata) VALUES ( ?, ? )''',
        ( buffer(address), buffer(data) ) )
        
    conn.commit()
    time.sleep(1)
    
print '\n==== Retrieved Success ===='
print "Run geodump.py to read the data from the database so you can vizualize it on a map."
    
    
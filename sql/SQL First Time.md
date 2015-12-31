
> 这里记录一些与SQL/Sqlite3/Database相关的第一次知道的，或一直理解错的。

* SQL,
    * `INSERT OR IGNORE INTO` 忽略重复数据的插入
    * `INSERT OR REPLACE INTO ` 如果该行不存在，则插入；如果存在，则替换之
        * 这比`UPDATE`要好一些：因为当该行不存在时，则`UPDATE`不会有任何操作
	
* Sqlite3处理Blob
    * Write into Sqlite3:
        * `stuff = buffer(pickle.dumps(range(50), pickle.HIGHEST_PROTOCOL))`
            * [Store sequences of data in sqllite3 (blob)](http://stackoverflow.com/questions/18080081/store-sequences-of-data-in-sqllite3-blob)
            * [sqlite3二进制文件存储问题](http://www.tuicool.com/articles/viaUne)
        * `stuff = sqlite3.Binary(range(50))`
        * 将包含中文字符的`list`用pickle处理时一直提示:
            * `RuntimeError: maximum recursion depth exceeded`好像是递归调用超过一定次数时触发的
            * 解决：将中文字符用`utf-8`编码，`s.encode('utf-8')` 然后再用pickle.loads就可以了
            * 
    * Read from Sqlite3
        * `stuff = pickle.loads(something_from_sqlite3)`
        
        ```
            # Create DB
            dbpath = './test.db'
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
                INSERT INTO trials VALUES (?,?)""", (timestamp,s))
            db.commit()

            # Fetch vars
            cursor.execute("""
                SELECT * FROM trials WHERE timestamp = ?""", (timestamp,))
            out = cursor.fetchone()
            s1 = out[1] 
            emg1 = pickle.loads(s1)

            # Test equality
            print(emg1 == emg)        
        ```
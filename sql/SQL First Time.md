
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

            # get all the records
            # There are two ways to do this
            # The First One is Recommanded.
            
            # First One
            cur.execute("SELECT c FROM t")
            for row in cursor:
                print row[0]
                
            # Second One
            cur.execute("SELECT c FROM t")
            for row in cursor.fetchall():
                print row[0]
            
            
        ```
        [Is sqlite3 fetchall necessary?](http://stackoverflow.com/questions/21334767/is-sqlite3-fetchall-necessary)
        
* Sqlite3存储、读取中文数据
    *. 存储中文text时，用utf-8编码
        ` sutff.encode('utf-8') `
        
    *. Text字符集？ text_factory
        ```
        def connect_db():
            """Connects to the specific database."""
            conn = sqlite3.connect(app.config['DATABASE'])
            conn.text_factory = str
            return conn        
        ```
        * 若没有设置，则在显示时会出错：
        ```
        sqlite3.ProgrammingError
ProgrammingError: You must not use 8-bit bytestrings unless you use a text_factory that can interpret 8-bit bytestrings (like text_factory = str). It is highly recommended that you instead just switch your application to Unicode strings.
        
        ```
        
        
    *. 显示时，设置页面字符集
    ```
        import sys
        reload(sys)
        sys.setdefaultencoding('utf-8')
    
    ```
        * 如果没有设置此行，则提示：
        ```
        UnicodeDecodeError: 'ascii' codec can't decode byte 0xe5 in position 0: ordinal not in range(128)
        
        ```
    
* set default values & alter table
    `ALTER TABLE t ADD COLUMN c INTEGER DEFAULT 0;`
    
    * but sqlite3 doesn't support DROP A COLUMN
       `ALTER TABLE t DROP COLUMN c` , THIS DOESN'T WORK.
        * The following steps illustrate how this could be done:
            ```
                BEGIN TRANSACTION;
                CREATE TEMPORARY TABLE t1_backup(a,b);
                INSERT INTO t1_backup SELECT a,b FROM t1;
                DROP TABLE t1;
                CREATE TABLE t1(a,b);
                INSERT INTO t1 SELECT a,b FROM t1_backup;
                DROP TABLE t1_backup;
                COMMIT;
            
            ```
       
        * create a new table with all the columns and data we want to save
            `CREATE TABLE my_table_temp AS (SELECT id, user_id, latitude, longitude FROM my_table);`
        * Then we drop the old table
            `DROP my_table;`
        * rename our new table with the old name
            `ALTER TABLE my_table_temp RENAME TO my_table`
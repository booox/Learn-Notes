
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
    * Read from Sqlite3
        * `stuff = pickle.loads(something_from_sqlite3)`
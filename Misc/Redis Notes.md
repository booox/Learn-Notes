
# Quick Started

## Install

* Download, extract and compile Redis with:
    ```
        $ sudo yum install redis
            (CentOS 6.4, 2016-3-14)
    ```
    
## Try Redis

* [try.redis.io](http://try.redis.io/)
* Commands
    * *SET* : 
        `SET server:name "fido"` 
    * *GET* :
        `GET server:name` 
    * *INCR* : 
        `SET connections 10`
        `INCR connections => 11`
        `INCR connections => 12`
    * *DEL* : 
        `DEL connections`
        `INCR connections => 1`
    * *EXPIRE* : 
        `SET resource:lock "Redis Demo 1"`
        `EXPIRE resource:lock 60`
    * *TTL* : 
        `TTL resource:lock => 39`
        `TTL resource:lock => 19`
        `SET test:v 30`
        `TTL test:v => -1`    (never expire)
    
## Data structures
### Lists
    * *RPUSH* : puts the new value at the end of the list
        `RPUSH friends "Alice"`
        `RPUSH friends "Bob"`
    * *LPUSH* : puts the new value at the start of the list
        `LPUSH friends "Sam"`
        
    * *LRANGE* : gives a subset of the list.
        `LRANGE friends 0 -1 => 1) "Sam", 2) "Alice", 3) "Bob"` 
            * *-1*, until the end of the list
        `LRANGE friends 0 1 => 1) "Sam", 2) "Alice"`
        `LRANGE friends 1 2 => 1) "Alice", 2) "Bob"`
    * *LLEN* : length of the list
        `LLEN friends => 3`
    * *LPOP* : remove the first elemnet from the list and return it.
        ` LPOP friends => "Sam"`
    * *RPOP* : remove the last element from the list and return it.
        `RPOP friends => "Bob"`
    * Note that the list now only has one element.
        ` LLEN friends => 1`
        `LRANGE friends 0 -1 => 1) "Alice" `
    * ** : 
### Set
    * A set is similar to a list, except it does not have a specific order
    * And each element may only appear once.
#### Some import commands with sets 
    * *SADD* *SREM* *SISMEMBER* *SMEMBERS* AND *SUNION*
    * *SADD* : adds the given value to the set.
        `SADD superpowers "flight" `
        `SADD superpowers "x-ray vision" `
        `SADD superpowers "reflexes" `
    * *SREM* : removes the given value from the set.
        `SREM superpowers "reflexes"`
    * *SISMEMBER* : tests if the given value is in the set.
        `SISMEMBER superpowers "flight" => 1`
        `SISMEMBER superpowers "reflexes" => 0`
    * *SMEMBERS* : returns a list of all the members of this set.
        `SMEMBERS superpowers => 1) "flight", 2) "x-ray vision"`
    * *SUNION* : combines two or more sets and returns the list of all elements.
        `SADD birdpowers "pecking"`
        `SADD birdpowers "flight"`
        `SUNION superpowers birdpowers => 1) "pecking", 2) "x-ray vision", 3) "flight"`
### Sorted Sets
    * A sorted set is similar to a regular set, but now each value has an associated score.
    * *ZADD* : 
        ```
        ZADD hackers 1940 "Alan Kay"
        ZADD hackers 1906 "Grace Hopper"
        ZADD hackers 1953 "Richard Stallman"
        ZADD hackers 1965 "Yukihiro Matsumoto"
        ZADD hackers 1916 "Claude Shannon"
        ZADD hackers 1969 "Linus Torvalds"
        ZADD hackers 1957 "Sophie Wilson"
        ZADD hackers 1912 "Alan Turing"
        
        ```
    * *ZRANGE* : 
        ```
            > ZRANGE hackers 0 1
            1) "Grace Hopper"
            2) "Alan Turing"
            > ZRANGE hackers 0 -1
            1) "Grace Hopper"
            2) "Alan Turing"
            3) "Claude Shannon"
            4) "Alan Kay"
            5) "Sophie Wilson"
        ```
### Hashes
    * Hashes are maps between string fields and string values.
    
    * *HSET* : set a value to a string field
        ```
            HSET user:1000 name "John Smith"
            HSET user:1000 email "john.smith@example.com"
            HSET user:1000 password "s3cret"        
        ```
        
    * *HGETALL* : to get back the saved data.
        `HGETALL user:1000`
    * *HMSET* : set multiple fields at once.
        `HMSET user:1001 name "Mary Jones" password "hidden" email "mjones@example.com"`
    * *HGET* : get a single field value
        `HGET user:1001 name => "Mary Jones"`
    * *HINCRBY* : increment this value in an atomic way.
        ```
            HSET user:1000 visits 10
            HINCRBY user:1000 visits 1 => 11
            HINCRBY user:1000 visits 10 => 21
            HDEL user:1000 visits
            HINCRBY user:1000 visits 1 => 1        
        ```
    * *HDEL* : 
    
    * ** : 

    
    
    


# Chapter 1 A Sneak Preview

## STep 1 : Representing Records

### Using Lists


```
    >>> bob = ['Bob Smith', 42, 30000, 'software']
    >>> sue = ['Sue Jones', 45, 40000, 'hardware']
	
    >>> bob[0], sue[2]		# fetch name, pay
    ('Bob Smith', 40000)
	
    >>> bob[0].split()[-1]		# What's bob's last name?
    'Smith'
    >>> sue[2] *= 1.25			# give sue a 25% raise
	
    >>> sue
    ['Sue Jones', 45, 50000.0, 'hardware']
    >>> bob[2] = bob[2] * 1.25
    >>> bob
    ['Bob Smith', 42, 37500.0, 'software']
    >>> 
    >>> people = [bob, sue]
    >>> for person in people:
        print person

        
    ['Bob Smith', 42, 37500.0, 'software']
    ['Sue Jones', 45, 50000.0, 'hardware']
    >>> people[1][0]
    'Sue Jones'
    >>> for person in people:
        print person[0].split()[-1]
        person[2] *= 1.20

        
    Smith
    Jones
    >>> for person in people: print person[2]

    45000.0
    60000.0
    >>> 
    >>> pays = [person[2] for person in people]
    >>> pays
    [45000.0, 60000.0]
    >>> sum(person[2] for person in people)
    105000.0
    >>> 
    >>> people.append(['Tom', 50, 0, None])
    >>> len(people)
    3
    >>> people[-1][0]
    'Tom'
    >>> 
```	
	
### Using Dictionaries
```
	>>> bob = {'name': 'Bob Smith', 'age': 42, 'pay': 30000, 'job': 'dev'}
	>>> sue = {'name': 'Sue Jones', 'age': 45, 'pay': 40000, 'job': 'hdw'}

	>>> bob['name'], sue['pay']		# not bob[0], sue[2]
	('Bob Smith', 40000)
	
	>>> bob['name'].split()[-1]			
	'Smith'
	
	>>> sue['pay'] *= 1.10
	>>> sue['pay']
	44000.0
```
	
#### Other ways to make dictionaries

- With keyword arguments and the type constructor:

```
	>>> bob = dict(name='Bob Smith', age=42, pay=30000, job='dev')
	>>> sue = dict(name='Sue Jones', age=45, pay=40000, job='hdw')
	>>> bob
	{'pay': 30000, 'job': 'dev', 'age': 42, 'name': 'Bob Smith'}
	>>> sue
	{'pay': 40000, 'job': 'hdw', 'age': 45, 'name': 'Sue Jones'}	
```
	
- Filling out a dictionary one field at a  time
```
	>>> sue = {}
	>>> sue['name'] = 'Sue Jones'
	>>> sue['age'] = 45
	>>> sue['pay'] = 40000
	>>> sue['job'] = 'hdw'
	>>> sue
```	
	
- Zipping together name/value lists:

```
	>>> names = ['name', 'age', 'pay', 'job']
	>>> values = ['Sue Jones', 45, 40000, 'hdw']
	>>> list(zip(names, values))
	[('name', 'Sue Jones'), ('age', 45), ('pay', 40000), ('job', 'hdw')]
	>>> sue = dict(zip(names, values))
	>>> sue
	{'job': 'hdw', 'pay': 40000, 'age': 45, 'name': 'Sue Jones'}
```
	
- From a sequence of key values and an optional starting value for all the keys(handy to initialize an empty dictionary):

```
	>>> fields = ('name', 'age', 'pay', 'job')
	>>> record = dict.fromkeys(fields, '?')
	>>> record
	{'job': '?', 'pay': '?', 'age': '?', 'name': '?'}	
```	
#### Lists of dictionaries
	
- 	Collect our dictionary-based records into a database

```
>>> bob
{'job': 'dev', 'pay': 30000, 'age': 42, 'name': 'Bob Smith'}
>>> sue
{'job': 'hdw', 'pay': 40000, 'age': 45, 'name': 'Sue Jones'}
>>> people = [bob, sue]                         # reference in a list
>>> for person in people:
	print person['name'], person['pay']        # all name, pay

	
Bob Smith 30000
Sue Jones 40000
>>> for perpon in people:
	if person['name'] == 'Sue Jones':           # fetch sue's pay
		print person['pay']

		
40000
```

- Iteration tools work just as well here, but we use keys rather than obsure positions.

```
>>> names = [person['name'] for person in people]           # collect names
>>> names
['Bob Smith', 'Sue Jones']

>>> list(map((lambda x: x['name']), people))                    # ditto, generate
['Bob Smith', 'Sue Jones']

>>> sum(person['pay'] for person in people)                     # sum all pay
70000
	
```	
    
- SQL queries

```
>>> [rec['name'] for rec in people if rec['age'] >= 45]
['Sue Jones']

>>> [(rec['pay'] + 5000 if rec['pay'] < 40000 else rec['pay']) for rec in people]
[35000, 40000]

>>> G = [rec['name'] for rec in people if rec['age'] >= 45]     # Error
>>> next(G)

Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    next(G)
TypeError: list object is not an iterator
>>> G = (rec['name'] for rec in people if rec['age'] >= 45)     # Notice: **Here is a Generator, not a list .**
>>> next(G)
'Sue Jones'

>>> G = ((rec['pay'] + 5000 if rec['pay'] < 40000 else rec['pay']) for rec in people)
>>> G.__next__()                                                            # Error : **for python 3.x**
Traceback (most recent call last):          
  File "<pyshell#13>", line 1, in <module>
    G.__next__()
AttributeError: 'generator' object has no attribute '__next__'
>>> G.next
<method-wrapper 'next' of generator object at 0x0000000002B14090>
>>> G.next()
35000

    
```    

- Update records

```
>>> for person in people:
	print (person['name'].split()[-1])
	person['pay'] *= 1.10

	
Smith
Jones
>>> for person in people: print person['pay']

33000.0
44000.0

```

#### Nested structures

```
    >>> bob2 = {'name': {'first': 'Bob', 'last': 'Smith'},
                          'age': 42,
                          'job': ['software', 'writing'],
                          'pay': (40000, 50000)}
                          
    >>> bob2['name']
```




## Step 2: Storing Records Persistently

### Using Formatted Files

> One way to keep our data around between program runs is to write all the data out to a simple text file, in a formatted way.

#### Test data script

> Example 1-1: create a database with dictionary.

```
    # Example 1-1
    # records
    bob = {'job': 'dev', 'pay': 30000, 'age': 42, 'name': 'Bob Smith'}
    sue = {'job': 'hdw', 'pay': 40000, 'age': 45, 'name': 'Sue Jones'}
    tom = {'job': None, 'pay': 0, 'age': 50, 'name': 'Tom'}

    #database
    db = {}
    db['bob'] = bob
    db['sue'] = sue
    db['tom'] = tom

    if __name__ == '__main__':      # when run as a script
        print type(db)
        print db
        print 
        for value in db.values():
            # print(key, '=>\n    ', db[key])
            # print key, '=>\n    ', db[key]
            print value
```


#### Script start-up pointers

- On most Windows system you can just type the file's name to run it.
- Add an *input()* call to the bottom of the script to keep the output window up.

#### Data format script

> Example 1-2 writes the database (Example 1-1) out to a flat file.

```
    # # Example 1-2
from __future__ import print_function

dbfilename = 'people-file.txt'
ENDDB = 'enddb.'
ENDREC = 'endrec.'
RECSEP = '=>'

def storeDbase(db, dbfilename=dbfilename):
    "formatted dump of database to flat file"
    
    dbfile = open(dbfilename, 'w')
    
    for key in db.keys():
        print(key, file=dbfile)     # key
        
        for (k, v) in db[key].items():
            print (k, '=>', v, file=dbfile) # loop value
        print ('endrec.', file=dbfile)
        
    print ('enddb.', file=dbfile)
    

def loadDbase(dbfilename=dbfilename):
    "parse data to reconstruct database"
    
    dbfile = open(dbfilename)
    import sys
    sys.stdin = dbfile
    db = {}
    key = input()
    while key != ENDDB:
        rec = {}
        field = input()
        while field != ENDREC:
            name, value = field.split(RECSEP)
            rec[name] = eval(value)
            field = input()
        db[key] = rec
        key = input()
        
    return db





if __name__ == '__main__':
    from initdata import db
    storeDbase(db)

```

#### Utility scripts

> Example 1-3 reloads the database from a file each time it is run.

```


```














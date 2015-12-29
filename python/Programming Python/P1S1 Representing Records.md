

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



#### Dictionaries of dictionaries

- The outer dictionary is the database, and the nested dictionaries are the records within it.
	**We can access a record directly by indexing on key,  without a loop**

```
	>>> bob = dict(name='Bob Smith', age=42, pay=30000, job='dev')
	>>> sue = dict(name='Sue Jones', age=45, pay=40000, job='hdw')
	>>> bob
	{'pay': 30000, 'job': 'dev', 'age': 42, 'name': 'Bob Smith'}
	>>> db = {}
	>>> db['bob'] = bob
	>>> db['sue'] = sue
	>>> 
	>>> db['bob']['name']
	'Bob Smith'
	>>> db['sue']['pay'] = 50000
	>>> db['sue']['pay']
	50000

```

- *pprint* pretty-printer module

```
	>>> db
	{'bob': {'pay': 30000, 'job': 'dev', 'age': 42, 'name': 'Bob Smith'}, 'sue': {'pay': 50000, 'job': 'hdw', 'age': 45, 'name': 'Sue Jones'}}
	>>> import pprint
	>>> pprint.pprint(db)
	{'bob': {'age': 42, 'job': 'dev', 'name': 'Bob Smith', 'pay': 30000},
	 'sue': {'age': 45, 'job': 'hdw', 'name': 'Sue Jones', 'pay': 50000}}
```

- Through dictionary iterators, step through the database one record at a time.

```
	>>> for key in db:
				print key, '=>', db[key]['name']

	bob => Bob Smith
	sue => Sue Jones
	
	
	>>> for key in db:
		print db[key]['name'].split()[-1]
		db[key]['pay'] *= 1.10

		
	Smith
	Jones	
```

- Step through the dictionary's values

```
	>>> for record in db.values(): print record['pay']

	33000.0
	55000.0
	>>> x = [db[key]['name'] for key in db]
	>>> x
	['Bob Smith', 'Sue Jones']
	>>> x = [rec['name'] for rec in db.values()]
	>>> x
	['Bob Smith', 'Sue Jones']

```

- Add a new record

```
	>>> db['tom'] = dict(name='Tom', age=50, job=None, pay=0)
	>>> db['tom']
	{'pay': 0, 'job': None, 'age': 50, 'name': 'Tom'}
	>>> db['tom']['name']
	'Tom'
	>>> list(db.keys())
	['bob', 'sue', 'tom']
	>>> len(db)
	3
	>>> [rec['age'] for rec in db.values()]
	[42, 45, 50]
	>>> [rec['name'] for rec in db.values() if rec['age'] >= 45]
	['Sue Jones', 'Tom']
```


## STep 2 : Storing Records Persistently

### Using Formatted Files

#### Test data script

- Initialize data to be stored in files, pickles, shelves

```
	# records
	bob = {'pay': 30000, 'job': 'dev', 'age': 42, 'name': 'Bob Smith'}
	sue = {'job': 'hdw', 'pay': 40000, 'age': 45, 'name': 'Sue Jones'}
	tom = {'pay': 0, 'job': None, 'age': 50, 'name': 'Tom'}

	#database
	db = {}
	db['bob'] = bob
	db['sue'] = sue
	db['tom'] = tom

	if __name__ == '__main__':          # When run as a script
		for key in db:
			print key, '=>\n    ', db[key]
			
```

	** __name__** : when this file is run, not when it is imported

 - Script start-up pointers
	- On most Windows: you can just type the file's name to run it
	- On windows: add an input() call to the bottom of the script to keep the output window up.

#### Data format script
=======
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
    # Example 1-1 : initdata.py
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
    # # Example 1-2: make_db_file.py
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
    key = raw_input()						# NOTICE: input()  -- python 3.x
    while key != ENDDB:
        rec = {}
        field = raw_input()
        while field != ENDREC:
            name, value = field.split(RECSEP)
            rec[name] = eval(value)
            field = raw_input()
        db[key] = rec
        key = raw_input()
        
    return db


if __name__ == '__main__':
    from initdata import db
    storeDbase(db)

```

#### Utility scripts

> Example 1-3 reloads the database from a file each time it is run.

```
	## Example 1-3:: dump_db_file.py
    
	import make_db_file

	db = make_db_file.loadDbase()
	for key in db:
		print key, '=>\n  ', db[key]
	print db['sue']['name']
	
    

```
> Run 

```
    > dump_db_file.py
    bob =>
       {'pay': 30000, 'job': 'dev', 'age': 42, 'name': 'Bob Smith'}
    sue =>
       {'pay': 40000, 'job': 'hdw', 'age': 45, 'name': 'Sue Jones'}
    tom =>
       {'pay': 0, 'job': None, 'age': 50, 'name': 'Tom'}
    Sue Jones

```

> Example 1-4 makes changes by loading, updating, and storing again.

```
	## Example 1-3:: update_db_file.py
    
    import make_db_file

    db = make_db_file.loadDbase()

    db['sue']['pay'] *= 1.10
    db['tom']['name'] = 'Tom Tom'

    make_db_file.storeDbase(db)

```

```
    > update_db_file.py

    > dump_db_file.py
    bob =>
       {'pay': 30000, 'job': 'dev', 'age': 42, 'name': 'Bob Smith'}
    sue =>
       {'pay': 44000.0, 'job': 'hdw', 'age': 45, 'name': 'Sue Jones'}
    tom =>
       {'pay': 0, 'job': None, 'age': 50, 'name': 'Tom Tom'}
    Sue Jones

```

#### Utility Pickle Files

> Limitations of the formatted text file scheme
    
    * Has to read the entire database from the file just to fetch one record
    * Must write the entire database back to the file after each set of updates.
    * Separators will not appear in the data to be stored ( `"=>"`)
    
> The `pickle` module translates an in-memory Python object into a serialized byte stream -- a string of bytes that can be written to any file-like object.



* Shows how to store our records in a flat file, using pickle.

```
	## Example 1-5:: make_db_pickle.py
    
    from initdata import db
    import pickle

    dbfile = open('people-pickle', 'w')     # use `wb` binary mode in 3.x
    pickle.dump(db, dbfile)
    dbfile.close()

```

* Shows how to access the pickled database after it has been created
    
```
	## Example 1-6:: dump_db_pickle.py
    
    import pickle

    dbfile = open('people-pickle', 'r')     # use `rb` binary mode in 3.x
    db = pickle.load(dbfile)

    for key in db:
        print key, '=>\n   ', db[key]
        
    print db['sue']['name']

```

* Updating with a pickle file
    
```
	## Example 1-7:: update_db_pickle.py
    
    import pickle

    dbfile = open('people-pickle', 'r')     # use `rb` binary mode in 3.x
    db = pickle.load(dbfile)
    dbfile.close()

    db['sue']['pay'] *= 1.10
    db['tom']['name'] = 'Tom Tom'

    dbfile = open('people-pickle', 'w')
    pickle.dump(db, dbfile)
    dbfile.close()
    
```

#### Using Per-Record Pickle Files

* Stores each record in its own flat file, using each record's original key as its filename with a .pkl appended

    ```
    # Example 1-8. PP4E\Preview\make_db_pickle_recs.py
    
    from initdata import bob, sue, tom
    import pickle

    for (key, record) in [('bob', bob), ('tom', tom), ('sue', sue)]:
        recfile = open(key + '.pkl', 'w')
        pickle.dump(record, recfile)
        recfile.close()

    ```

* Dumps the entire database by using the standard library's `glob` module to do filename expansion and thus collect all the files in this directory with a `.pkl` extension.

    ```
    # Example 1-9. PP4E\Preview\dump_db_pickle_recs.py
    
    import pickle, glob
    for filename in glob.glob('*.pkl'):         # for 'bob','sue','tom'
        recfile = open(filename, 'rb')
        record  = pickle.load(recfile)
        print(filename, '=>\n  ', record)
    suefile = open('sue.pkl', 'rb')
    print(pickle.load(suefile)['name'])         # fetch sue's name

    ```

* Updates the database by fetching a record from its file, changing it in memory, and then writing it back to its pickle file.

```
    # Example 1-10. PP4E\Preview\update_db_pickle_recs.py
    
    import pickle

    suefile = open('sue.pkl', 'r')
    sue = pickle.load(suefile)
    suefile.close()

    sue['pay'] *= 1.10

    suefile = open('sue.pkl', 'w')
    pickle.dump(sue, suefile)
    suefile.close()

```    

> The filesystem becomes our top-level dictionary -- filenames provide direct access to each record.


#### Using Shelves

> Shelves automatically pickle objects to and from a keyed-access filesystem.The shelve system automatically splits up stored records and fetches and updates only those records that are accessed and changed. In this way, shelves provide utility similar to per-record pickle files, but they are usually easier to code.

* Store our in-memory dictionary objects in a shelve for permanent keeping.

```
    # Example 1-11. PP4E\Preview\make_db_shelve.py
    
    from initdata import bob, sue
    import shelve

    db = shelve.open('people-shelve')
    db['bob'] = bob
    db['sue'] = sue
    db.close()

```
> This script creates one or more files in the current directory with the name `people-shelve` as a prefix (such as: `people-shelve.bak`, `people-shelve.dat`, `people-shelve.dir`.)


* Reopen the shelve and indexes it by key to fetch its stored records.

```
    # Example 1-12. PP4E\Preview\dump_db_shelve.py
    
    import shelve

    db = shelve.open('people-shelve')

    for key in db:
        print key, '=>\n    ', db[key]
        
    print db['sue']['name']
    db.close()
```

> We still have a dictionary of dictionaries here, but the top-level dictionary is really a shelve mapped onto a file.

* Shelve Update

```
    # Example 1-13. PP4E\Preview\update_db_shelve.py
    
    from initdata import tom
    import shelve

    db = shelve.open('people-shelve')
    sue = db['sue']                                 # fetch sue
    sue['pay'] *= 1.50
    db['sue'] = sue                                 # update sue
    db['tom'] = tom                                 # add a new record
    db.close()


```
    
## Step 3: Stepping Up to OOP

> What we'd like is a way to bind processing logic with the data stored in the database in order to make it easier to understand, debug, and reuse.

* OOP attractive things:
    * **Structure** : We can naturally associate processing logic with record data -- classes.
    * **Encapsulation** : Wrap up details such as name processing behind method functions.
    * **Customization** : Natural growth path. Classes can be extended and customized by coding new subclasses, without changing or breaking already working code.
    
> Under OOP, we program by customizing and reusing, not by rewriting.

### Using Classes

* Implements our database records as class instances rather than as dictionaries.

```
    # Example 1-14. PP4E\Preview\person_start.py
    
    class Person:
        def __init__(self, name, age, pay=0, job=None):
            self.name = name
            self.age = age
            self.pay = pay
            self.job = job
            
    if __name__ == '__main__':
        bob = Person('Bob Smith', 42, 30000, 'software')
        sue = Person('Sue Jones', 45, 40000, 'hardware')
        print bob.name, sue.pay
        
        print bob.name.split()[-1]
        sue.pay *= 1.10
        print sue.pay
        
```

* This isn't a database yet, but we could stuff these objects into a list or dictionary as before in order to collect them as a unit.

```
    >>> from person_start import Person
    >>> bob = Person('Bob Smith', 42)
    >>> sue = Person('Sue Jones', 45, 40000)
    >>> people = [bob, sue]                          # a "database" list
    >>> for person in people:
            print(person.name, person.pay)
    Bob Smith 0
    Sue Jones 40000
    >>> x = [(person.name, person.pay) for person in people]
    >>> x
    [('Bob Smith', 0), ('Sue Jones', 40000)]
    >>> [rec.name for rec in people if rec.age >= 45]     # SQL-ish query
    ['Sue Jones']
    >>> [(rec.age ** 2 if rec.age >= 45 else rec.age) for rec in people]
    [42, 2025]

```
    
### Adding Behavior

> To really leverage the power of classes, we need to add some behavior.    
  
* Adds the last-name and raise logic as class methods
* Methods use the `self` argument to access or update the instance(record) being processed.

```
    # Example 1-15. PP4E\Preview\person.py
    
    class Person:
        def __init__(self, name, age, pay=0, job=None):
            self.name = name
            self.age = age
            self.pay = pay
            self.job = job
            
        def lastName(self):
            return self.name.split()[-1]
        def giveRaise(self, percent):
            self.pay *= (1.0 + percent)
            
    if __name__ == '__main__':
        bob = Person('Bob Smith', 42, 30000, 'software')
        sue = Person('Sue Jones', 45, 40000, 'hardware')
        print bob.name, sue.pay
        
        print bob.lastName()
        sue.giveRaise(.10)
        print sue.pay
        
```

### Adding Inheritance

* Customizes the last section's Person class in order to give a 10 percent bonus by default to managers whenever they receive a raise.

```
    # Example 1-16. PP4E\Preview\manager.py
    
    from person import Person

    class Manager(Person):
        def giveRaise(self, percent, bonus=0.1):
            self.pay *= (1.0 + percent + bonus)
            
    if __name__ == '__main__':
        tom = Manager('Tom Doe', age=50, pay=50000)
        print tom.lastName()
        tom.giveRaise(.20)
        print tom.pay    
```    

> * The `Manager` class appears in a module of its own, but it could have been added to the Person module instead.(Python doesn't requires just one class per file).
    * It inherits the constuctor and last-name methods from its superclass
    * It customizes just the `giveRaise` method.
    
> In OOP, we program by customizing, not by changing.


### Refactoring Code

#### Augmenting Methods

* Implemented the customized `Manager` class by `augmenting` the inherited raise method instead of replacing it completely.

```

    class Manager(Person):
        def giveRaise(self, percent, bonus=0.1):
            Person.giveRaise(self, percent + bonus)
            
```

#### Display format

```
    class Person:
        def __str__(self):
            return '<%s => %s>' % (self.__class__.__name__, self.name)
    tom = Manager('Tom Jones', 50)
    print(tom)                               # prints: <Manager => Tom Jones>

```
#### Constructor customization

* We didn't pass the `job` argument when making a manager in Example 1-16; if we had, it would look like this with keyword arguments:
    `tom = Manager('Tom Doe', age=50, pay=50000, jog='manager')`
    
* Provide an explicit constructor for managers, when a manager is created, its job is filled in automatically.

```
    class Manager(Person):
        def __init__(self, name, age, pay):
            Person.__init__(self, name, age, pay, 'manager')

```
#### Alternative classes

```
    # Example 1-17. PP4E\Preview\person_alternative.py
    
    """
    Alternative implementation of person classes, with data, behavior,
    and operator overloading (not used for objects stored persistently)
    """

    class Person:
        """
            a general person: data + logic
        """
        
        def __init__(self, name, age, pay=0, job=None):
            self.name = name
            self.age = age
            self.pay = pay
            self.job = job
        
        def lastName(self):
            return self.name.split()[-1]
        def giveRaise(self, percent):
            self.pay *= (1.0 + percent)
            
        def __str__(self):
            return ( '<%s => %s: %s, %s>' %
                        (self.__class__.__name__, self.name, self.job, self.pay))
                        
    class Manager(Person):
        """
        a person with custom raise inherits general lastname, str
        """
        def __init__(self, name, age, pay):
            Person.__init__(self, name, age, pay, 'manager')
        def giveRaise(self, percent, bonus=0.1):
            Person.giveRaise(self, percent + bonus)
            

    if __name__ == '__main__':
        bob = Person('Bob Smith', 44)
        sue = Person('Sue Jones', 47, 40000, 'hardware')
        tom = Manager(name='Tom Doe', age=50, pay=50000)
        print sue, sue.pay, sue.lastName()
        
        for obj in (bob, sue, tom):
            obj.giveRaise(.10)
            print obj

```

#### Adding Persistence

* Store records in per-record pickle files

```
    # Example 1-18. PP4E\Preview\make_db_classes.py
    
    import shelve
    from person import Person
    from manager import Manager

    bob = Person('Bob Smith', 42, 30000, 'software')
    sue = Person('Sue Jones', 45, 40000, 'hardware')
    tom = Manager('Tom Doe', 50, 50000)

    db = shelve.open('class-shelve')
    db['bob'] = bob
    db['sue'] = sue
    db['tom'] = tom
    db.close()
```

* Read the shelve and prints fields of its records

```
    # Example 1-19. PP4E\Preview\dump_db_classes.py
    
    import shelve

    db = shelve.open('class-shelve')

    for key in db:
        print key, '=>\n    ', db[key].name, db[key].pay
        
    bob = db['bob']
    print bob.lastName()
    print db['tom'].lastName()    

```
* Update the records

```
    # Example 1-20. PP4E\Preview\update_db_classes.py
    
    import shelve

    db = shelve.open('class-shelve')

    sue = db['sue']
    sue.giveRaise(.25)
    db['sue'] = sue

    tom = db['tom']
    tom.giveRaise(.20)
    db['tom'] = tom

    db.close()    

```
    
## Step 4: Adding Console Interaction

### A Console Shelve Interface

* A simple interactive loop that allows a user to query multiple record objects in the shelve by key.

```
    # Example 1-21. PP4E\Preview\peopleinteract_query.py
    
    # interactive queries

    import shelve

    fieldnames = ('name', 'age', 'job', 'pay')
    maxfield = max(len(f) for f in fieldnames)
    db = shelve.open('class-shelve')

    while True:
        key = raw_input('\nKey? => ')
        if not key:break
        try:
            record = db[key]
        except:
            print 'No such key "%s"! ' % key
        else:
            for field in fieldnames:
                print field.ljust(maxfield), ' => ', getattr(record, field)    
```    


* Update from interactive console.     
    
    
    
    
    
    
    
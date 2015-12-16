

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
	
	
	
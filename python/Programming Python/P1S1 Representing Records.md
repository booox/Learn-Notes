
# Using Lists


```
    bob = ['Bob Smith', 42, 30000, 'software']
    sue = ['Sue Jones', 45, 40000, 'hardware']


    # fetch name, pay
    print bob[0], sue[2]

    # What's bob's last name?
    print bob[0].split()[-1]

    # give sue a 25% raise
    print sue[2] = sue[2] * 1.25
    # print sue[2] *= 1.25
    # --- ?? Can't run in IDLE -------

    # check sue
    print sue

```

```
    >>> bob = ['Bob Smith', 42, 30000, 'software']
    >>> sue = ['Sue Jones', 45, 40000, 'hardware']
    >>> bob[0], sue[2]
    ('Bob Smith', 40000)
    >>> bob[0].split()[-1]
    'Smith'
    >>> sue[2] *= 1.25
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


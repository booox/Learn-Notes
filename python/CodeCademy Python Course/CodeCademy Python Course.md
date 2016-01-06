
## String & Console Ouutput

* Three ways to create strings
```
    'Alpha'
    "Bravo"
    str(3)   

```
* String methods
```
    len("Charlie")
    "Delta".upper()
    "Echo".lower()
```

* Printing a string
```
    print "Foxtrot"
```
* Advanced printing techniques
```
    g = "Golf"
    h = "Hotel"
    print "%s, %s" % (g, h)
```


### STring Formatting with %

```
name = "Mike"
print "Hello %s" % (name)
```

```
print "The %s who %s %s!" % ("Knights", "say", "Ni")
# This will print "The Knights who say Ni!"

```

```
    name = raw_input("What is your name?")
    quest = raw_input("What is your quest?")
    color = raw_input("What is your favorite color?")

    print "Ah, so your name is %s, your quest is %s, " \
    "and your favorite color is %s." % (name, quest, color)

```


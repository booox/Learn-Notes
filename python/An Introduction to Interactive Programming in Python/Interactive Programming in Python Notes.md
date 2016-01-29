*Interactive Programming in Python Notes.md*


# Logic and comparisons


## Boolean Constans
* Type *bool* : *True* and *False* 
* Boolean expressions:
    * *and*
    * *or*
    * *not*
    
## Comparions
* compare operators
    * `>` 
    * `<` 
    * `>=` 
    * `<=` 
    * `==` 
    * `!=` 
    
    
## Conditionals

```
    def greet(friend, money):
        print 'Hi!'
        moeny = money - 20
        return moeny
        
    money = 15
    
    money = greet(True, money)
    print "Money:", money
    print ""
    
    money = greet(False, money)
    print "Money:", money
    print ""
    
    money = greet(True, money)
    print "Money:", money
    print ""
    

```

# Week 2a - Interactive applications in Python

## Event-driven programming

* General Programming Flow
    * `START -> A -> B -> C -> D -> ... -> END `
* Event-driven programming
    * `START -> INITIALIZE -> WAIT -> `
        * `EVENT1 -> WAIT <-> Handler1`
        * `EVENT2 -> WAIT <-> Handler2`
        * `"QUIT -> END"`
* Events
    * Input
        * Button
        * Text Box
    * Keyboard
        * key down
        * key up
    * Mouse
        * Click
        * Drag
    * Timer
    
## Local vs. global variables

* Global Variables

* Local Variables
    * Variables: Variables that define inside a function.
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
    
    
## Simple GUI

### GUI Program Structure

* Global (state)
* Helper functions
* Classes (later)
* Define event handlers
* Create a frame
* Register event handlers
* Start frame & timers

### Programming tips

#### Correct it!

* global variables
    ```
        n = 0
        
        def assign(x):
            n = x
            
        assign(2)
        assign(15)
        
        print n
    
    ```
* return None
    ```
        n = 0
        
        def decrement():
            global n
            n = n - 1
            
        x = decrement()
        
        print "x = ", x
        print "n = ", n
    
    ```
    
* Briefly
    * First
    ```
        def f(a, b):
            """ Returns True eactly when a is False and b is True. """
            if a == False and b == True:
                return True
            else:
                return False
        ```
    * Change 1:
    ```
        def f(a, b):
            """ Returns True eactly when a is False and b is True. """
            if not a and b:
                return True
            else:
                return False
        ```
    * Change 2:
    ```
        def f(a, b):
            """ Returns True eactly when a is False and b is True. """
            return not a and b
        ```
        
* Another Example
    * First
    ```
        def g(a, b):
            """ Returns False eactly when a and b are both True. """
            if a == True and b == True:
                return False
            else:
                return True
        ```
    * Changed:
    ```
        def f(a, b):
            """ Returns True eactly when a is False and b is True. """
            return  not (a and b)
        ```

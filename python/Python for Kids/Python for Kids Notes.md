


# Chapter 8. How to Use Classes and Objects

* why is a giraffe like a sidewalk?
    * A giraffe is a type of mammal, which is a type of animal. A giraffe is also an animate object - it's alive.
    * A sidewalk is an inanimate object (it's not alive).
    
## Breaking Things into Classes

* Things
    * Inanimate - Sidewalks
    * Animate - Animals - Mammals - Giraffes
* define classes
    ```
        class Things:
            pass
    ```
    
## Clidren and Parents
* define children class of the parent class
    ```
        class Inanimate(Things):
            pass
            
        class Animate(Things):
            pass
            
        class Sidewalks(Inanimate):
            pass
            
        class Animals(Animate):
            pass
        class Mammals(Animals):
            pass
        class Giraffes(Mammals):
            pass
    ```
    
## Adding Objects to Classes
* Say we have a giraffe named Reginald
    * We call Reginald an object of the class Giraffes.
    * Or we use the term *instance* of the class.
* `reginald = Giraffes()`

## Defining Functions of Classes

### Adding Class Characteristics as Functions
* 
    

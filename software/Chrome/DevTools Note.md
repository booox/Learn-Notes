
[Discover DevTools](http://discover-devtools.codeschool.com/)

# Chapter 1: Getting Started & Basic DOM and Styles

## Elements Tab

* Inspect the element
* Add Attribute / Edit Attribute
* Edit as HTML
* Change the location (Move Up / Down)
* Hide Element
* Delete Element
* Select an element

## Sources Tab

* `{}` : Pretty print
* Local modifications - revert

## Network Tab

* Resource info - size, type, etc
* Server response details
* Timeline of network  requests
* Avoid bad requests

## Console Tab

* Interact with your app's views and scripts
* Run Javascript commands
    ```document.getElementById('date');
        <h1 id=​"date" class=​"date">​…​</h1>​<b>​Mon​</b>​" Jan 04 2016"</h1>​
        
        console.log(console);
        
        > console.assert(1 == 1);
        < underfined
        console.assert(1 == 2);
        < Assertion failed
        
        document.getElementById('events');
        Calendar.countEvents();
        console.assert(Calendar.countEvents() == 3);
        
    ```
    * `console.assert(Calendar.countEvents() == 3);`
        * `var debugging=false; console.assert(debugging,"You are not debugging"); `
    * `console.log`
        * `console.log("I can't wait to run my 5K");`
        * `console.log("a", "b", "c")`
        * `console.log("Hello %s", "Console")`
    * `console.warn(message[, object])`
        * `console.warn("Watch out!")`
    * `console.info(message[, object])`
        * `console.info("%s you get a message", "Susan")`
    * `console.error(message[, object])`
        * `console.error("This ", "is ", "an ", "error!")`
    * `console.dir(document)`
    * `console.clear()`
      

## Debugger

## Profiles

## Frames
* HTML loading
* Javascript execution
* Styling
* Painting to screen

## Some Other Things
* Page Speed Plugin for Chrome
* Google Closure Compiler - making Javascript download and run faster
    
## 
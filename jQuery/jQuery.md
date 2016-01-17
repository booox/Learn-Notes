jQuery

* 23:18 2016/1/16 [codeskulptor](http://www.codeskulptor.org/docs.html)
    * div hide & display
    * Using jQuery
        * `<head></head>`  中加入
           * `<script src="https://code.jquery.com/jquery-1.10.2.js"></script>`
        * HTML & javascript
            ```
            <body>
            <p id="hello">Hello</p>
            <a id="clickme" href="#">Click to hide me too</a>
            <p id="p2">Here is another paragraph</p>
            
            <script>
            $( "#hello" ).hide();
            $( "a#clickme" ).click(function( event ) {
              $("#p2").toggle();
            });

            </script>
            </body>
            
            
            ```
            
# Links

* [jQuery - Official Site](http://jquery.com/)
* [Try jQuery](https://www.codeschool.com/courses/try-jquery)
* [jQuery Tutorial at W3schools](http://www.w3schools.com/jquery/)
* 
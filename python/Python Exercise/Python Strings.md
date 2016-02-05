
# Strings

## Creating Strings
### Single Line Strings
* Using Single quotes
    * `s = 'This is a String.'`
* Using Double quotes
    * `s = "This is a String."`
    
### Multi Lines Strings
* Using Three Single quotes
    * ```
        s = '''This is a String.
               Yes, this is a string.
               En!
            '''
      ```
* Using Double Single quotes
    * ```
        s = """This is a String.
               Yes, this is a string.
               En!
            """
      ```
## Handling Problems with Strings
* `EOL while scanning string literal`
    ```
    >>> s = 'python abc
    SyntaxError: EOL while scanning string literal
    >>> s = 'python abc'
    >>> s = "python abc
    SyntaxError: EOL while scanning string literal
    >>> s = "python abc"
    
    ```
* Mixture single and double quotes
    * 
    ```
    >>> s = 'He said:"I'm a good man."'
    SyntaxError: invalid syntax
    >>> s = '''He said:"I'm a good man."'''
    >>> print s
    He said:"I'm a good man."
    >>> s = 'He said:I'm a good man.'
    SyntaxError: invalid syntax
    >>> s = "He said:I'm a good man."
    >>> print s
    He said:I'm a good man.    
    ```
    * Using backslash(\)
    ```
    >>> s = 'He said:I'm a good man.'
    SyntaxError: invalid syntax
    >>> s = 'He said:I\'m a good man.'
    >>> print s
    He said:I'm a good man.
    
    ```
    
## Combining Strings
* Using Concatenation(+) Operator
    ```
    >>> n = 5 + 3
    >>> print n
    8
    >>> s = 'Hello' + 'Python'
    >>> print s
    HelloPython
    >>> s = 'Hello' + ' ' + 'Python'
    >>> print s
    Hello Python
    >>> s = 'Hello ' + 'Python'
    >>> print s
    Hello Python
    
    ```
    
## Substrings
* `len(s)`
    ```
    >>> print len('hello python')
    12
    ```
* string slicing
    ```
    >>> print s[0]
    h
    >>> print s[1]
    e
    >>> print s[-1]
    n
    >>> print s[-2]
    o
    >>> print s[11]
    n
    >>> print s[12]

    Traceback (most recent call last):
      File "<pyshell#70>", line 1, in <module>
        print s[12]
    IndexError: string index out of range
    >>> print s[-11]
    e
    >>> print s[-12]
    h
    >>> print s[-13]

    Traceback (most recent call last):
      File "<pyshell#73>", line 1, in <module>
        print s[-13]
    IndexError: string index out of range
    >>> print s[0:11]
    hello pytho
    >>> print s[0:12]
    hello python
    >>> print s[-1:-12]

    >>> print s[-1:]
    n
    >>> print s[-12:-1]
    hello pytho
    >>> print s[-12:]
    hello python
    >>> print s[:5]
    hello
    >>> print s[6:]
    python
    >>> print s[:]
    hello python
    >>> print s[::-1]
    nohtyp olleh
    
    ```
    
# Converting Strings
* 
    ```
    >>> >>> points = 1000
    >>> s1 = 'I scored'
    >>> s2 = ' points'
    >>> s1 = 'I scored '
    >>> s = s1 + points + s2

    Traceback (most recent call last):
      File "<pyshell#97>", line 1, in <module>
        s = s1 + points + s2
    TypeError: cannot concatenate 'str' and 'int' objects
    >>> print type(1000)
    <type 'int'>
    >>> print type(points)
    <type 'int'>
    >>> print type(s1)
    <type 'str'>
    >>> print type(s2)
    <type 'str'>
    >>> str(1000)
    '1000'
    >>> str(points)
    '1000'
    >>> print type(str(points))
    <type 'str'>
    >>> s = s1 + str(points) + s2
    >>> print s
    I scored 1000 points
    >>> print s1, points, s2
    I scored  1000  points
    
    ```
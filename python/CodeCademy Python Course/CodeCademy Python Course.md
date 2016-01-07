
## UNIT 1: Python Syntax
### Variables 变量
* 不论是创建Web应用、游戏都会遇到存储和处理不同类型的数据
* 他们都使用 *variables （ *变量 ）来完成这个任务
* Variable 就是给他一个特定的名称并使它来存储一段数据。
* ex: `span = 5`, 这里 *spam 里就存放了数字 *5 。


## UNIT 2: String & Console Ouutput

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



## UNIT 3: Conditionals & Control Flow

### Go With the Flow

* Compare Closely!
    * `==`, `!=`, `<`, `<=`, `>`, `>=`

    
* Boolean operators: To Be and/or Not to be 

```
         Boolean Operators
    ------------------------      
    True and True is True
    True and False is False
    False and True is False
    False and False is False

    True or True is True
    True or False is True
    False or True is True
    False or False is False

    Not True is False
    Not False is True

```

* Boolean operators Order:
    * not , and , or
    
### Conditional Statement Syntax

```
if 8 < 9:
    print "Eight is less than nine!"
```

```
response = 'Y'

answer = "Left"
if answer == "Left":
    print "This is the Verbal Abuse Room, you heap of parrot droppings!"
    
# Will the above print statement print to the console?
# Set response to 'Y' if you think so, and 'N' if you think not.

```
```
if some_function():
    # block line one
    # block line two
    # et cetera

```


* 用一个表达式替换第2行和第6行中的下划线，使之返回值 *True*

```
def using_control_once():
    if _______:
        return "Success #1"

def using_control_again():
    if _______:
        return "Success #2"

print using_control_once()
print using_control_again()

```

* `if ... else...` 完成 *else* 部分代码
   

```

answer = "'Tis but a scratch!"

def black_knight():
    if answer == "'Tis but a scratch!":
        return True
    else:             
        return       # Make sure this returns False

def french_soldier():
    if answer == "Go away, or I shall taunt you a second time!":
        return True
    else:             
        return        # Make sure this returns False
```

*  *elif* : 完成下划线部分语句
```
def greater_less_equal_5(answer):
    if ____:
        return 1
    elif ____:          
        return -1
    else:
        return 0
        
print greater_less_equal_5(4)
print greater_less_equal_5(5)
print greater_less_equal_5(6)


```

* The Big If

    * Comparators
        ```
        3 < 4
        5 >= 5
        10 == 10
        12 != 13
        ```
    * Boolean operators
    ```
        True or False 
        (3 < 4) and (5 >= 5)
        this() and not that()
    
    
    ```

    * Conditional statements
        ```
        if this_might_be_true():
            print "This really is true."
        elif that_might_be_true():
            print "That is true."
        else:
            print "None of the above."
        Let's get to the grand finale.
        ```
        
* 综合练习，完成下面练习
    * 使用 *if* ,  *elif* , *else*
    * 至少有一个 *and*, *or*, 或者 *not*
    * 使用比较运算符： (==, !=, <, <=, >, or >=);
    * 最后，返回True
    * 不要忘记在 *if* , *elif* , *else* 后面要有 **:**

```
# Make sure that the_flying_circus() returns True
def the_flying_circus():
    if ________:    # Start coding here!
        # Don't forget to indent
        # the code inside this block!
    elif ________:
        # Keep going here.
        # You'll want to add the else statement, too!

```

### PygLatin Game

* PygLatin Game:  "Python" ==> "ythonpay"

* STEPS
    * 让用户输入一个英语的单词
    * 验证用户输入是否有效
        * 长度
        * 英文字母
    * 将英语单词转化为Pig Latin
    
* 引导步骤
    * 打印一串字符试试： `print "Something"`
    * 接受并存储用户输入： `word = raw_input("Enter a word:")`
    * 验证用户是否有输入： `if len(word) < 0:`
    * 验证用户输入是否为字母：`"Hello123".isalpha() #False` 
        * 使用 *and* 连接
    * 多做几次测试你的代码，试着输入不同的内容，如单词、数字、空的内容、包含数字的单词、其它符号等等
    * 变换字符串，例如--python -> ythonpay
        * 创建一个变量，并将后缀 *ay* 赋给它：`pyg = "ay"`
        * 将字符串变成小写: `word = original.lower()`   
            ```
            the_string = "Hello"
            the_string = the_string.lower()
            ```
        * 获取单词第一个字母：`first  = word[0]` `second = word[1]`
        * 将字符串连接起来： `new_word = word + first + pyg`  这里有一个问题，就是单词首字母出现了两次
        * 将首字母排除：`new_word = word[1:len(new_word)] + first + pyg`
            或 `new_word = word[1:] + first + pyg`
            
        
## UNIT 4: Functions

### 函数的好处在哪里？
* 函数就是一段可以重复使用的代码，在程序中它用来完成特定的任务
* 当你遇到这样的情形时，你要考虑定义一个函数：
    * 你可能会重复使用一段代码，只是可能会变换很少的几个值
    
### 函数的组成
* 函数头（header）: 包括 `def` 关键词，函数的名称，函数可能需要的参数。
    * `def helloWorld():`
* 函数注释（comment）: 解释函数可以完成的功能
    * `"""Prints 'Hello World!' to the console."""`
    * 注意：使用三对双引号或单引号
* 函数主体(body) : 缩进的语句块，实现函数功能
    * `print "Hello World"`
    
```
def hello_world():
    """Prints 'Hello World!' to the console."""
    print "Hello World!"

```

### Call and Response
* 我们已经定义好了一个函数，`square`。用10来调用它（将10放在括号里）
```
def square(n):
    """Returns the square of a number."""
    squared = n**2
    print "%d squared is %d." % (n, squared)
    return squared
    
square(10)

```
### Parameters and Arguments
* Parameter, 函数定义时使用的变量，也被称为形参
* Argument, 函数被调用时实际的输入，也被称为实参
* `def add(x, y): return x + y`
    * *x *y is parameters
    * `add(2, 3)` , *2, *y is arguments
    
* 在函数定义部分，将下划线替换为形参 *base *exponent ，并用 *37 和 *4 来调用。
```
def power(___, ___):  # Add your parameters here!
    result = base**exponent
    print "%d to the power of %d is %d." % (base, exponent, result)

power(__, __)  # Add your arguments here!

```
### Functions Calling Functions 函数嵌套（函数里调用别的函数）
* 函数可以实现非常复杂的功能，如一个函数可以调用其他的函数
```
def fun_one(n):
    return n * 5

def fun_two(m):
    return fun_one(m) + 7
```
* 下面这两个函数，`one_good_turn(n)` 将给定的数加上1，`deserves_another(n)` 将给定的数加上2，修改 `deserves_another`的函数体body部分，使之调用`one_good_turn`并实现上述相同的功能
```
def one_good_turn(n):
    return n + 1
    
def deserves_another(n):
    return n + 2

```

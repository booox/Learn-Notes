
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



## Conditionals & Control Flow

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

## PygLatin Game

### PygLatin part 1
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
            
        
    
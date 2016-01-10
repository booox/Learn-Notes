Codecadema Python Course

# UNIT 1: Python Syntax

## 变量和数据类型 (Variables and Data Types)

### 变量 (Variables)
* 不论是创建Web应用、游戏都会遇到存储和处理不同类型的数据
* 他们都使用 *variables （ *变量 ）来完成这个任务
* Variable 就是给他一个特定的名称并使它来存储一段数据。
    * ex: `span = 5`, 这里 *spam 里就存放了数字 *5 。
    
### 布尔 (Booleans)
* 布尔数就像一个电灯的开关，它只有两个值。电灯开关只能是 *开* 或 *关* 两种状态，布尔数只有 *True* 或 *False* 两个值。
* 可以用变量将布尔值存储起来
    * `a = True`  `b = False`
* 设置下面变量
    * 将 7 赋给变量 *my_int*
    * 将 1.23 赋给变量 *my_float*
    * 将 True 赋给变量 *my_bool*

### 修改变量的值
* 我们已经知道可以用变量来存储值
* 我们还可以修改变量的值，只需要将新的值赋给原来的变量就可以了。
* 试试看：将变量的 *my_int* 的值从7改为3，然后 *print* 出来看看结果

## 缩进和语句
### 缩进
* 在Python中，使用缩进来控制代码的结果，这一点要特别注意。
* 下面的代码的结构存在问题，试着运行它看看有什么问题
    ```
    def spam():
    eggs = 12
    return eggs
            
    print spam()
    ```
* 正确的缩进使用4个空格（或按Tab键），修改后的代码如下：
    ```
    def spam():
        eggs = 12
        return eggs
            
    print spam()
    
    ```
## 注释
### 单句注释 (Single Line Comments)
* `#` 开头的语句代表是注释。Python不会运行这些代码，只是为了方便我们理解代码。
* 写一句注释

### 多行注释 (Multi-Line Comments)
* 三引号（三个单引号或三个双引号），如 `''' 注释内容 '''` 或 `""" 注释内容 """`

## 数学计算

### 做算术运算

* 可以进行加、减、乘、除运算
    ```
    addition = 72 + 23
    subtraction = 108 - 204
    multiplication = 108 * 0.5
    division = 108 / 9    
    ```
* 乘方
    ```
    eggs = 10 ** 2
    print eggs
    
    ```
* 求余
    ``` print 5 % 2 ```
    
### 回顾一下

* 到此我们学习了：
    * 变量，存储后面要用到的值
    * 数据类型，例如整型、浮点型和字符型
    * 缩进
    * 注释
    * 算术运算符: + - * / ** %

* 组合到一起
    * 在第一行写上注释
    * 设置变量圆的半径 *r* ，并赋值为 *8*
    * 设置变量PI *pi* ，并赋值为 *3.14*
    * 设置变量圆的面积 *area*, 并计算面积
    
## 章节练习: 餐饮账单
* 在餐饮用完餐，收到你的账单
    * 餐费（Cost of meal）: $44.50
    * 税率（Restaurant tax）: 6.75%
    * 小比例（Tip）: 15%

### 声明变量
* 声明变量，也就是定义一个变量
    * 声明一个变量 *meal* 并赋值 *44.50*
    * 声明一个变量 *tax* 并赋值 *0.0675* ( 6.75%)
    * 声明一个变量 *tip* 并赋值 *0.15* ( 15%)
    * 给变量 *meal* 重新赋值为：它本身 + 税费
    * 再一次给变量 *meal* 重新赋值为：它本身 + 税费  （答案：$54.63）
    
    
    
    

# UNIT 2: 字符串和控制台输出（String & Console Ouutput）

## 字符串（Strings）

### 字符串
* 另一种有用的数据类型是 **string** 。 **string** 可以用来存储字母、数字和符号。
* 例如：
    ```
    name = "Ryan"
    age = "19"
    food = 'cheese'
    
    ```
* 定义一个变量 *brain* 并赋值 *Hello Python* 。

### 转义字符
* 有些字符会产生问题，如： 
    ```
    >>> print 'There's a snake in my boot!'
    SyntaxError: invalid syntax
    
    ```
* 可以反斜线 `\` 来修正这个问题，就像这样：
    ```
    >>> print 'There\'s a snake in my boot!'
    There's a snake in my boot! 
    
    ```
### 通过索引（index）来获取字符
* 在字符串中的每一个字母都被安排与一个数字对应。这个数字就称为 **索引(index)** 。
    ```
    >>> 'cats'[0]
    'c'
    >>> 'Python'[3]
    'h'

    ```
* 在大多数的编程语言中，索引是从 *0* 开始数的，而不是从1。

    ```
    """
    The string "PYTHON" has six characters,
    numbered 0 to 5, as shown below:

    +---+---+---+---+---+---+
    | P | Y | T | H | O | N |
    +---+---+---+---+---+---+
      0   1   2   3   4   5

    So if you wanted "Y", you could just type
    "PYTHON"[1] (always start counting from 0!)
    """


    ```
* 试着定义一个变量 *fifth_letter* 并将 *Python* 的第五个字母赋给它。

## 字符串方法（Strings Methods）

* 我们已经知道如何存储字符串了，现在我们来了解如何通过字符串的一些方法来改变它们。
* 我们首先关注四个字符串的方法
    * `len()`
    * `lower()`
    * `upper()`
    * `str()`
    
* 首先来看获取字符串长度的方法 `len()`
    * 创建一个变量 *parrot* 并赋值 `"Norwegian Blue"`
    * 输出长度：`print len(parrot)`
    
* 再来看将大写字母转换成小写字母 `lower()`
    * 可以这样使用： `"Ryan".lower()` 返回 `ryan`
    * 输出小写字母： `print parrot.lower()`
    
* 小写转大写：`upper()`
    * `print parrot.upper()`
    
* 其他类型数据转换成字符串：`str()`
    * `str(2)   # 2 --> '2' `
    * `pi = 3.14; print str(pi)`
    
### 点标记（Dot Notation）
* 为什么 `len(string) str(object)`可以直接使用，而其他的却要使用点标记，如(`parrot.lower()`)
* 这是因为：
    * 使用点标记，是因为这些方法只对字符串才有效
    * 而 `len() , str()`对其他数据类型仍然有效
    
## 输出
### 输出字符串
* `print 'Hello Python'`

### 输出变量
* `pi = 3.14; print str(pi)`
    
## 高级输出
### 字符串连接运算符 (+)
* 在字符串之间使用 **+** 号，则会让字符串连接起来，一个接着一个。
* 使用 *+* 将 *I * , *love * , *Python* 这三个字符串连接起来！

### 连接字符串与别的类型的数据
* 当需要将字符串与非字符串类型的数据连接起来时，则需要用到 `str()` 函数
* 运行下面代码，若有错请修改：`print "I have " + 2 + " books!"`

### 字符串格式化 ( % )
* 当我们想在字符串中输出变量时，有一个比字符串连接更好的方法。
    ```
    name = "Mike"
    print "Hello %s" % (name)    
    ```
* 如上例，在字符串 `"Hello %s"` 后面的 *%* 被用来将变量与字符串连在一起
    * 它会用变量来替代字符串中的 *%s*
* 不上机运行，下面语句会输出什么？
    ```
    string_1 = "Camelot"
    string_2 = "place"

    print "Let's not go to %s. 'Tis a silly %s." % (string_1, string_2)    
    ```
* 注意： 
    * *%* 后面的变量是要放到括号里面去的
    * 括号里的变量数量要与前面的点位符 *%s* 的数量一样多
* 下面语句中的下划线应该换成什么？思考并上机操作验证你的想法：
    ```
    name = raw_input("What is your name?")
    quest = raw_input("What is your quest?")
    color = raw_input("What is your favorite color?")

    print "Ah, so your name is ___, your quest is ___, " \
    "and your favorite color is ___." % (name, quest, color)    
    
    ```
  
### 回顾一下

* 创建字符串的三种方式
```
    'Alpha'
    "Bravo"
    str(3)   

```
* 字符串的方法（String methods）
```
    len("Charlie")
    "Delta".upper()
    "Echo".lower()
```

* 输出字符串（Printing a string）
```
    print "Foxtrot"
```
* 高级输出技巧（Advanced printing techniques）
```
    g = "Golf"
    h = "Hotel"
    print "%s, %s" % (g, h)
```

## 日期和时间
### Python的时间库 `datetime`

* 导入时间库
    `from datetime import datetime`

* 获取当前日期和时间 `datetime.now()`
    ```
    from datetime import datetime

    print datetime.now()    
    ```
* 创建一个变量 *now* ，将当前时间赋给它，并输出到控制台。

### 提取年月日
* 提取相关信息
    ```
    from datetime import datetime
    now = datetime.now()

    print now.year
    print now.month
    print now.day   
    ```
* 将日期按指定格式输出，如 `mm-dd-yyyy`
    ```
    from datetime import datetime
    now = datetime.now()

    print '%s-%s-%s' % (now.year, now.month, now.day)
    # will print: 2014-02-19
    ```
* 根据上面例子，将日期按 `mm/dd/yyyy` 格式输出

### 提取时间

* hour, minute and second
    ```
    from datetime import datetime
    now = datetime.now()

    print now.hour
    print now.minute
    print now.second
    ```
* 将时间按 `hh:mm:ss` 格式输出

### 综合练习

* 将日期、时间按 `mm/dd/yyyy hh:mm:ss` 格式输出


# UNIT 3: Conditionals & Control Flow

## Python能做判断吗？
* 就像现实生活中一样，有时我们希望我们的代码能够根据情况判断后做出决定
* 我们前面的代码都是自上而下的执行下来，就像瀑布流动一样
* 而如果代码可以根据情况进行判断，我们就称之为“控制流”

## 比较运算符
* 有六个比较运算符：
    * `==`
    * `!=`
    * `>`
    * `>=`
    * `<`
    * `<=`
* 比较运算符，顾名思义，是用来比较两个值之间的大小关系（可以是数值，也可以是字符串）
* 参考注释给每一个 *boolean* 值写一个表达式
    * 至少使用三个不同的比较运算符
    * 不能只使用 *True* 或 *False*
    
    ```
    # Make me true!
    bool_one = 3 < 5  # 请参考这个例子

    # Make me false!
    bool_two = 

    # Make me true!
    bool_three = 

    # Make me false!
    bool_four = 

    # Make me true!
    bool_five = 

    ```
## 布尔运算符

* 布尔运算符根据布尔值进行比较。有三种布尔运算符：
    * `and` : 检查两边是否都为 **True**
    * `or` : 检查是否至少有一个为 **True**
    * `not` : 将给定布尔值反相
    
* 真假表（The Truth table ）

    ```
        """
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

        """    
    ```
###  And
* 当 *and* 两边值都为 *True* 时结果才为 *True*
    `1 < 2 and 2 < 3 is True`
    `1 < 2 and 2 > 3 is False`
    
* 练习 *and* 
    * 将 `False and False` 结果赋给变量 *bool_one*
    * 将 `-(-(-(-2))) == -2 and 4 >= 16**0.5` 结果赋给变量 *bool_two*
    * 将 `19 % 4 != 300 / 10 / 10 and False` 结果赋给变量 *bool_three*
    * 将 `-(1**2) < 2**0 and 10 % 10 <= 20 - 10 * 2` 结果赋给变量 *bool_four*
    * 将 `True and True` 结果赋给变量 *bool_five*
    
### Or
* 当 *or* 两边有一个值为 *True* 时结果就为 *True*
    `1 < 2 or 2 < 3 is True`
    `1 > 2 or 2 > 3 is False`
    
* 练习 *or* 
    * 将 `2**3 == 108 % 100 or 'Cleese' == 'King Arthur'` 结果赋给变量 *bool_one*
    * 将 `True or False` 结果赋给变量 *bool_two*
    * 将 `100**0.5 >= 50 or False` 结果赋给变量 *bool_three*
    * 将 `True or True` 结果赋给变量 *bool_four*
    * 将 `1**100 == 100**1 or 3 * 2 * 1 != 3 + 2 + 1` 结果赋给变量 *bool_five*
    
### Not
*  *not* 将 *True* 变成 *False* ，将 *False* 变成 *True* 。
    `not False is True`
    `not 41 > 40 is False`
    
* 练习 *or* 
    * 将 `not True'` 结果赋给变量 *bool_one*
    * 将 `not 3**4 < 4**3` 结果赋给变量 *bool_two*
    * 将 `not 10 % 3 <= 10 % 2` 结果赋给变量 *bool_three*
    * 将 `not 3**2 + 4**2 != 5**2` 结果赋给变量 *bool_four*
    * 将 `not not False` 结果赋给变量 *bool_five*
    
### 布尔运算符的优先级

* 优先级： *not* > *and* > *or* 
    
* 优先级练习
    * 将 `False or not True and True'` 结果赋给变量 *bool_one*
    * 将 `False and not True or True` 结果赋给变量 *bool_two*
    * 将 `True and not (False or False)` 结果赋给变量 *bool_three*
    * 将 `not not True or False and not True` 结果赋给变量 *bool_four*
    * 将 `False or not (True and True)` 结果赋给变量 *bool_five*
    
### 练习

* 使用布尔表达式按注释的要求给变量赋值
    * *not* , *and* , *or* 每个至少要用一次

    ```
        # Make me false!
        bool_one = (2 <= 2) and "Alpha" == "Bravo"  # 例子

        # Make me true!
        bool_two = 

        # Make me false!
        bool_three = 

        # Make me true!
        bool_four = 

        # Make me true!
        bool_five = 
    ```
    
    
    

## If, Else and Elif

### 条件语句的语法
* `if` 是一个条件语句，当它的表达式为 *True* 时，它下面的代码都会被执行。
* 例子： 
    ```
    if 8 < 9:
        print "Eight is less than nine!"
    ```
    * `8 < 9` 是判断表达式
    * `print "Eight is less than nine!"` 则是当表达式为真时要执行的语句
    
* 下面语句的 `print` 语句会不会被输出:
    ```
        response = 'Y'

        answer = "Left"
        if answer == "Left":
            print "This is the Verbal Abuse Room, you heap of parrot droppings!"    
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

### `Else` 语句
* `if ... else ...`语句的含义：
    * 当表达式为 *True* 时，执行 *if* 后面的语句，否则，执行 *else* 后面的语句。
* 实例：
    ```
        if 8 >= 9:
            print "8 >= 9"
        else:
            print "9 > 8"    
    ```

### Elif 语句
* `elif` 是 `else if`的缩写。
* 它的含义是： 如果这个表达式为真时，执行这个。
* 实例：   
    ```
    if 8 > 9:
        print "8 > 9"
    elif 8 < 9:
        print "8 < 9"
    else:
        print "8 = 9"   
        
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

### 回顾条件判断语句

* 比较运算符（Comparators）
    ```
    3 < 4
    5 >= 5
    10 == 10
    12 != 13
    ```
* 布尔运算符（Boolean operators）：
```
    True or False 
    (3 < 4) and (5 >= 5)
    this() and not that()


```

* 条件判断语句（Conditional statements）
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
    # returns True
    def the_flying_circus():
        if ________:    # Start coding here!

        elif ________:


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
            
        
# UNIT 4: Functions

## Lesson: Functions

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
D:\BaiduYun\SyanDisk\Study\Calibre Library
### What Good are Functions?
* 减少代码量，使结构更加清晰
* 可以被重复调用

### Practice Makes Perfect

* 定义一个名为 *cube* 的函数，返回一个数的立方
* 定义一个名为 *by_three* 的函数，如果一个数能被3整除，则返回这个数的立方，否则返回 *False* 。

```
def cube(number):
    return number ** 3
    
def by_three(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False
        

```

### I Know Kung Fu

* 不知道还记得前面有过 `import this`，这是导入一个模块的实例
* 模块( **module** )就是一个包含变量和函数定义的文件，一旦它被导入(import)，你就可以使用它们。
* 试着运行一下 `print sqrt(25)`
    * 提示出错：`"NameError: name 'sqrt' is not defined."`

### Generic Imports
* `import math`，此即被称为 *Generic *Imports*
* 语法：`import math`
* 举例： `import math` , 
* 用法：`math.sqrt(25)`
* 在`sqrt()` 前面插入 `math`，变成 `math.sqrt(25)`

### Function Imports
* 从模块中仅导入特定的变量或函数，被称为 **function import**
* 语法： `from module import function`
* 举例：`from math import sqrt`，这里`sqrt`后面不需要括号
* 用法： `sqrt(25)`

### Universal Imports
* 从模块中将所有的变量和函数全部导入进来，且不需要在前面写上模块名称
* 语法: `from module import *`
* 举例：`from math import *`
* 用法：`sqrt(25)`

### Here Be Dragons
* 如果你自己定义了一个函数名称叫 `sqrt`，同时你又 `import math`，这时你的函数是安全的
    * 这里有你的 `sqrt` 和 `math.sqrt`
* 但如果你使用 `from math import *`，那么你就会有两个不同的函数却有着相同的名称
* 因此，不建议使用 *Universal Imports* 这种方式导入，而使用下面两种方式：
    * `import math`  :  `math.sqrt(25)`
    * `from math import sqrt` : `sqrt(25)`，仅在需要的时候使用
* 查看模块可用的所有内容
    ```
        import math
        print dir(math)
    ```
    
### Built-in Functions

* Python的内置函数，不需要导入模块，即可直接使用
* 我们已经学过 `.upper()`, `.lower()`, `str()`, `len()`
* 练习：尝试理解下面内容
```
def biggest_number(*args):
    print max(args)
    return max(args)
    
def smallest_number(*args):
    print min(args)
    return min(args)

def distance_from_zero(arg):
    print abs(arg)
    return abs(arg)


biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)

```

* `max()`
* `min()`
* `abs()`
* `type()`  : 返回给定参数的数据类型
    
    
### Review: Functions

```
def shut_down(s):
    if s == 'yes':
        return 'Shutting down'
    elif s == 'no':
        return 'Shutting aborted'
    else:
        return 'Sorry'

```
### Review: Modules

* 让我们来看看如何导入模块
### Review: Built-In Functions
```
def is_numeric(num):
    return type(num) == int or type(num) == float:

max(2, 3, 4) # 4
min(2, 3, 4) # 2

abs(2) # 2
abs(-2) # 2

```
```
def distance_from_zero(num):
    if type(num) == int or type(num) == float:
        return abs(num)
    else:
        return 'Nope'

```

## Lesson: Taking a Vacation

### STEPS
* 回顾Python的函数
    ```
    def bigger(first, second):
        print max(first, second)
        return True
    ```
    * 定义一个没有参数、名称为answer的函数
    * 注意：括号和冒号别忘记
    ```
    def answer():
        return 42
    ```

* 定义旅行中需要花费的函数：Hotel, plane, car, other_spending
    * 定义一个计算住宿的函数：hotel_cost，有一个参数 *nights* , 每晚140
        ```
        def hotel_cost(nights):
        return 140 * nights
        ```
    * 定义一个计算大交通费用的函数： *plane_ride_cost*  有一个字符串参数 *city* ，不同城市飞机的费用列表如下
        * "Charlotte": 183
        * "Tampa": 220
        * "Pittsburgh": 222
        * "Los Angeles": 475
        
        ```
        def hotel_cost(nights):
            return 140 * nights
            
        def plane_ride_cost(city):
            if city == "Charlotte":
                return 183
            elif city == "Tampa":
                return 220
            elif city == "Pittsburgh":
                return 222
            elif city == "Los Angeles":
                return 475
        ```
    * 到了城市之后的出行方式采用租车，定义一个计算租车费用的函数： *rental_car_cost*  , 有一个整数参数  *days*
        * 每天租车费用 40
        * *if* 如果租车7天及以上，会有从总计里减50的优惠
        * *elif* 如果租车3天及以上，会有从总计里减20的优惠
        * 只能享受其中一种优惠
        * 返回总的费用
        
        ```
        def rental_car_cost(days):
            day_price = 40
            if days >= 7:
                car_cost = day_price * days - 50
            elif days >= 3:
                car_cost = day_price * days - 20
            else:
                car_cost = day_price * days
            return car_cost        
        
        ```
    * 定义一个计算全部费用的函数： *trip_cost* 有两个参数， *city* 和 *days* 
    
        ```
        def trip_cost(city, days):
            total = hotel_cost(days) + plane_ride_cost(city) + rental_car_cost(days)
            return total
        
        ```
    * 旅行中除了上述费用，肯定还会有美食和纪念品，修改上述 *trip_cost* 函数， 添加一个参数 *spending_money* 
    
        ```
        def trip_cost(city, days, spending_money):
            total = hotel_cost(days) + plane_ride_cost(city) + rental_car_cost(days) + spending_money
            return total
        
        ```
    * 全部的代码如下：
        ```
        def hotel_cost(nights):
            return 140 * nights
            
        def plane_ride_cost(city):
            if city == "Charlotte":
                return 183
            elif city == "Tampa":
                return 220
            elif city == "Pittsburgh":
                return 222
            elif city == "Los Angeles":
                return 475
        def rental_car_cost(days):
            day_price = 40
            if days >= 7:
                car_cost = day_price * days - 50
            elif days >= 3:
                car_cost = day_price * days - 20
            else:
                car_cost = day_price * days
            return car_cost        
            
        def trip_cost(city, days, spending_money):
            total = hotel_cost(days) + plane_ride_cost(city) + rental_car_cost(days) + spending_money
            return total
            
        
        ```
        
    * Let's take a trip! 我们计划来一次说走就走的旅行，为期5天，去"Los Angeles"，另有额外600元的其他花销。
        `print trip_cost("Los Angeles", 5, 600)`
    
    

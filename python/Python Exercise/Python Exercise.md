

## 字符串

* 输入一个字符串，利用 *while* 循环将该字符串字符按从后往前顺序输出，每个字符一行。
    [string-backwards.py]
    
* *fruit* 是一个字符串，统计其中字母 *a* 出现的次数。
    * [count-char.py]
* 将上述练习扩展成一个函数，函数名为 *count*  将字母在字符串中出现的次数输出，字符串和字母作为参数。
    * [count-char-def.py]
 
* 输入一个字符串，统计其中每个字母出现的次数。    
    * [count-chars.py]
    
## 文件

* 写一个程序读取一个文件，将文件内容一行一行的打印输出，并全部为大写。
    * [line-print-uppercase.py]
    
    
    raised hand with part between middle and ring fingers.
    
## 函数


    
## 逻辑与条件判断（Logic and Conditionals ）

* 定义一个函数， *is_even* ，整数 *number* 作为参数，当 *number* 为偶数是返回 *True* ，否则为 *False* 。
    * [Logic and Conditionals/is_even.py]
    
* 定义一个函数， *is_cool* ，字符串 *name* 作为参数，当 *name* 为 "Joe", "John", "Stephen" 其中之一时返回 *True* ，否则为 *False* 。
    * [Logic and Conditionals/is_cool.py]



## Programming tips

* *NameError* 
    * 
    ```
    def volume_cube(side):
        return sidde ** 3
        
    s = 2
    print "Volume of ", s, "is", volume(s)
    
    ```
    * 
    ```
    def random_dice():
        die1 = random.randrange(1, 7)
        die2 = random.randrange(1, 7)
        return die1 + die2
        
    print random_dice()
    print random_dice()
    print random_dice()
    
    ```
* *AttributeError*     
    * 
    ```
        import math
        def volume_sphere(radius):
            return 4.0 / 3.0 * math.Pi * (radius ** 3)
            
        r = 2
        print volume_sphere(r)
    ```
* *TypeError*
    * 
    ```
        def area_triangle(base, height):
            return 0.5 * base * height
            
        b = "5"
        h = "2 + 2"
        print area_triangle(b)
    
    ```
    
* *SyntaxError*
    * 
    ```
        def is_mary(x)
            if x = "Mary":
                print "Found Mary!"
            else:
                print "No Mary."
                
        is_mary(Mary)
        is_mary(Fred)
    
    ```
    
* clear and readable
    * Not clear
    ```
        import math
        
        def area(a,b,c):
            s = (a+b+c) / 2.0
            return math.sqrt(s*(s-a)*(s-b)*(s-c))
    
    ```
    * modified
    ```
        import math
        
        def area_triangle_sss(side1, side2, side3):
            """
            Returns area of a triangle, given the lengths of
            its three sides.
            """
            
            # Heron's Formula
            semi_perim = (side1 + side2 + side3) / 2.0
            return math.sqrt(semi_perim *
                                    (semi_perim - side1) *
                                    (semi_perim - side2) *
                                    (semi_perim - side3))
    
    ```
* for debugging
    * 
    ```
        def favorites(instructor):
            """ Returns the favorite thing of the given instructor."""
            
            if instructor == "Joe":
                return "games"
            elif instructor == "Scott":
                return "ties"
            elif instructor == "John"
                return "outdoors"
                
        print favorites("John")
        print favorites("Jeannie")
            
    
    ```

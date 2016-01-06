
> 这里记录一些与Python相关的第一次知道的，或一直理解错的。

* print()
    * 一直用的是python2.x，打印输出直接 `print something`
    * 刚知道可以`print(*objects, sep=' ', end='\n', file=sys.stdout) `可以将内容输出到文件
    * 而在python2.x中使用，则很可能被当做一个**关键词**，而不是一个**语句**从而出错，解决办法：在开始使用语句：`from __future__ import print_function`
    * 或在python2.x中，使用`print >>filename, 'something'`
    * 另：使用`help(__builtins__)`可以查看一些内置函数的帮助，但`print`这个在python2.x中却帮了倒忙。

    
* sys.stdout, sys.stdin
	* sys.stdout与print 
		* 当我们在 Python 中打印对象调用 print obj 时候，事实上是调用了 sys.stdout.write(obj+'\n')
		* print 将你需要的内容打印到了控制台，然后追加了一个换行符
		* print 会调用 sys.stdout 的 write 方法
		* 以下两行在事实上等价：
			* `sys.stdout.write('hello'+'\n') `
			* `print 'hello'`
	
	* sys.stdin 与 raw_input
		* 当我们用 raw_input('Input promption: ') 时，事实上是先把提示信息输出，然后捕获输入
		* 以下两组在事实上等价：
			* `hi=raw_input('hello? ') `
			* `print 'hello? ', #comma to stay in the same line `
			* `hi=sys.stdin.readline()[:-1] # -1 to discard the '\n' in input stream`
	* 引自：[ Python的sys.stdout、sys.stdin重定向](http://blog.csdn.net/sxhlovehmm/article/details/41479005)
	
* raw_input() 与 input()
	* raw_input() 	-- python 2.x
	* input() 			-- python 3.x
	
* Check Python in 32 bit mode
	```
		>>> import sys, platform
		>>> platform.architecture()
		('64bit', 'WindowsPE')
		>>> sys.maxint
		2147483647				# 64bit: 9223372036854775807
		[Ref](http://stackoverflow.com/questions/3411079/why-does-the-python-2-7-amd-64-installer-seem-to-run-python-in-32-bit-mode)
	```
    
* SQL,
    * `INSERT OR IGNORE INTO` 忽略重复数据的插入
    * `INSERT OR REPLACE INTO ` 如果该行不存在，则插入；如果存在，则替换之
        * 这比`UPDATE`要好一些：因为当该行不存在时，则`UPDATE`不会有任何操作
	
* buffer(), memoryview()
	* buffer()用在2.x，memoryview()用在python3(python 2.7中也添加了此用法)
	* 在使用很大的数据时，应该使用此函数
	* 作用：引用了支持buffer/memoryview的对象（如string）的一个切片，但不占用额外的内存空间
	* 示例：
		```
			>>> s = 'Hello world'
			>>> t = buffer(s, 6, 5)
			>>> t
			<read-only buffer for 0x10064a4b0, size 5, offset 6 at 0x100634ab0>
			>>> print t
			world
			
			>>> s = 'Hello world'
			>>> t = memoryview(s)
			>>> t
			<memory at 0x0000000002CE3438>
			>>> print t[6:].tobytes()
			world			
		
		```
	* [What is Python buffer type for?](http://stackoverflow.com/questions/3422685/what-is-python-buffer-type-for)
    
    
* BeautifulSoup()
    * You can add, remove, and modify a tag’s attributes. Treat the tag as a dictionary.
        ```
            tag['class'] = 'verybold'
            tag['id'] = 1
            tag
            # <blockquote class="verybold" id="1">Extremely bold</blockquote>

            del tag['class']
            del tag['id']
            tag
            # <blockquote>Extremely bold</blockquote>

            tag['class']
            # KeyError: 'class'
            print(tag.get('class'))
            # None        
        ```
    * tag_wrap = soup.find('div', class_='wrapper')
    * tag_wrap = soup.find_all('li')
    
* try...except...finally...raise,  [python try/except/finally](http://blog.csdn.net/spch2008/article/details/9343207#)
    *  try不仅捕获异常，而且会恢复执行
    ```
        def catcher():
            try:
                fetcher(x, 4)
            except:
                print "got exception"
            print "continuing"    
    ```
    
    * 无论try是否发生异常，finally总会执行
    
    ```
        def catcher():
            try:
                fetcher(x, 4)
            finally:
                print 'after fecth'    
    ```
    
    *  try无异常，才会执行else
    ```
        def catcher():
            try:
                fetcher(x, 4)
            except:
                print "got exception"
            else:
                print "not exception"    
    ```
    > else作用：没有else语句，当执行完try语句后，无法知道是没有发生异常，还是发生了异常并被处理过了。通过else可以清楚的区分开。
    
    *  利用raise传递异常
    ```
        def catcher():
            try:
                fetcher(x, 4)
            except:
                print "got exception"
                raise    
    ```
    > raise语句不包括异常名称或额外资料时，会重新引发当前异常。如果希望捕获处理一个异常，而又不希望
异常在程序代码中消失，可以通过raise重新引发该异常。

    *  except(name1, name2)
    ```
        def catcher():
            try:
                fetcher(x, 4)
            except(TypeError, IndexError):
                print "got exception"
            else:
                print "not exception"
    ```
    > 捕获列表列出的异常，进行处理。若except后无任何参数，则捕获所有异常。
    
    
* 执行Python的CGI脚本
    * （Common Gateway Interface）在这里是指一种基于浏览器的输入、在Web服务器上运行的程序方法
    * CGI脚本使你的浏览器与用户能交互.这个脚本通常象服务器和系统中其他程序如数据库的桥梁。
    * 首先考虑到nginx作为web server
    * 但据说，原生Nginx不能直接执行外部CGI程序，因此需要依赖spawn-fcgi来执行
    
* Command-line arguments
    * The list of command line arguments passed to a Python script. 
    * argv[0] is the script name (it is operating system dependent whether this is a full pathname or not). 
    
```
    import sys

    print sys.argv
    for arg in sys.argv:
        print arg
        
    fname = sys.argv[1]
    fh = open(fname, 'r')
    text = fh.read()
    print fname, len(text)
```

* `os.popen(cmd)`
    * *cmd* is a shell command.
    * The return value is a file pointer that behaves just like an open file.
    * You can read the output one line at a time with `readline()` or get the whole thing at once with `read()`
    ```
        import os
        
        cmd = 'ipconfig/all'
        cp = os.popen(cmd)
        print cp.read()
    
    ```
    
* Paths
    * relative path : A string that describes where a file or directory is stored relative to the current working directory.
    * absolute path : A string that describes where a file or directory is stored that starts at the "top of the tree of directories" .
    * current working directory: The current working directory that you are **in**.

* Python System Path for Windows
    * PATH=PATH;c:\python26 => 可以在cmd中打开python shell，或使用`python file.py`来运行python程序
    * PATHEXT=PATHEXT;.PY;.PYM => 可直接运行.py程序
    
## Lists

* Reverse a List:   `['a', 1, '2', 'c'][::-1]`
    * The are seven sequence types: strings, Unicode strings, lists, tuples, bytearrays, buffer, and xrange objects.
    * The sequence operations sorted in ascending priority:
        1 `x in s`  `2 in [1, 2, 3]`
        2 `x not in s`  `4 not in [1, 2, 3]`
        3 `s + t`  `'hello' + 'world'`
        4 `s * n` or `n * s`  `'hello ' * 5`
        5 `s[i]`  `'hello'[2]`
        6 `s[i:j]`  `'hello'[1:2]`
        7 `s[i:j:k]`  `'hello'[::-1]`
        8 `len(s)`  `len('hello')`
        9 `min(s)`  `min([2, 3, 'a', 55])`
        10 `max(s)`  `max([2, 3, 'a', 55])`
        11 `s.index(x)`  `[2, 3, 'a', 55].index('a')`
        12 `s.count(x)`  `[2, 3, 'a', 55].count('a')`

        

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
    
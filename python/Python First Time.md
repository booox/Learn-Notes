
> 这里记录一些与Python相关的第一次知道的，或一直理解错的。

* print()
    * 一直用的是python2.x，打印输出直接 `print something`
    * 刚知道可以`print(*objects, sep=' ', end='\n', file=sys.stdout) `可以将内容输出到文件
    * 而在python2.x中使用，则很可能被当做一个**关键词**，而不是一个**语句**从而出错，解决办法：在开始使用语句：`from __future__ import print_function`
    * 或在python2.x中，使用`print >>filename, 'something'`
    * 另：使用`help(__builtins__)`可以查看一些内置函数的帮助，但`print`这个在python2.x中却帮了倒忙。

    
    
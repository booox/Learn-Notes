
# Linux

## 数据分析有关操作

* `$ head -n 3 data.csv`
* `$ tail -n 3 data.csv`
* `$ grep 'data' data.csv`
* `$ wc -l filename`
* `$ wc -w filename`
* `$ ls -IR /home/yoyo | grep js | wc -l`

* sort
    * `$ sort -nrk 1 data`
    * `-n` : 按数字排序
    * `-r` : 逆序排序
    * `-k N` : 按第N列排序
    * `-d` : 按字典排序
    
* sort+
    * 消除重复行： `$ sort unsort.txt | uniq`
    * 制表符转空格： `$ cat text | tr '\t' ' '`
    * 截取文件的第2，4 列： `$ cut -f 2, 4 filename`
    * 按列拼接两个文件： `$ paste file1 file2 -d ","`
    * 改变文件编码： `$ iconv -f GBK -t UTF-8 file1 -o file2`
    
    
    
# Python 科学计算库
    
## Python 科学计算库
    * ![Python 科学计算库](images/Python Data Library.jpg)
    
## 分析流程中的Python

    * ![分析流程中的 Python](images/Python Data Steps.jpg)
    
    * *Obtain* : Python
    * *Scrub* : pandas, IPython
    * *Explore* : matplotlib, SciPy, Seaborn
    * *Model* : sklearn, NumPy
    * *iNterpret* : BOKEH, js
    
## Python的数据相关模块

### 本课程用到
* *IPython* : 增强的交互式运行环境 (浏览器即软件)
* *NumPy* : 数组数据结构和矩阵计算
* *SciPy* : 科学计算
* *Matplotlib* : 数组绘图
* *Pandas* : 提供data frames 数据结构，对结构化/非结构化数据的转换以及灵活处理
* *Statsmodels* : 统计模型，数据挖掘
* *Scikit-learn* : 机器学习

### 可能涉及
* *Requests* : 网页数据抓取
* *BeautifulSoup* : 解析网页数据
* *Flask* : 轻型web框架
* *sqlite3* : 轻量级数据库接口
    
### 更高级的数据模块
* *Pyspark* : Spark的Python接口
* *nltk* : 自然语言处理器
* *networkx* : 社交网络分析
* *theano* : 深度学习

### 其它
* *wordcloud* : 词云绘图工具
* *Louvain算法* : 社交网络挖掘
* *xgboost* : Gradient boosting工具
* *processing 3* : 可视化

    
### 科学计算套件：Anaconda

* [Anaconda]()
* Why you'll love Anaconda?
    > Making it easy to install, intuitive to discover, quick to analyze, simple to collaborate, and accessible to all.
    
* 有这样一些特点：
    * 开源，全平台
    * 开放的数据科学
        * 330+ 流行的Python或R数据
    * 数据引擎
    * 大数据
        * Hadoop, Spark, Clusters & GPUs
    * 高性能运算
        * 分布式算法
    

# 补充阅读
-[] [Ipython官网](http://ipython.org/)
-[] [Ipython Quick Ref Sheets](https://damontallen.github.io/IPython-quick-ref-sheets/)
-[] [利用Python进行数据分析 第三章]()
-[] [Numerical Python, Chapter 1]()
-[] [python for scientists, Chapter 2]()
-[] [命令行中的数据科学(Optional)]()

    
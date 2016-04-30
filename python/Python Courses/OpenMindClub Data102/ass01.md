# 你认为应该用什么样的数字来度量中国人的生活水平变化？
*  尝试找到这样的数据源并画出图看看。
*  用这种数字来衡量有什么样的缺点？

## 应该用什么样的数字来度量中国人的生活水平变化？
### 首先要理解什么叫生活水平

* Ref: [Standard of living](https://en.wikipedia.org/wiki/Standard_of_living)

> Standard of living refers to the level of wealth, comfort, material goods and necessities available to a certain socioeconomic class in a certain geographic area. The standard of living includes factors such as income, quality and availability of employment, class disparity, poverty rate, quality and affordability of housing, hours of work required to purchase necessities, gross domestic product, inflation rate, number of holiday days per year, affordable (or free) access to quality healthcare, quality and availability of education, life expectancy, incidence of disease, cost of goods and services, infrastructure, national economic growth, economic and political stability, political and religious freedom, environmental quality, climate and safety. The standard of living is closely related to quality of life.[1] In 2013, the Human Development Index ranked the top six countries for quality of living as: Norway, Australia, Switzerland, Netherlands, United States and Germany.

* 从上面可以看出：
    * 生活水平是指在特定地区特定阶层的财富、舒适度、产品和必需品的供给的水平。
    * 生活水平包含许多因素，诸如：
        * 收入水平
        * 就业水平
        * 阶级的不平均水平
        * 财富的分布
        * 住房的质量及可负担
        * 工作时间
        * 用于购买必需品的工作时间
        * 通货膨胀率
        * 每年可休假的时间
        * 预期寿命（life expectancy）
        * 患病几率()
        * ……
* 由此可见衡量一个地区的生活水平，不是由单一的某种指标就能简单的衡量，相反需要多种指标综合考量。
* 生活水平通常由人均真实收入和贫穷比例来衡量。而其它的如健康的获得及质量、收入增长的不平均和受教育的标准也被当作衡量指标。
    * 例如可用某种产品的具体程度（如每1000人拥有的冰箱数量），或衡量健康可用平均寿命。
* 重要指标：
    * Human Development Index
    * Gini coefficient
    
### 采用哪些指标？

* 根据上述资料，决定采用以下指标：
    * Human Development Index
    

## 尝试找到这样的数据源并画出图看看。

### Human Development Index

* 数据来源：
    * [Trends in the Human Development Index, 1990-2014](http://hdr.undp.org/en/composite/trends)
    * [List of countries by Human Development Index](https://en.wikipedia.org/wiki/List_of_countries_by_Human_Development_Index)

* 画出图来
    * ![Trends in the Human Development Index, 1990-2014](images/Trends in the Human Development Index, 1990-2014.jpg)
    * ![List of countries by Human Development Index](images/List of countries by Human Development Index.jpg)


*  用这种数字来衡量有什么样的缺点？
    * 指标只能从某一个侧面来反映人们的生活水平，不能全面了解
    * 用于指标的数据的来源可能未必真实可信

# 理解什么是双盲实验

* reference
    * [Blind experiment](https://en.wikipedia.org/wiki/Blind_experiment)
    * [何谓三盲试验？](http://www.dxy.cn/bbs/thread/9819796#9819796)
    
## 先了解一下什么是盲试验

* 盲试验： 即在试验中，为了降低或消除偏好的影响，而将测试的信息对参与者隐藏，直到试验结果被知晓后。
* 通常可以分成以下几种：
    * 单盲： 只有研究者了解分组情况，受试者不知道自己是试验组还是对照组。
    * 双盲：研究者和受试者都不清楚试验分组情况，而是由研究设计者来安排和控制全部试验。
    * 三盲：研究者、受试者和资料分析者均不知道受试者分组情况。

* 盲试验是科学方法中一种重要的工具，它被用在非常多的领域，如学术研究中的医学、心理学和社会科学，自然科学中的物理学和生物学，应用科学中的市场调研等等。 


# 学习使用Google ngram服务，并研究你关心的某一组词汇的变化。

## 根据下面的参考文章，Google ngram相关内容如下
### ngram 由来

* 谷歌与哈佛大学的两名研究人员共同开发了一套数据库，可以对历年的单词和短语使用频率进行统计，从而了解文化和语言的变迁过程。
* 谷歌的确已经对近520万本可供用户免费下载和搜索的数字图书进行了摘选，从而建立起了庞大的数据库。
* Google 对书籍的处理不仅是扫描，还进行了数字化。
* 这个数据宝库汇集了大量的单词和短语及其每年出现的频率。
* 该数据库包含的5000亿个单词选自1800至2000年出版的各种书籍，
* 语种包括英语、法语、西班牙语、德语、汉语、俄语和希伯来语。
* 该数据库的目标受众是学者，
* 但同时也提供了Google Books Ngram Viewer（https://books.google.com/ngrams）这样一款简单的网络工具
* Ngram Viewer收录的单词或短语需满足一项要求：该词或短语在某年出版的超过40本书中出现过，才会有该年该词的数据点。

### Google ngram用法

* 用户都可以输入不超过5个单词的字符串，从而了解其历年来使用频率的折线图
* Ngram Viewer在发布后一段时间后也增加了通配符及词形变化及多种大小写风格的搜索功能
  * 比如搜索“President *_NOUN”就可以了解“President”后出现频率最高的名词

### Google ngram用法举例

* ![Marriage vs Sex](http://mmbiz.qpic.cn/mmbiz/GIhWrtDH6qefmKNnV79z4ejwwPOrkQ60r7IapFproGdJzbWMBlCdHxBowU5k7RZWlXVuGdh3Re4iaSh5GGYbVBA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1)
* ![几个国家的出现率变化情况](https://pic4.zhimg.com/34ca540a78a6fc7409aa9516c34db383_b.jpg)
* ![物理、化学、地理](images/)
  * 物理有两个有趣的突出，大概时间为，一个1850~1870，另一个为1940~1960，想想看什么原因？

* ![语文与英语](images/)
  * 可以看到在非常长的一时间里，英语一直占据很大优势，直到建国后语文成功超过英语，但自67年往后，英语开始发力，直到83年前后英语再度超越语文，并仍以很快的速度上升，而语文则越发下降。


**我特想了解一下“中华民族”这个词的发展，却不得知


## Some Links

* [https://books.google.com/ngrams](https://books.google.com/ngrams)
* [Google Ngram：词频趋势数据神器丨语言学午餐](http://mp.weixin.qq.com/s?__biz=MjM5MTA5MjcxMA==&mid=207357877&idx=1&sn=a5b64cd9b5ac346da30e7f06de869bdd&scene=2&from=timeline&isappinstalled=0#rd)
* [一个玩得停不下来的Google神器：Ngram](https://zhuanlan.zhihu.com/p/20165483)



# 理解什么是 Simpson's Paradox








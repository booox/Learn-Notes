#coding=utf-8

import string
import operator

fname = raw_input('Enter filename:')
if len(fname) < 1: 
    fname = 'Little Prince.txt'
    
try:
    fhand = open(fname)
except:
    print 'Wrong Filename!'
    exit()
    
total_words = {}            # 新建空白字典
for line in fhand:
    line = line.translate(None, string.punctuation)     # 去掉标点符号
    line_words = line.split()                                     # 将每行拆分成一个一个的单词
    for word in line_words:
        word = word.lower()                                         # 将单词变成小写
        total_words[word] = total_words.get(word, 0) + 1    # 将单词添加到 total_words 字典中
        

# 将获得的字典按值从大到小排序
items = sorted(total_words.items(), key=operator.itemgetter(1), reverse=True)

# for item in items:
for item in items[:30]:    
    print item[0], '\t', item[1]
    

#coding=utf-8

fruit = 'strawberry'

def count(string, char):
    count = 0
    for _char in string:
        if _char == char:
            count = count + 1

    print 'There are %d times %s in %s' % (count, char, string)
    
count(fruit, 'a')
count(fruit, 'r')
count(fruit, 'y')


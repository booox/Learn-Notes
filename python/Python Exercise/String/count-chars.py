#coding=utf-8

fruit = 'strawberry'

char_dict = {}

for char in fruit:
    char_dict[char] = char_dict.get(char, 0) + 1

print 'The word is :', fruit
for k, v in char_dict.items():
    print k, ':', v


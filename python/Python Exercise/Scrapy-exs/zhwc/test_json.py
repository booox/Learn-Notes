#coding = utf-8

import json

fname = 'blog_content.json'

with open(fname) as f:
    json_data = json.load(f)
    
print type(json_data)
# print json_data[0]['link'], json_data[0]['title']

count = 0
for item in json_data:
    count += 1
    print count, type(item['title']), item['title'].encode('gbk', 'ignore'), item['link']
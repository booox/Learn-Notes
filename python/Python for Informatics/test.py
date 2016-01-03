import urllib
import urllib2

url = 'http://img3.douban.com/view/photo/photo/public/p2264580551.jpg'
img = urllib2.urlopen(url)

fhand = open('51.jpg', 'w')
# fhand.write(img)
# fhand.close()

size = 0
while True:
    info = img.read(100000)
    if len(info) < 1: break
    size = size + len(info)
    fhand.write(info)
    
    
print size, 'characters copied.'
fhand.close()
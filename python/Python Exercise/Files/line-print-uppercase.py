#coding=utf-8

fname = raw_input('Enter file name:')
if len(fname) < 1: fname = 'mbox-short.txt'

try:
    fhand = open(fname)
except:
    print "Wrong File Name!"
    exit()
    
count = 0
for line in fhand:
        line = line.upper().rstrip()
        print line, ':', len(line)
        count = count + 1
        if count >1:
            break
        

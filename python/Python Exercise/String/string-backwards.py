#coding=utf-8

string = raw_input('Enter a string:')
if len(string) < 1:
    print 'Please input a string!'
else:
    
    print "Your input is:", string

    index = -1
    while index >= -len(string):
        print string[index]
        index = index -1
        
    print '-'*5
    
    index = -1
    while True:
        if index < -len(string):            
            break
        print string[index]
        index = index - 1
        
    print '-'*5
        
    for c in string[::-1]:
        print c
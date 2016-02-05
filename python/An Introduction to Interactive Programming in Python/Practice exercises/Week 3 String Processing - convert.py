#coding=utf-8

def convert(val):
    """ Convert xx.yy to xx dollars and yy cents """
    dollars = int(val)
    cents = int((val - dollars) * 100)
    return str(dollars) + " dollars and " + str(cents) + " cents"
    
print convert(11.22)
print convert(0.22)
print convert(1.00)
print convert(0)
print convert(-1.40)
print convert(12.45545454)



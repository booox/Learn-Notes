# Given any initial natural number,
# consider the sequence of numbers generated 
# by repeatedly following the rule:
# 	divide by two if the number is even or
# 	multiply by 3 and add 1 if the number is odd.

# http://www.codeskulptor.org/#user41_9cg8Wj92g1_1.py

import simplegui

# global state
n_list = []


# helper functions

def init(start):
    """Initializes n."""
    global n
    n = start
    print "Input is", n
    
def get_next(current):
    # n is even
    if current % 2 == 0:	
        return current / 2
    else:
        return current * 3 + 1

# timer callback

def update():
    """???  Part of mystery computation."""
    global n, n_list

    if n == 1:
        timer.stop()
        print "Output is", n
        n_list.sort()
        print 'Largest Number is:', n_list[-1]
    else:

        n = get_next(n)
        n_list.append(n)
        print n,



timer = simplegui.create_timer(1, update)

# start program
init(217)
timer.start()


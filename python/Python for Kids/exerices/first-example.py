import os
import turtle

t = turtle.Pen()

# t.forward(50)
# t.left(90)
# t.forward(50)
# t.left(90)

count = 0
while count < 4:
    t.forward(50)
    t.left(90)
    count = count + 1

    
t.reset()

t.backward(100)
t.up()
t.left(90)
t.forward(20)
t.right(90)
t.down()
t.forward(100)
os.system('pause')

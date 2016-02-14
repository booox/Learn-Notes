import simplegui
import random

# http://www.codeskulptor.org/#user41_FHT56XWWk1_0.py
# Global Variables
message = 'Python is Fun'
x = 30
y = 30

# Handler for timer
def timer_handler():
    global x, y
    x = random.randrange(0, 200)
    y = random.randrange(0, 200)
    
# for draw
def draw(canvas):
    global message, x, y
    canvas.draw_text(message, [x, y], 16, 'Red')
    
frame = simplegui.create_frame('Test Timer', 200, 200)
frame.set_draw_handler(draw)

frame.start()

timer = simplegui.create_timer(1000, timer_handler)
print timer.is_running()
timer.start()



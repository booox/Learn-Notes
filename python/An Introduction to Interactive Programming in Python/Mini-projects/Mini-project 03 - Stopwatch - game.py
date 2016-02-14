# template for "Stopwatch: The Game"
# http://www.codeskulptor.org/#user41_Kn09QGpGvL_2.py


import simplegui
import time

# define global variables
WIDTH = 300
HEIGHT = 300
main_count = 0
message = ' '
stop_count = 0
bingo_count = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    minute = t / 600
    second = abs((t - minute * 600)) / 10
    m_second = abs(t - minute * 600 - second * 10)
    return "%d:%02d.%d" % (minute, second, m_second)

# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()

def stop():
    global main_count, stop_count, bingo_count
    stop_count += 1
    if main_count % 10 == 0:
        bingo_count += 1
    timer.stop()

def reset():
    global main_count, stop_count, bingo_count
    timer.stop()
    main_count = 0
    stop_count = 0
    bingo_count = 0
    

# define event handler for timer with 0.1 sec interval
def timer():
    global main_count
    main_count += 1
#    print main_count

# define draw handler
def draw(canvas):
    global message, main_count, stop_count, bingo_count
    message = format(main_count)
    canvas.draw_text(message, [150, 150], 25, 'Red')
    bingo_message = str(bingo_count) + "/" + str(stop_count)
    canvas.draw_text(bingo_message, [WIDTH - 50, 30], 25, 'Red')
    
# create frame
frame = simplegui.create_frame('Stopwatch: The Game', WIDTH, HEIGHT)

btn_start = frame.add_button('Start', start, 100)
btn_stop = frame.add_button('Stop', stop, 100)
btn_reset = frame.add_button('Reset', reset, 100)

# register event handlers
frame.set_draw_handler(draw)

# start frame
frame.start()

timer = simplegui.create_timer(100, timer)


# Please remember to review the grading rubric

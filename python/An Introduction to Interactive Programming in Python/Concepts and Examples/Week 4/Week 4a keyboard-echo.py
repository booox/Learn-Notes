
import simplegui

# initialize state
current_key = ' '

# event handler
def keydown(key):
    global current_key
    current_key = chr(key)
    
def keyup(key):
    global current_key
    current_key = ' '
    
def draw(canvas):
    if current_key in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
        canvas.draw_text(current_key, [10, 20], 20, 'Red')
    
# create frame
frame = simplegui.create_frame('Test Keyboard', 30, 30)

# register event handlers
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_draw_handler(draw)

# start frame
frame.start()
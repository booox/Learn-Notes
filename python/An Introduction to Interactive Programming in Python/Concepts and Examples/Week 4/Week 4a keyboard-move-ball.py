
import simplegui

# initialize state
WIDTH = 300
HEIGHT = 300

ball_pos = [WIDTH / 2, HEIGHT / 2]


# event handler
def keydown(key):
    val = 4
    if key == simplegui.KEY_MAP['up']:
        ball_pos[1] -= val
    elif key == simplegui.KEY_MAP['down']:
        ball_pos[1] += val
    elif key == simplegui.KEY_MAP['left']:
        ball_pos[0] -= val
    elif key == simplegui.KEY_MAP['right']:
        ball_pos[0] += val
        
def draw(canvas):
    canvas.draw_circle(ball_pos, 10, 1, 'Black', 'Red')
    
# create frame
frame = simplegui.create_frame('Ball Move', WIDTH, HEIGHT)


# register event handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)

# start frame
frame.start()
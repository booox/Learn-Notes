# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

# CodeSkulptor runs in Chrome 18+, Firefox 11+, and Safari 6+.
# Some features may work in other browsers, but do not expect
# full functionality.  It does NOT run in Internet Explorer.

# http://www.codeskulptor.org/#user41_9cg8Wj92g1_0.py

import simplegui

message = "Welcome!"

# Handler for mouse click
def click():
    global message
    message = "Good job!"

# Handler to draw on canvas
def draw(canvas):
    # canvas.draw_text(message, [50,112], 48, "Red")
    canvas.draw_circle([150, 150], 120, 1, 'Black', 'White')
    canvas.draw_circle([150, 150], 110, 1, 'Black', 'White')    
    
    canvas.draw_circle([150, 150], 100, 1, 'White', 'Black')
    canvas.draw_circle([150, 150], 90, 1, 'White', 'Black')    
    
    canvas.draw_circle([150, 150], 80, 1, 'Black', '#00BCCF')
    canvas.draw_circle([150, 150], 70, 1, 'Black', '#00BCCF')
    
    canvas.draw_circle([150, 150], 60, 1, 'Black', 'Red')   
    canvas.draw_circle([150, 150], 50, 1, 'Black', 'Red')
    
    canvas.draw_circle([150, 150], 40, 1, 'Black', 'Yellow')
    canvas.draw_circle([150, 150], 20, 1, 'Black', 'Yellow')
    canvas.draw_circle([150, 150], 10, 1, 'Black', 'Yellow')
    canvas.draw_circle([150, 150], 1, 1, 'Black')
    

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 300, 300)
frame.set_canvas_background('White')
frame.add_button("Click me", click)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()

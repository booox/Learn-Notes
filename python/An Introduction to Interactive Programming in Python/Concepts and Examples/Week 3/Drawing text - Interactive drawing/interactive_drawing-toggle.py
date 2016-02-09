import simplegui

# Global Variables
canvas_width = 300
canvas_height = 300
toggle = False
text = ""

# Envent handler

def draw(canvas):
    global toggle, text
    if toggle:
        canvas.draw_text(text, [100, 100], 24, "Red")

def toggle_image():
    global toggle
    toggle = not toggle
#    print text
    
def text_input_handler(input_text):
    global text
    text = str(input_text)


# create frame
frame = simplegui.create_frame("Test", canvas_width, canvas_height)

frame.add_input('Input something', text_input_handler, 100)
frame.add_button('display toggle', toggle_image, 100)

frame.set_draw_handler(draw)

# start frame
frame.start()
# interactive application to convert a float in dollars and cents
# http://www.codeskulptor.org/#user41_RycsA8N2RA_0.py

import simplegui

# define global value
value = 0


# Handle single quantity
def convert_units(val, name):
    result = str(val) + " " + name
    if val > 1:
        result = result + "s"
    return result
        
# convert xx.yy to xx dollars and yy cents
def convert(val):
    # Split into dollars and cents
    dollars = int(val)
    cents = int(round(100 * (val - dollars)))
    

    # Convert to strings
    dollars_string = convert_units(dollars, "dollar")
    cents_string = convert_units(cents, "cent")

    # return composite string
    if dollars == 0 and cents == 0:
        return "Broke!"
    elif dollars == 0:
        return cents_string
    elif cents == 0:
        return dollars_string
    else:
        return dollars_string + " and " + cents_string
    
#print str(convert(0))

# define draw handler
def draw(canvas):
    global value    
    
    try:
        value = float(value)
        draw_text = convert(value)
    except Exception, x:
        # print 'Error:', x
        draw_text = "Please Input a Number."          
 
        
    canvas.draw_text(draw_text, [20, 100], 24, "White")
    
def input(text_input):
    global value
    value = text_input
        
    
# create frame
frame = simplegui.create_frame("Convert", 300, 200)

frame.add_input("Enter Value", input, 100)

# register event handler
frame.set_draw_handler(draw)

# start frame
frame.start()
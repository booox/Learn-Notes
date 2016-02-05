# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random

secret_number = 0
user_input = 0
range_top = 100 - 1
max_tries = 5

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number, range_top
    print ""
    print "Range is [0, " + str(range_top + 1) + ")"
    secret_number = random.randrange(0, range_top)

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global range_top
    range_top = 100 - 1
    new_game()
   
    # remove this when you add your code    
    # pass

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global range_top
    range_top = 1000 - 1
    new_game()

    # pass
    

    

    
    
def input_guess(guess):
    # main game logic goes here	
    global secret_number, user_input, range_top, max_tries
    try_count = 0
    try:
        user_input = int(guess)
        try_count = try_count + 1
        print "Guess was %s" % (user_input), 
        # check
        if secret_number == user_input:
            print 'Correct'
        elif secret_number > user_input and user_input >= 0:
            print 'Lower'
        elif secret_number < user_input and user_input < range_top:
            print 'Higher'
        else:
            print 'Out of guesses.'     
        
    except:
        print 'Wrong Input!'
        # exit()
        

    
# create frame
frame = simplegui.create_frame("Guess", 200, 200)


# register event handlers for control elements and start frame
frame.add_input('Enter', input_guess, 100)
frame.add_button("Range is [0,100)", range100, 200)
frame.add_button("Range is [0,1000)", range1000, 200)

# call new_game 
new_game()

frame.start()

# always remember to check your completed program against the grading rubric
